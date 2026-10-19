// Small web copies made from the card PNGs: thumbnails for the overview pages and link-preview
// (Open Graph) pictures. They are new files under /thumbs/ and /og/; the reference files in
// /media/ are never re-encoded (decision 8 of the site plan).
import { readdirSync } from "node:fs";
import path from "node:path";
import sharp from "sharp";

// Twice the widest thumbnail on the deck overview (about 12rem), for sharp screens.
export const THUMB_WIDTH = 400;
export const OG_WIDTH = 1200;
export const OG_HEIGHT = 630;
const PAPER = "#efe5cc";
const INK = "#1a1612";
// The card the deck is named after stands in the middle of the deck picture.
const CENTRE = "card_the-sower.png";

// The card PNGs in the media folder, by file name.
export function cardFiles(mediaDir) {
  return readdirSync(mediaDir)
    .filter((f) => /^card_.+\.png$/.test(f))
    .sort();
}

// Every derived file: its path under the site root and how to make it.
export function derivedFiles(mediaDir) {
  const cards = cardFiles(mediaDir);
  const src = (f) => path.join(mediaDir, f);
  const out = new Map();
  for (const f of cards) {
    const base = f.replace(/\.png$/, "");
    out.set(`thumbs/${base}.webp`, () => thumb(src(f)));
    out.set(`og/${base}.jpg`, () => ogCard(src(f), false));
    out.set(`og/${base}-reversed.jpg`, () => ogCard(src(f), true));
  }
  if (cards.length) out.set("og/deck.jpg", () => ogDeck(pickFive(cards).map(src)));
  return out;
}

export function thumb(png) {
  return sharp(png).resize({ width: THUMB_WIDTH }).webp({ quality: 80 }).toBuffer();
}

// One card, whole, on the cards' paper inside the site's double rule.
export async function ogCard(png, reversed) {
  const height = OG_HEIGHT - 2 * 48;
  const card = await framedCard(png, height, reversed);
  const { width } = await sharp(card).metadata();
  return page([{ input: card, left: Math.round((OG_WIDTH - width) / 2), top: 48 }]);
}

// Five cards side by side.
export async function ogDeck(pngs) {
  const gap = 24;
  const width = Math.floor((OG_WIDTH - 2 * 60 - (pngs.length - 1) * gap) / pngs.length);
  const height = Math.round((width * 1792) / 1024);
  const cards = await Promise.all(pngs.map((p) => framedCard(p, height, false)));
  const widths = await Promise.all(cards.map(async (c) => (await sharp(c).metadata()).width));
  const total = widths.reduce((a, b) => a + b, 0) + (cards.length - 1) * gap;
  let left = Math.round((OG_WIDTH - total) / 2);
  const top = Math.round((OG_HEIGHT - height) / 2);
  return page(
    cards.map((input, i) => {
      const layer = { input, left, top };
      left += widths[i] + gap;
      return layer;
    }),
  );
}

// Five cards spread evenly through the deck, The Sower in the middle when it is there.
export function pickFive(cards) {
  if (cards.length <= 5) return cards;
  const others = cards.filter((f) => f !== CENTRE);
  const step = others.length / 4;
  const four = [0, 1, 2, 3].map((i) => others[Math.min(others.length - 1, Math.round(i * step + step / 2))]);
  const middle = cards.includes(CENTRE) ? CENTRE : others[Math.floor(others.length / 2)];
  return [four[0], four[1], middle, four[2], four[3]];
}

// The card scaled to the given height with a thin ink line round it, as on the site.
async function framedCard(png, height, reversed) {
  let img = sharp(png).resize({ height });
  if (reversed) img = img.rotate(180);
  return img.extend({ top: 1, bottom: 1, left: 1, right: 1, background: INK }).png().toBuffer();
}

function page(layers) {
  const rule = (inset, w) =>
    `<rect x="${inset}" y="${inset}" width="${OG_WIDTH - 2 * inset}" height="${OG_HEIGHT - 2 * inset}" fill="none" stroke="${INK}" stroke-width="${w}"/>`;
  const frame = Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${OG_WIDTH}" height="${OG_HEIGHT}">${rule(16, 2)}${rule(23, 1)}</svg>`);
  return sharp({ create: { width: OG_WIDTH, height: OG_HEIGHT, channels: 3, background: PAPER } })
    .composite([{ input: frame }, ...layers])
    .jpeg({ quality: 85, mozjpeg: true })
    .toBuffer();
}
