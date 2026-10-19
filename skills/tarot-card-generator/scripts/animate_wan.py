#!/usr/bin/env python3
"""Animate one card image with Wan 2.2 on the host ComfyUI; saves frames as PNGs.

  animate_wan.py --model 14b|5b --image <local PNG, uploaded; or a name already in ComfyUI input> --prompt "..." --seed N --prefix <name>

14b = Wan 2.2 i2v 14B fp8 + lightx2v 4-step LoRAs, WanFirstLastFrameToVideo with the same image as
first and last frame (loops by construction); 576x1008, 81 frames @16 fps. --full drops the LoRAs
      (template's 20-step run: more motion, ~5x slower).
5b  = Wan 2.2 ti2v 5B, start image only; 576x1024, 121 frames @24 fps.
Settings follow ComfyUI's templates video_wan2_2_14B_flf2v and video_wan2_2_5B_ti2v.
"""
import argparse, http.client, json, os, time, urllib.request

HOST = os.environ.get("COMFY_LOCAL_URL", "http://127.0.0.1:8188").rstrip("/")  # set by with-comfy
NEG = ("色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，"
       "JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，"
       "手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走")


def common(image, prompt, vae):
    return {
        "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "type": "wan", "device": "default"}},
        "pos": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["clip", 0], "text": prompt}},
        "neg": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["clip", 0], "text": NEG}},
        "vae": {"class_type": "VAELoader", "inputs": {"vae_name": vae}},
        "img": {"class_type": "LoadImage", "inputs": {"image": image}},
    }


def build_14b(image, prompt, seed, prefix, w=576, h=1008, length=81, fast=True):
    # fast: lightx2v 4-step LoRAs (cfg 1, shift 5); else the template's full run (20 steps, cfg 4, shift 8)
    steps, cfg, shift = (4, 1.0, 5.0) if fast else (20, 4.0, 8.0)
    g = common(image, prompt, "wan_2.1_vae.safetensors")
    for side in ("high", "low"):
        g[f"unet_{side}"] = {"class_type": "UNETLoader", "inputs": {"unet_name": f"wan2.2_i2v_{side}_noise_14B_fp8_scaled.safetensors", "weight_dtype": "default"}}
        src = [f"unet_{side}", 0]
        if fast:
            g[f"lora_{side}"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"model": src, "lora_name": f"wan2.2_i2v_lightx2v_4steps_lora_v1_{side}_noise.safetensors", "strength_model": 1.0}}
            src = [f"lora_{side}", 0]
        g[f"ms_{side}"] = {"class_type": "ModelSamplingSD3", "inputs": {"model": src, "shift": shift}}
    g["flf"] = {"class_type": "WanFirstLastFrameToVideo", "inputs": {"positive": ["pos", 0], "negative": ["neg", 0], "vae": ["vae", 0], "width": w, "height": h, "length": length, "batch_size": 1, "start_image": ["img", 0], "end_image": ["img", 0]}}
    g["k1"] = {"class_type": "KSamplerAdvanced", "inputs": {"model": ["ms_high", 0], "add_noise": "enable", "noise_seed": seed, "steps": steps, "cfg": cfg, "sampler_name": "euler", "scheduler": "simple", "positive": ["flf", 0], "negative": ["flf", 1], "latent_image": ["flf", 2], "start_at_step": 0, "end_at_step": steps // 2, "return_with_leftover_noise": "enable"}}
    g["k2"] = {"class_type": "KSamplerAdvanced", "inputs": {"model": ["ms_low", 0], "add_noise": "disable", "noise_seed": 0, "steps": steps, "cfg": cfg, "sampler_name": "euler", "scheduler": "simple", "positive": ["flf", 0], "negative": ["flf", 1], "latent_image": ["k1", 0], "start_at_step": steps // 2, "end_at_step": 10000, "return_with_leftover_noise": "disable"}}
    g["dec"] = {"class_type": "VAEDecode", "inputs": {"samples": ["k2", 0], "vae": ["vae", 0]}}
    g["save"] = {"class_type": "SaveImage", "inputs": {"images": ["dec", 0], "filename_prefix": prefix}}
    return g


def build_5b(image, prompt, seed, prefix, w=576, h=1024, length=121):
    g = common(image, prompt, "wan2.2_vae.safetensors")
    g["unet"] = {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_ti2v_5B_fp16.safetensors", "weight_dtype": "default"}}
    g["ms"] = {"class_type": "ModelSamplingSD3", "inputs": {"model": ["unet", 0], "shift": 8.0}}
    g["lat"] = {"class_type": "Wan22ImageToVideoLatent", "inputs": {"vae": ["vae", 0], "width": w, "height": h, "length": length, "batch_size": 1, "start_image": ["img", 0]}}
    g["k"] = {"class_type": "KSampler", "inputs": {"model": ["ms", 0], "seed": seed, "steps": 20, "cfg": 5.0, "sampler_name": "uni_pc", "scheduler": "simple", "positive": ["pos", 0], "negative": ["neg", 0], "latent_image": ["lat", 0], "denoise": 1.0}}
    g["dec"] = {"class_type": "VAEDecode", "inputs": {"samples": ["k", 0], "vae": ["vae", 0]}}
    g["save"] = {"class_type": "SaveImage", "inputs": {"images": ["dec", 0], "filename_prefix": prefix}}
    return g


def get_json(req, tries=6):
    """urlopen + json with retries: the host's ComfyUI drops a connection now and then. Only for idempotent calls."""
    for t in range(tries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=120))
        except (OSError, http.client.HTTPException, json.JSONDecodeError):
            if t == tries - 1:
                raise
            time.sleep(5 * (t + 1))


def upload(path):
    """Upload a local image to ComfyUI's input folder (needed on a host whose input is not mounted); returns its name."""
    import uuid
    boundary = uuid.uuid4().hex
    name = os.path.basename(path)
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{name}\"\r\n"
            f"Content-Type: image/png\r\n\r\n").encode() + open(path, "rb").read() + \
           f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(HOST + "/upload/image", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"})
    return get_json(req)["name"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["14b", "5b"], required=True)
    ap.add_argument("--image", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--full", action="store_true", help="14b only: no lightx2v speed-up LoRAs; 20 steps, cfg 4 (~5x slower, more motion)")
    a = ap.parse_args()
    if os.path.isfile(a.image):  # a local file: upload it; otherwise --image names a file already in ComfyUI's input
        a.image = upload(a.image)
    g = build_14b(a.image, a.prompt, a.seed, a.prefix, fast=not a.full) if a.model == "14b" else build_5b(a.image, a.prompt, a.seed, a.prefix)
    req = urllib.request.Request(HOST + "/prompt", json.dumps({"prompt": g}).encode(), {"Content-Type": "application/json"})
    pid = json.load(urllib.request.urlopen(req))["prompt_id"]
    t0 = time.time()
    while True:
        time.sleep(10)
        h = get_json(f"{HOST}/history/{pid}").get(pid)
        if h and h.get("status", {}).get("completed") is not None:
            break
        if h and h.get("status", {}).get("status_str") == "error":
            break
    st = h["status"]
    if st.get("status_str") != "success":
        print(json.dumps(st, indent=1)[:3000]); raise SystemExit(1)
    files = [i["filename"] for i in h["outputs"]["save"]["images"]]
    print(json.dumps({"seconds": round(time.time() - t0), "frames": len(files), "first": files[0], "last": files[-1]}))


if __name__ == "__main__":
    main()
