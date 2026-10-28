import { getCollection, type CollectionEntry } from "astro:content";
import { cardUrl, deck, originVerb, readings, readingUrl, shortDate, sownCards } from "./deck";

export type Post = CollectionEntry<"news">;

export interface NewsItem {
  date: Date;
  title: string;
  summary: string;
  url: string;
  kind: "post" | "card" | "milestone";
}

/** How long the home page names the newest news item (counted from its date). */
export const NEWS_DAYS = 30;

/** The day sowertarot.com went live; its anniversaries are milestones. */
const GO_LIVE = new Date("2026-10-19");

/** The 50th and 100th reading, then every 100th. */
const isReadingMilestone = (n: number) => n === 50 || (n % 100 === 0 && n > 0);

export const postUrl = (p: Post) => `/news/${p.id}/`;

/** Hand-written posts, newest first. */
export async function posts(): Promise<Post[]> {
  return (await getCollection("news")).sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

function ordinal(n: number): string {
  const tens = n % 100;
  const suffix = tens >= 11 && tens <= 13 ? "th" : ({ 1: "st", 2: "nd", 3: "rd" } as Record<number, string>)[n % 10] ?? "th";
  return `${n}${suffix}`;
}

const sentence = (s: string) => s.charAt(0).toUpperCase() + s.slice(1) + (/[.!?]$/.test(s) ? "" : ".");

/**
 * Every news item, newest first: the hand-written posts, one item per card grown from a trigger draw,
 * and milestones counted from the repository (reading counts, the site's anniversaries).
 * Nothing is dated after `now`, so an anniversary appears with the first build on or after its day.
 */
export async function news(now = new Date()): Promise<NewsItem[]> {
  const cards = await deck();
  const allReadings = await readings();
  const cardsBy = (d: Date) => cards.filter((c) => c.data.created.getTime() <= d.getTime()).length;
  const items: NewsItem[] = [];

  for (const p of await posts()) {
    items.push({ date: p.data.date, title: p.data.title, summary: p.data.summary, url: postUrl(p), kind: "post" });
  }

  for (const { card, trigger } of await sownCards()) {
    const origin = trigger ? `${originVerb(trigger)} from the draw of ${shortDate(trigger.data.date)}; the deck` : "The deck";
    items.push({
      date: card.data.created,
      title: `New card: ${card.data.title}`,
      summary: `${sentence(card.data.concept)} ${origin} now has ${cardsBy(card.data.created)} cards.`,
      url: cardUrl(card),
      kind: "card",
    });
  }

  const oldestFirst = [...allReadings].reverse();
  oldestFirst.forEach((r, i) => {
    const n = i + 1;
    if (!isReadingMilestone(n)) return;
    items.push({
      date: r.data.date,
      title: `${n} readings`,
      summary: `The ${ordinal(n)} daily reading drew ${r.data.card}, on ${shortDate(r.data.date)}.`,
      url: readingUrl(r),
      kind: "milestone",
    });
  });

  for (let year = 1; ; year++) {
    const day = new Date(GO_LIVE);
    day.setUTCFullYear(GO_LIVE.getUTCFullYear() + year);
    if (day.getTime() > now.getTime()) break;
    const drawn = allReadings.filter((r) => r.data.date.getTime() <= day.getTime()).length;
    items.push({
      date: day,
      title: `${year === 1 ? "One year" : `${year} years`} of Sower Tarot`,
      summary: `sowertarot.com went live on ${shortDate(GO_LIVE)}. The archive now holds ${drawn} readings, and the deck has ${cardsBy(day)} cards.`,
      url: "/readings/",
      kind: "milestone",
    });
  }

  return items.filter((i) => i.date.getTime() <= now.getTime()).sort((a, b) => b.date.getTime() - a.date.getTime());
}
