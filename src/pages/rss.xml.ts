import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { readings, readingUrl } from "../lib/deck";

export async function GET(context: APIContext) {
  return rss({
    title: "Sower Tarot",
    description: "One card from the Sower Tarot deck each morning, with its reading.",
    site: context.site!,
    items: (await readings()).map((r) => ({
      title: `${r.data.card}${r.data.orientation === "reversed" ? " (reversed)" : ""}`,
      pubDate: r.data.date,
      description: r.data.lede,
      link: readingUrl(r),
    })),
  });
}
