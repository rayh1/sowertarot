// Thumbnails and link-preview pictures (src/integrations/derived.mjs), made from stand-in card PNGs.
import assert from "node:assert/strict";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { after, before, test } from "node:test";
import sharp from "sharp";
import { derivedFiles, OG_HEIGHT, OG_WIDTH, pickFive, THUMB_WIDTH } from "../src/integrations/derived.mjs";

let dir;
const names = ["the-anchor", "the-root", "the-sower", "the-tide", "the-veil", "the-well", "the-ember"].map((s) => `card_${s}.png`);

before(async () => {
  dir = mkdtempSync(path.join(tmpdir(), "derived-"));
  // Top half red, bottom half blue, so a reversed picture can be told apart.
  const half = (r, g, b) => sharp({ create: { width: 1024, height: 896, channels: 3, background: { r, g, b } } }).png().toBuffer();
  const top = await half(200, 0, 0);
  const bottom = await half(0, 0, 200);
  const png = await sharp({ create: { width: 1024, height: 1792, channels: 3, background: "#fff" } })
    .composite([{ input: top, top: 0, left: 0 }, { input: bottom, top: 896, left: 0 }])
    .png()
    .toBuffer();
  for (const n of names) writeFileSync(path.join(dir, n), png);
  writeFileSync(path.join(dir, "card_the-root.mp4"), "not a card picture");
});

after(() => rmSync(dir, { recursive: true, force: true }));

test("one thumbnail and two previews per card PNG, plus the deck picture", () => {
  const files = [...derivedFiles(dir).keys()];
  assert.equal(files.length, names.length * 3 + 1);
  assert.ok(files.includes("thumbs/card_the-root.webp"));
  assert.ok(files.includes("og/card_the-root.jpg"));
  assert.ok(files.includes("og/card_the-root-reversed.jpg"));
  assert.ok(files.includes("og/deck.jpg"));
});

test("thumbnail is a WebP of the thumbnail width, card proportions kept", async () => {
  const m = await sharp(await derivedFiles(dir).get("thumbs/card_the-root.webp")()).metadata();
  assert.deepEqual([m.format, m.width, m.height], ["webp", THUMB_WIDTH, 700]);
});

test("previews are 1200×630 JPEGs; the reversed one is upside down", async () => {
  const files = derivedFiles(dir);
  const colour = async (name, y) => {
    const { data } = await sharp(await files.get(name)())
      .extract({ left: OG_WIDTH / 2, top: y, width: 1, height: 1 })
      .raw()
      .toBuffer({ resolveWithObject: true });
    return data[0] > data[2] ? "red" : "blue";
  };
  for (const name of ["og/card_the-root.jpg", "og/card_the-root-reversed.jpg", "og/deck.jpg"]) {
    const m = await sharp(await files.get(name)()).metadata();
    assert.deepEqual([m.format, m.width, m.height], ["jpeg", OG_WIDTH, OG_HEIGHT], name);
  }
  assert.equal(await colour("og/card_the-root.jpg", 100), "red");
  assert.equal(await colour("og/card_the-root-reversed.jpg", 100), "blue");
});

test("deck picture: five different cards, The Sower in the middle", () => {
  const five = pickFive([...names].sort());
  assert.equal(five.length, 5);
  assert.equal(new Set(five).size, 5);
  assert.equal(five[2], "card_the-sower.png");
  assert.deepEqual(pickFive(names.slice(0, 3)), names.slice(0, 3));
});
