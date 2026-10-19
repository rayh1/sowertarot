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

export const collections = { cards, readings };
