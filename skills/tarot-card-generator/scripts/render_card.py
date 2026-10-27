#!/usr/bin/env python3
"""Render one tarot card locally: FLUX art -> ESRGAN/upscale -> framed title card.

Chains the frozen deck style (assets/style.md) + the frozen workflow
(assets/tarot-card-flux.json) + frame_card.py into one call. The ONLY per-card
inputs are the scene description, the title, and the seed.

    python3 render_card.py \
        --scene "A hooded figure sets a glowing keystone into a stone arch..." \
        --title "The Keystone" --seed 271828 --out work/cards/the-keystone/the-keystone_271828.png

Prereqs: ComfyUI running locally with flux1-dev-fp8.safetensors and
4x-UltraSharp.pth installed; the `comfy` CLI on PATH. Emits a JSON line on
success: {"ok":true,"out":...,"seed":...,"comfy_file":...,"raw":...}.

--from-card "<Card Name>" regenerates a card from its card file (content/cards/<slug>.md) alone: it runs
the record's base workflow, re-applies each recorded repair (a Qwen edit pasted back
inside its box and tone-matched when recorded so, or a fill_disc / fill_halo sky fill), frames with the recorded title and frame flags, and writes the
same record into the output PNG.

The framed card PNG carries a render record (PNG text chunk `tarot_render`):
seed, title, scene, full prompt, frame flags, ComfyUI version and the executed
ComfyUI graph. place_card.py attach copies it into the card file.
"""
import argparse, json, os, re, subprocess, sys, time, urllib.request, uuid
from datetime import datetime

from PIL import Image, ImageDraw, ImageFilter, PngImagePlugin

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
STYLE_MD = os.path.join(SKILL, "assets", "style.md")
WORKFLOW = os.path.join(SKILL, "assets", "tarot-card-flux.json")
FRAME = os.path.join(HERE, "frame_card.py")
RECORD_KEY = "tarot_render"  # PNG text chunk read by place_card.py attach

def read_frame_flags():
    """Parse the frozen frame flags from assets/style.md § Frame flags.

    style.md is the single source of truth; a deck-level frame change edited there
    takes effect here with no code change. Lines are `--flag value` with optional
    `# ...` comments; pure-comment lines (e.g. the font note) are skipped.
    """
    txt = open(STYLE_MD, encoding="utf-8").read()
    i = txt.index("## Frame flags")
    m = re.search(r"```(?:\w*)\n(.*?)```", txt[i:], re.S)
    if not m:
        raise SystemExit("style.md: no fenced block after '## Frame flags'")
    flags = []
    for line in m.group(1).splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            flags.extend(line.split())
    return flags


def read_style_blocks():
    """Return (style_block, tail) from the two fenced blocks under their headers."""
    txt = open(STYLE_MD, encoding="utf-8").read()

    def fenced_after(header):
        i = txt.index(header)
        m = re.search(r"```(?:\w*)\n(.*?)```", txt[i:], re.S)
        if not m:
            raise SystemExit(f"style.md: no fenced block after '{header}'")
        return m.group(1).strip()

    return fenced_after("## Style block"), fenced_after("## Frame-agnostic tail")


def comfy_json(args):
    r = subprocess.run(["comfy", "--json"] + args, capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"comfy {' '.join(args)} failed:\n{r.stdout}\n{r.stderr}")


def comfy_version(url):
    try:
        with urllib.request.urlopen(f"{url}/system_stats", timeout=5) as r:
            return json.load(r)["system"].get("comfyui_version")
    except Exception:
        return None


def embed_record(card_png, raw_png, record):
    """Write the render record into the framed card as PNG text chunk `tarot_render`.

    The record travels with the file, so copying the card keeps it; place_card.py attach
    copies it into the card file. `workflow` is the executed ComfyUI graph (API
    format) that ComfyUI embedded in the raw output: models, LoRA, sampler, size,
    upscaler — everything needed to re-render without the ComfyUI output file.
    """
    graph = Image.open(raw_png).info.get("prompt")
    if not graph:
        raise SystemExit(f"{raw_png}: ComfyUI output has no embedded 'prompt' graph")
    record["workflow"] = json.loads(graph)
    write_record(card_png, record)


def write_record(card_png, record):
    """Store `record` in card_png's `tarot_render` PNG text chunk (re-saves the PNG)."""
    img = Image.open(card_png)
    img.load()
    info = PngImagePlugin.PngInfo()
    info.add_itxt(RECORD_KEY, json.dumps(record, ensure_ascii=False))
    img.save(card_png, pnginfo=info)


def note_record(card):
    """Return the render record JSON from the card file content/cards/<slug>.md § Render Record."""
    from card_repo import card_record
    return card_record(card)


def post_graph(url, graph):
    """Run an API-format graph on ComfyUI; return the output image filenames."""
    req = urllib.request.Request(f"{url}/prompt", json.dumps({"prompt": graph, "client_id": str(uuid.uuid4())}).encode(),
                                 {"Content-Type": "application/json"})
    try:
        pid = json.load(urllib.request.urlopen(req))["prompt_id"]
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ComfyUI rejected the graph:\n{e.read().decode()}")
    while True:
        time.sleep(3)
        h = json.load(urllib.request.urlopen(f"{url}/history/{pid}"))
        if pid in h:
            h = h[pid]
            if h["status"].get("status_str") == "error":
                raise SystemExit(json.dumps(h["status"]["messages"])[-3000:])
            return [i["filename"] for o in h["outputs"].values() for i in o.get("images", [])]


def upload_image(url, path):
    """Upload path to ComfyUI's input folder under a unique name; return that name."""
    name = f"tarot_src_{uuid.uuid4().hex[:8]}.png"
    boundary = uuid.uuid4().hex
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{name}\"\r\n"
            "Content-Type: image/png\r\n\r\n").encode() + open(path, "rb").read() + f"\r\n--{boundary}--\r\n".encode()
    urllib.request.urlopen(urllib.request.Request(f"{url}/upload/image", body,
                                                  {"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return name


def paste_back(orig, edit, box, feather):
    """Keep `edit` only inside box (x0,y0,x1,y1) with a soft edge; `orig` everywhere else."""
    if edit.size != orig.size:
        raise SystemExit(f"edit is {edit.size}, art is {orig.size}; cannot paste back")
    mask = Image.new("L", orig.size, 0)
    ImageDraw.Draw(mask).rectangle(tuple(box), fill=255)
    return Image.composite(edit, orig, mask.filter(ImageFilter.GaussianBlur(feather / 2)))


def repair_graph(repair, image_name):
    """A recorded repair's edit graph, pointed at a freshly uploaded source image."""
    graph = json.loads(json.dumps(repair["workflow"]))
    for node in graph.values():
        if node["class_type"] == "LoadImage":
            node["inputs"]["image"] = image_name
    return graph


def from_note(args):
    """Regenerate a card from its card file's render record: base render, repairs, frame."""
    url, record = args.comfy_url, note_record(args.from_note)
    outdir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(outdir, exist_ok=True)
    outs = post_graph(url, record["workflow"])
    base = next((f for f in outs if "final" in f), outs[-1])
    art = args.keep_raw or os.path.join(outdir, ".render_raw.png")
    urllib.request.urlretrieve(f"{url}/view?filename={base}&type=output", art)
    edits = []
    from repair_tools import fill_disc, fill_halo, tone_match
    for rep in record.get("repairs", []):
        if rep.get("method") == "fill_disc":          # deterministic sky fill, no ComfyUI
            fill_disc(Image.open(art), rep["box"], rep["grow"], rep["thresh"])[0].save(art)
            edits.append("fill_disc")
            continue
        if rep.get("method") == "fill_halo":          # deterministic rim fill, no ComfyUI
            fill_halo(Image.open(art), rep["box"], rep["grow"])[0].save(art)
            edits.append("fill_halo")
            continue
        fn = post_graph(url, repair_graph(rep, upload_image(url, art)))[0]
        tmp = os.path.join(outdir, ".edit_out.png")
        urllib.request.urlretrieve(f"{url}/view?filename={fn}&type=output", tmp)
        orig = Image.open(art).convert("RGB")
        pasted = paste_back(orig, Image.open(tmp).convert("RGB"), rep["box"], rep["feather"])
        if rep.get("tone_match"):
            pasted = tone_match(orig, pasted, rep["box"], rep["feather"])[0]
        pasted.save(art)
        os.remove(tmp)
        edits.append(fn)
    fr = subprocess.run([sys.executable, FRAME, "--art", art, "--title", record["title"],
                         "--out", args.out] + record["frame_flags"], capture_output=True, text=True)
    if fr.returncode != 0:
        raise SystemExit(f"frame_card.py failed:\n{fr.stdout}\n{fr.stderr}")
    write_record(args.out, record)
    if not args.keep_raw:
        os.remove(art)
    print(json.dumps({"ok": True, "out": args.out, "seed": record["seed"], "comfy_file": base,
                      "repair_files": edits, "raw": args.keep_raw or None}))


def node_id(nodes, cls):
    ids = [n["id"] for n in nodes if n["type"] == cls]
    if not ids:
        raise SystemExit(f"workflow has no {cls} node")
    return ids[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", help="card-specific scene description")
    ap.add_argument("--title")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--from-card", "--from-note", dest="from_note", metavar="CARD",
                    help="regenerate CARD from its card file's ## Render Record (base render + recorded repairs); "
                    "replaces --scene/--title/--seed (--from-note is the old name)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--comfy-url", default=os.environ.get("COMFY_LOCAL_URL", "http://127.0.0.1:8188"))
    ap.add_argument("--workflow", default=WORKFLOW)
    ap.add_argument("--keep-raw", default=None, help="path to also keep the unframed art")
    args = ap.parse_args()
    if args.from_note:
        if args.scene or args.title or args.seed is not None:
            ap.error("--from-card takes the scene, title and seed from the card file; omit them")
        return from_note(args)
    if not (args.scene and args.title and args.seed is not None):
        ap.error("--scene, --title and --seed are required (or use --from-card)")

    style_block, tail = read_style_blocks()
    prompt = f"{style_block}\n\n{args.scene.strip()}\n\n{tail}"

    # work on a copy so the bundled workflow stays pristine
    wf = os.path.join(os.path.dirname(os.path.abspath(args.out)) or ".", ".render_wf.json")
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.workflow) as f:
        open(wf, "w").write(f.read())

    nodes = comfy_json(["workflow", "ls-nodes", wf])["data"]["nodes"]
    pos = node_id(nodes, "CLIPTextEncode")
    ks = node_id(nodes, "KSampler")
    # set-slot needs the server's node list; the comfy CLI refuses to fetch it from a
    # non-loopback host, so pass it as --input. Through with-comfy the URL is loopback anyway;
    # this keeps a direct LAN URL working too.
    # Without this check a refused set-slot rendered the workflow's default scene at seed 0.
    oi = os.path.join(os.path.dirname(wf), ".object_info.json")
    urllib.request.urlretrieve(f"{args.comfy_url}/object_info", oi)
    ss = comfy_json(["workflow", "set-slot", wf, f"{pos}.text={prompt}",
                     f"{ks}.seed={args.seed}", "--input", oi])
    if not ss.get("ok"):
        raise SystemExit(f"set-slot failed: {json.dumps(ss.get('error'))}")

    # --timeout: wait out other jobs (e.g. a YuE song) queued ahead on the shared server
    run = comfy_json(["run", "--workflow", wf, "--where", "local", "--wait", "--timeout", "3600"])
    if not run.get("ok"):
        raise SystemExit(f"render failed: {json.dumps(run.get('error'))}")
    outs = run["data"].get("outputs", [])
    final = next((u for u in outs if "final" in u), outs[-1] if outs else None)
    if not final:
        raise SystemExit("no output image produced")

    fn = re.search(r"filename=([^&]+)", final).group(1)
    raw = args.keep_raw or os.path.join(os.path.dirname(os.path.abspath(args.out)),
                                        ".render_raw.png")
    urllib.request.urlretrieve(f"{args.comfy_url}/view?filename={fn}&type=output", raw)

    frame_flags = read_frame_flags()
    fr = subprocess.run([sys.executable, FRAME, "--art", raw, "--title", args.title,
                         "--out", args.out] + frame_flags, capture_output=True, text=True)
    if fr.returncode != 0:
        raise SystemExit(f"frame_card.py failed:\n{fr.stdout}\n{fr.stderr}")
    embed_record(args.out, raw, {
        "rendered": datetime.now().astimezone().isoformat(timespec="seconds"),
        "comfyui_version": comfy_version(args.comfy_url),
        "comfy_file": fn, "seed": args.seed, "title": args.title,
        "scene": args.scene.strip(), "prompt": prompt, "frame_flags": frame_flags,
    })

    if not args.keep_raw:
        try:
            os.remove(raw)
        except OSError:
            pass
    try:
        os.remove(wf)
    except OSError:
        pass
    print(json.dumps({"ok": True, "out": args.out, "seed": args.seed,
                      "comfy_file": fn, "raw": (args.keep_raw or None)}))


if __name__ == "__main__":
    main()
