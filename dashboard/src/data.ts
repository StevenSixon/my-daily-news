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

export interface NewsItem {
  title: string;
  url: string;
  source: string;
  /** official | paper | hf | community */
  sourceType: string;
  published: string;
  /** LLM-generated one-line Chinese summary (may be empty). */
  summary: string;
  category: string;
}

export interface Edition {
  date: string;
  count: number;
  projects: Project[];
  /** AI-news parallel track; absent on pre-feature editions. */
  news?: NewsItem[];
}

export interface TrendRow {
  fullName: string;
  url: string;
  oneLiner: string;
  language: string;
  starsTotal: number;
  weeklyGain: number;
  appearDays: number;
  streakDays: number;
  firstSeen: string;
  isNewcomer: boolean;
}

export interface ProjectWeekly {
  date: string;
  windowDays: number;
  total: number;
  hottest: TrendRow[];
  rising: TrendRow[];
  newcomers: TrendRow[];
}

export interface NewsWeekly {
  date: string;
  windowDays: number;
  total: number;
  byCategory: Record<string, NewsItem[]>;
  sourceCounts: Record<string, number>;
}

export interface Weekly {
  project?: ProjectWeekly;
  news?: NewsWeekly;
}

const data = rawDaily as { editions: Edition[]; weekly?: Weekly | null };

/** All daily editions, newest first. */
export const editions: Edition[] = data.editions;

/** The most recent edition (convenience). */
export const daily: Edition = editions[0];

/** Latest weekly reports (project trend + news digest), or null if none yet. */
export const weekly: Weekly | null = data.weekly ?? null;
