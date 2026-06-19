// Data is generated from the my-daily-news pipeline output by
// scripts/gen-data.mjs (reads daily/<date>.json + projects/*/metadata.json +
// analysis.md). Regenerate with `pnpm gen`, then rebuild the artifact.
import rawDaily from "./daily.json";

export interface AnalysisSection {
  heading: string;
  body?: string;
  bullets?: string[];
}

export interface Appearance {
  date: string;
  reason: string;
  starsTotal: number;
  starsGained: number;
  release: string;
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
  appearances: Appearance[];
  analysis: AnalysisSection[];
}

export interface Edition {
  date: string;
  count: number;
  projects: Project[];
}

const data = rawDaily as { editions: Edition[] };

/** All daily editions, newest first. */
export const editions: Edition[] = data.editions;

/** The most recent edition (convenience). */
export const daily: Edition = editions[0];
