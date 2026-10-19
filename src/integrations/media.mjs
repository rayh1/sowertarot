// Serves the content folder's media/ at /media/ in dev and copies it into the build.
// The media are reference files (decision 8 of the site plan): served byte-identical, never
// re-encoded, so they stay out of Astro's image pipeline. The thumbnails and link-preview pictures
// made from them (derived.mjs) are served at /thumbs/ and /og/: made on request in dev, written
// into the build. The content folder's checksums.txt (scripts/checksums.py) is served at /checksums.txt;
// the build fails when it does not match the media exactly, so no unlisted file is ever published.
import { createHash } from "node:crypto";
import { createReadStream, cpSync, existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { derivedFiles } from "./derived.mjs";

const TYPES = { ".png": "image/png", ".mp4": "video/mp4", ".jpg": "image/jpeg", ".webp": "image/webp" };

// Differences between the media folder and its checksum list, as lines; empty when they match.
export function checksumProblems(mediaDir, listFile) {
  const have = new Map(
    readdirSync(mediaDir, { withFileTypes: true })
      .filter((e) => e.isFile())
      .map((e) => [e.name, createHash("sha256").update(readFileSync(path.join(mediaDir, e.name))).digest("hex")]),
  );
  const want = new Map();
  if (existsSync(listFile)) {
    for (const line of readFileSync(listFile, "utf8").split("\n").filter(Boolean)) {
      const [digest, name] = [line.slice(0, line.indexOf("  ")), line.slice(line.indexOf("  ") + 2)];
      want.set(name, digest);
    }
  }
  return [
    ...[...have.keys()].filter((n) => !want.has(n)).map((n) => `not listed: ${n}`),
    ...[...want.keys()].filter((n) => !have.has(n)).map((n) => `listed but missing: ${n}`),
    ...[...have].filter(([n, d]) => want.has(n) && want.get(n) !== d).map(([n]) => `changed: ${n}`),
  ];
}

export default function media(mediaDir) {
  const root = path.resolve(mediaDir);
  const checksums = path.join(path.dirname(root), "checksums.txt");
  return {
    name: "sower-media",
    hooks: {
      "astro:server:setup": ({ server }) => {
        const made = new Map();
        for (const prefix of ["/thumbs", "/og"]) {
          server.middlewares.use(prefix, async (req, res, next) => {
            const name = prefix.slice(1) + decodeURIComponent(req.url.split("?")[0]);
            const make = existsSync(root) && derivedFiles(root).get(name);
            if (!make) return next();
            try {
              if (!made.has(name)) made.set(name, await make());
            } catch (e) {
              return next(e);
            }
            res.setHeader("Content-Type", TYPES[path.extname(name)]);
            res.end(made.get(name));
          });
        }
        server.middlewares.use("/checksums.txt", (req, res, next) => {
          if (!existsSync(checksums)) return next();
          res.setHeader("Content-Type", "text/plain; charset=utf-8");
          res.end(readFileSync(checksums));
        });
        server.middlewares.use("/media", (req, res, next) => {
          const file = path.join(root, decodeURIComponent(req.url.split("?")[0]));
          if (!file.startsWith(root + path.sep) || !existsSync(file)) return next();
          const size = statSync(file).size;
          res.setHeader("Content-Type", TYPES[path.extname(file)] ?? "application/octet-stream");
          res.setHeader("Accept-Ranges", "bytes");
          // Safari plays a <video> only when the server answers byte-range requests.
          const range = /bytes=(\d*)-(\d*)/.exec(req.headers.range ?? "");
          if (range) {
            const start = range[1] ? Number(range[1]) : 0;
            const end = range[2] ? Number(range[2]) : size - 1;
            res.statusCode = 206;
            res.setHeader("Content-Range", `bytes ${start}-${end}/${size}`);
            res.setHeader("Content-Length", end - start + 1);
            createReadStream(file, { start, end }).pipe(res);
          } else {
            res.setHeader("Content-Length", size);
            createReadStream(file).pipe(res);
          }
        });
      },
      "astro:build:done": async ({ dir, logger }) => {
        if (!existsSync(root)) return;
        const problems = checksumProblems(root, checksums);
        if (problems.length) {
          throw new Error(`${checksums} does not match the media (run scripts/checksums.py write):\n${problems.join("\n")}`);
        }
        const out = fileURLToPath(dir);
        cpSync(root, path.join(out, "media"), { recursive: true });
        cpSync(checksums, path.join(out, "checksums.txt"));
        const files = derivedFiles(root);
        await Promise.all(
          [...files].map(async ([name, make]) => {
            const file = path.join(out, name);
            mkdirSync(path.dirname(file), { recursive: true });
            writeFileSync(file, await make());
          }),
        );
        logger.info(`${files.size} thumbnails and link-preview pictures written`);
      },
    },
  };
}
