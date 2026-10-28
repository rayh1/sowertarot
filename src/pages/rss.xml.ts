import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { readings, readingUrl } from "../lib/deck";
import { news } from "../lib/news";

export async function GET(context: APIContext) {
  return rss({
    title: "Sower Tarot",
    description: "One card from the Sower Tarot deck each morning, with its reading, and news of the deck.",
    site: context.site!,
    items: [
      ...(await readings()).map((r) => ({
        title: `${r.data.card}${r.data.orientation === "reversed" ? " (reversed)" : ""}`,
        pubDate: r.data.date,
        description: r.data.lede,
        link: readingUrl(r),
      })),
      // News: hand-written posts, new cards grown from trigger draws, milestones.
      ...(await news()).map((item) => ({
        title: item.title,
        pubDate: item.date,
        description: item.summary,
        link: item.url,
      })),
    ].sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime()),
  });
}
