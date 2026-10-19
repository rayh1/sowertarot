#!/usr/bin/env python3
"""Unattended batch of card animations over one or more ComfyUI instances (§ Animate a card).

  animate_batch.py --dir <batch dir> --worker local|remote [--dropbox dropbox:Tarot/animations/batch]

<batch dir>/jobs.json is a list of {"slug", "name", "seed"}; each <batch dir>/<slug>/ holds art.png,
input_576x1024.png, mask.png, prompt.txt, optionally crop.txt (see animate_mask.py crop) and, once the mask is checked, an empty READY file;
jobs of cards without READY wait. Run one worker per instance (e.g. under setsid nohup);
workers claim jobs from <batch dir>/state.json under a file lock, so two instances share one queue.
Per job: animate_wan.py (5B, through `with-comfy <worker>`), animate_compose.py, then the MP4 is
copied to --dropbox. A job that fails is retried once (possibly by the other worker); when the
worker's instance is down (with-comfy exit 69, e.g. the remote after 07:00) the worker releases its
job and exits. Progress: <batch dir>/run.log and state.json.
"""
import argparse, fcntl, json, os, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
WITH_COMFY = "/workspace/.claude/tools/with-comfy/with-comfy"


def log(d, msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(os.path.join(d, ".lock"), "w") as lk:  # two workers append at once; the mount does not keep that atomic
        fcntl.flock(lk, fcntl.LOCK_EX)
        with open(os.path.join(d, "run.log"), "a") as f:
            f.write(line + "\n")


def update(d, fn):
    """Run fn(state, jobs) under the lock; fn returns a value passed back."""
    with open(os.path.join(d, ".lock"), "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        p = os.path.join(d, "state.json")
        state = json.load(open(p)) if os.path.exists(p) else {}
        jobs = json.load(open(os.path.join(d, "jobs.json")))
        out = fn(state, jobs)
        json.dump(state, open(p + ".tmp", "w"), indent=1)
        os.replace(p + ".tmp", p)
        return out


def job_id(j):
    return f"{j['slug']}_s{j['seed']}"


def claim(worker, d):
    def fn(state, jobs):
        waiting = False
        for j in jobs:
            s = state.get(job_id(j), {})
            if s.get("status") not in (None, "retry"):
                continue
            if not os.path.exists(os.path.join(d, j["slug"], "READY")):  # mask and prompt not checked yet
                waiting = True
                continue
            state[job_id(j)] = {"status": "running", "worker": worker, "tries": s.get("tries", 0) + 1,
                                "started": time.strftime("%H:%M:%S")}
            return j
        return "wait" if waiting else None
    return fn


def finish(jid, status, **kw):
    def fn(state, jobs):
        state[jid].update(status=status, ended=time.strftime("%H:%M:%S"), **kw)
    return fn


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)[-1500:]


def crop_arg(cd):
    p = os.path.join(cd, "crop.txt")  # the model renders only this box of the art
    return ["--crop", open(p).read().strip()] if os.path.exists(p) else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--worker", required=True)
    ap.add_argument("--dropbox", default="dropbox:Tarot/animations/batch")
    a = ap.parse_args()
    d = os.path.abspath(a.dir)
    log(d, f"[{a.worker}] start")

    def reset_stale(state, jobs):  # this worker's jobs left "running" by a killed earlier run
        for s in state.values():
            if s.get("status") == "running" and s.get("worker") == a.worker:
                s["status"] = "retry"
    update(d, reset_stale)
    while True:
        j = update(d, claim(a.worker, d))
        if j is None:
            log(d, f"[{a.worker}] queue empty, exit")
            return
        if j == "wait":  # jobs left, but their cards have no READY marker yet
            time.sleep(60)
            continue
        jid, cd = job_id(j), os.path.join(d, j["slug"])
        prefix = f"anim_{jid}"
        log(d, f"[{a.worker}] {jid} render")
        rc, out = run([WITH_COMFY, a.worker, "python3", f"{HERE}/animate_wan.py", "--model", "5b",
                       "--image", "input_576x1024.png", "--seed", str(j["seed"]), "--prefix", prefix,
                       "--prompt", open(os.path.join(cd, "prompt.txt")).read().strip()], cd)
        if rc == 0:
            rc, out = run([WITH_COMFY, a.worker, "python3", f"{HERE}/animate_compose.py", "--frames-prefix", prefix,
                           "--count", "121", "--fps", "24", "--art", "art.png", "--mask", "mask.png",
                           "--title", j["name"], "--out", jid, "--crossfade", "0.5", *crop_arg(cd)], cd)
        if rc == 0:
            rc, out = run(["rclone", "copy", f"{jid}.mp4", a.dropbox], cd)
        if rc == 0:
            update(d, finish(jid, "done"))
            log(d, f"[{a.worker}] {jid} done")
            continue
        down = rc == 69 or "exit 69" in out or "is down" in out
        def fail(state, jobs, jid=jid, out=out):
            s = state[jid]
            s["status"] = "retry" if (down or s["tries"] < 2) else "failed"
            s["error"] = out[-400:]
        update(d, fail)
        log(d, f"[{a.worker}] {jid} FAILED rc={rc}: {out[-300:]!r}")
        if down:
            log(d, f"[{a.worker}] instance down, exit")
            return
        time.sleep(30)


if __name__ == "__main__":
    main()
