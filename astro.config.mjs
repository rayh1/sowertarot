import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";
import media from "./src/integrations/media.mjs";

// Where cards, readings and media live: content/ (the card and daily-reading skills write it). SOWER_CONTENT
// points elsewhere, e.g. for a test copy.
const content = process.env.SOWER_CONTENT ?? "content";

// https://astro.build/config
export default defineConfig({
  site: "https://sowertarot.com",
  devToolbar: { enabled: false },
  integrations: [sitemap(), media(`${content}/media`)],
  vite: {
    plugins: [tailwindcss()],
  },
  // The devcontainer forwards port 3000 for Node (.devcontainer/compose.yaml).
  server: {
    host: true,
    port: 3000,
  },
});
