import { getCollection, type CollectionEntry } from "astro:content";
import { marked } from "marked";

export type Card = CollectionEntry<"cards">;
export type Reading = CollectionEntry<"readings">;

export const media = (file: string) => `/media/${file}`;
// Web copies made at build time by src/integrations/derived.mjs; the reference PNG stays as it is.
const base = (c: Card) => c.data.image.replace(/\.png$/, "");
export const thumbUrl = (c: Card) => `/thumbs/${base(c)}.webp`;
export const previewUrl = (c: Card, reversed = false) => `/og/${base(c)}${reversed ? "-reversed" : ""}.jpg`;

export async function deck(): Promise<Card[]> {
  return (await getCollection("cards")).sort((a, b) => a.data.title.localeCompare(b.data.title));
}

/** Readings, newest first. */
export async function readings(): Promise<Reading[]> {
  return (await getCollection("readings")).sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

export async function cardByTitle(title: string): Promise<Card | undefined> {
  return (await deck()).find((c) => c.data.title === title);
}

/** Cards that grew from a trigger reading (sown_by), newest trigger first, with that reading if it exists. */
export async function sownCards(): Promise<{ card: Card; trigger?: Reading }[]> {
  const all = await readings();
  return (await deck())
    .filter((c) => c.data.sown_by)
    .sort((a, b) => b.data.sown_by!.localeCompare(a.data.sown_by!))
    .map((card) => ({ card, trigger: all.find((r) => r.id === card.data.sown_by) }));
}

/** "Sown from the draw of The Sower" or "Mined from the draw of The Miner". */
export const originVerb = (trigger: Reading) => (trigger.data.card === "The Miner" ? "Mined" : "Sown");

export const readingUrl = (r: Reading) => `/readings/${r.id}/`;
export const cardUrl = (c: Card) => `/cards/${c.id}/`;

export function longDate(d: Date): string {
  return d.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
}

export function shortDate(d: Date): string {
  return d.toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric", timeZone: "UTC" });
}

/**
 * A card note's or reading's ## and ### sections, rendered to HTML, keyed by heading, in text order.
 * ### counts too: newer card notes put Composition, Symbolism and Atmosphere under "## Visual Description".
 */
export function sections(entry: Card | Reading): Record<string, string> {
  const parts = (entry.body ?? "").split(/^#{2,3} (.+)$/m);
  const out: Record<string, string> = {};
  for (let i = 1; i < parts.length; i += 2) out[parts[i].trim()] = marked.parse(parts[i + 1].trim(), { async: false });
  return out;
}
