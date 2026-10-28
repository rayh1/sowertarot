import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const content = process.env.SOWER_CONTENT ?? "content";

const cards = defineCollection({
  loader: glob({ pattern: "*.md", base: `${content}/cards` }),
  schema: z.object({
    title: z.string(),
    concept: z.string(),
    key_terms: z.array(z.string()),
    created: z.coerce.date(),
    image: z.string(),
    clip: z.string().optional(),
    // The trigger reading (its date) this card grew from: The Sower or The Miner drawn as the day's card.
    sown_by: z.string().optional(),
  }),
});

const readings = defineCollection({
  loader: glob({ pattern: "*.md", base: `${content}/readings` }),
  schema: z.object({
    date: z.coerce.date(),
    card: z.string(),
    orientation: z.enum(["upright", "reversed"]),
    lens: z.string(),
    lead: z.string(),
    drand: z.coerce.string(),
    lede: z.string(),
    alt: z.string(),
  }),
});

// Hand-written news posts, content/news/<date>-<slug>.md. New cards and milestones are added by src/lib/news.ts.
const news = defineCollection({
  loader: glob({ pattern: "*.md", base: `${content}/news` }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),
  }),
});

export const collections = { cards, readings, news };
