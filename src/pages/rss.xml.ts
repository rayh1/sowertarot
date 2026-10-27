import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { cardUrl, readings, readingUrl, sownCards } from "../lib/deck";

export async function GET(context: APIContext) {
  return rss({
    title: "Sower Tarot",
    description: "One card from the Sower Tarot deck each morning, with its reading.",
    site: context.site!,
    items: [
      ...(await readings()).map((r) => ({
        title: `${r.data.card}${r.data.orientation === "reversed" ? " (reversed)" : ""}`,
        pubDate: r.data.date,
        description: r.data.lede,
        link: readingUrl(r),
      })),
      // A card grown from a trigger draw gets an item of its own.
      ...(await sownCards()).map(({ card }) => ({
        title: `New card: ${card.data.title}`,
        pubDate: card.data.created,
        description: card.data.concept,
        link: cardUrl(card),
      })),
    ].sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime()),
  });
}
