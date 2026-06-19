import path from "path";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { viteSingleFile } from "vite-plugin-singlefile";

// `vite build` emits a single self-contained dist/index.html (all JS/CSS/assets
// inlined) — that file IS the dashboard artifact published to GitHub Pages.
// CI builds it fresh from source on every push; it is no longer committed.
export default defineConfig({
  plugins: [react(), viteSingleFile()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
