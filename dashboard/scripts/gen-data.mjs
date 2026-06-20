#!/usr/bin/env node
// Generate dashboard/src/daily.json from the my-daily-news pipeline output.
//
// Emits ALL daily editions (newest first). For each item in a daily/<date>.json
// it joins projects/<owner__name>/metadata.json + analysis.md (parsed into
// ordered sections) and the project's `appearances` history (for trend charts).
//
// Re-run after each pipeline run (`pnpm gen`), then rebuild the artifact.
//
// Usage:
//   node scripts/gen-data.mjs            # all editions
//   node scripts/gen-data.mjs 2026-06-19 # only this date

import { readFileSync, writeFileSync, readdirSync, existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const DASHBOARD_DIR = resolve(SCRIPT_DIR, "..");
const REPO_ROOT = resolve(DASHBOARD_DIR, "..");
const DAILY_DIR = resolve(REPO_ROOT, "daily");
const PROJECTS_DIR = resolve(REPO_ROOT, "projects");
const OUT = resolve(DASHBOARD_DIR, "src", "daily.json");

const DATE_RE = /^(\d{4}-\d{2}-\d{2})\.json$/;

function listDates(dateArg) {
  if (dateArg) {
    if (!existsSync(resolve(DAILY_DIR, `${dateArg}.json`)))
      throw new Error(`No daily file for ${dateArg}`);
    return [dateArg];
  }
  const dates = readdirSync(DAILY_DIR)
    .map((n) => n.match(DATE_RE))
    .filter(Boolean)
    .map((m) => m[1])
    .sort()
    .reverse(); // newest first
  if (dates.length === 0) throw new Error(`No daily/*.json files in ${DAILY_DIR}`);
  return dates;
}

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

// Strip inline markdown noise (bold, code, stray markers) for clean UI text.
function clean(text) {
  return text.replace(/\*\*/g, "").replace(/`/g, "").trim();
}

// Parse an analysis.md into ordered sections of { heading, body?, bullets? }.
function parseAnalysis(md) {
  const lines = md.split(/\r?\n/);
  const sections = [];
  let cur = null;
  const flush = () => {
    if (!cur) return;
    const body = cur.bodyLines.join(" ").trim();
    const section = { heading: cur.heading };
    if (body) section.body = clean(body);
    if (cur.bullets.length) section.bullets = cur.bullets;
    sections.push(section);
  };
  for (const raw of lines) {
    const line = raw.trimEnd();
    const h = line.match(/^#{2,3}\s+(.+)$/);
    if (h) {
      flush();
      cur = { heading: clean(h[1]), bodyLines: [], bullets: [] };
      continue;
    }
    if (!cur) continue;
    const b = line.match(/^\s*[-*]\s+(.+)$/);
    if (b) {
      const t = clean(b[1]);
      if (t) cur.bullets.push(t);
    } else if (line.trim()) {
      cur.bodyLines.push(line.trim());
    }
  }
  flush();
  return sections;
}

function mapAppearances(meta) {
  const arr = Array.isArray(meta.appearances) ? meta.appearances : [];
  return arr
    .map((a) => ({
      date: a.date ?? "",
      reason: a.reason ?? "",
      starsTotal: a.stars_total ?? 0,
      starsGained: a.stars_gained ?? 0,
      release: a.release ?? "",
    }))
    .sort((x, y) => x.date.localeCompare(y.date)); // chronological for charts
}

function buildProject(item, date) {
  const dir = item.full_name.replace("/", "__");
  const metaPath = resolve(PROJECTS_DIR, dir, "metadata.json");
  const analysisPath = resolve(PROJECTS_DIR, dir, "analysis.md");
  const meta = existsSync(metaPath) ? readJson(metaPath) : {};
  const analysis = existsSync(analysisPath)
    ? parseAnalysis(readFileSync(analysisPath, "utf8"))
    : [];

  const [owner, name] = item.full_name.split("/");
  return {
    id: dir,
    fullName: item.full_name,
    owner,
    name,
    url: item.url ?? meta.url ?? `https://github.com/${item.full_name}`,
    oneLiner: item.one_liner ?? meta.one_liner ?? "",
    description: meta.description ?? "",
    language: item.language ?? meta.language ?? "",
    category: meta.category ?? "",
    license: meta.license ?? "",
    starsTotal: item.stars_total ?? meta.stars_total ?? 0,
    starsGained: item.stars_gained ?? 0,
    streakDays: item.streak_days ?? meta.streak_days ?? 0,
    isNew: Boolean(item.is_new),
    createdAt: meta.created_at ?? "",
    pushedAt: meta.pushed_at ?? "",
    latestRelease: meta.latest_release ?? "",
    firstSeen: meta.first_seen ?? date,
    topics: Array.isArray(meta.topics) ? meta.topics : [],
    appearances: mapAppearances(meta),
    analysis,
  };
}

// Map the AI-news parallel track (daily/<date>.json `news` field) into the
// dashboard shape. Absent on editions generated before the news feature.
function mapNews(dailyRaw) {
  const arr = Array.isArray(dailyRaw.news) ? dailyRaw.news : [];
  return arr.map((n) => ({
    title: n.title ?? "",
    url: n.url ?? "",
    source: n.source ?? "",
    sourceType: n.source_type ?? "",
    published: n.published ?? "",
    summary: n.summary_zh ?? "",
    category: n.category ?? "",
  }));
}

function buildEdition(date) {
  const dailyRaw = readJson(resolve(DAILY_DIR, `${date}.json`));
  const items = Array.isArray(dailyRaw.items) ? dailyRaw.items : [];
  const projects = items.map((it) => buildProject(it, date));
  return {
    date: dailyRaw.date ?? date,
    count: projects.length,
    projects,
    news: mapNews(dailyRaw),
  };
}

function main() {
  const dates = listDates(process.argv[2]);
  const editions = dates.map(buildEdition);
  const out = { editions };
  writeFileSync(OUT, JSON.stringify(out, null, 2) + "\n");
  console.log(
    `✓ wrote ${OUT}\n  ${editions.length} edition(s): ` +
      editions.map((e) => `${e.date}(${e.count})`).join(", ")
  );
}

main();
