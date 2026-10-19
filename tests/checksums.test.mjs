// The build's checksum check (checksumProblems in src/integrations/media.mjs) against a stand-in media folder.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { appendFileSync, mkdirSync, mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { after, beforeEach, test } from "node:test";
import { checksumProblems } from "../src/integrations/media.mjs";

let dir, media, list;
const sha = (s) => createHash("sha256").update(s).digest("hex");

beforeEach(() => {
  dir = mkdtempSync(path.join(tmpdir(), "checksums-"));
  media = path.join(dir, "media");
  list = path.join(dir, "checksums.txt");
  mkdirSync(media);
  writeFileSync(path.join(media, "card_a.png"), "a");
  writeFileSync(path.join(media, "a_v1.mp4"), "clip");
  writeFileSync(list, `${sha("clip")}  a_v1.mp4\n${sha("a")}  card_a.png\n`);
});

after(() => rmSync(dir, { recursive: true, force: true }));

test("a list that matches has no problems", () => {
  assert.deepEqual(checksumProblems(media, list), []);
});

test("a changed, an unlisted and a missing file are each reported", () => {
  appendFileSync(path.join(media, "card_a.png"), "!");
  writeFileSync(path.join(media, "card_b.png"), "b");
  appendFileSync(list, `${sha("c")}  card_c.png\n`);
  assert.deepEqual(checksumProblems(media, list).sort(), ["changed: card_a.png", "listed but missing: card_c.png", "not listed: card_b.png"]);
});

test("no list at all reports every file as not listed", () => {
  rmSync(list);
  assert.equal(checksumProblems(media, list).length, 2);
});
