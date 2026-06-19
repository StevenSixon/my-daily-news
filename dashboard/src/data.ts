// Data is generated from the my-daily-news pipeline output by
// scripts/gen-data.mjs (reads daily/<date>.json + projects/*/metadata.json +
// analysis.md). Regenerate with `pnpm gen`, then rebuild the artifact.
import rawDaily from "./daily.json";

export interface AnalysisSection {
  heading: string;
  body?: string;
  bullets?: string[];
}

export interface Project {
  id: string;
  fullName: string;
  owner: string;
  name: string;
  url: string;
  oneLiner: string;
  description: string;
  language: string;
  category: string;
  license: string;
  starsTotal: number;
  starsGained: number;
  streakDays: number;
  isNew: boolean;
  createdAt: string;
  pushedAt: string;
  latestRelease: string;
  firstSeen: string;
  topics: string[];
  analysis: AnalysisSection[];
}

export interface Daily {
  date: string;
  count: number;
  projects: Project[];
}

export const daily: Daily = rawDaily as Daily;
