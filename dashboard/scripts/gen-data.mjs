#!/usr/bin/env node
// Generate dashboard/src/daily.json from the my-daily-news pipeline output.
//
// Reads the latest (or a given) daily/<date>.json, then for each item joins
// projects/<owner__name>/metadata.json + analysis.md into the dashboard's
// Project shape. Re-run after each pipeline run, then rebuild the artifact.
//
// Usage:
//   node scripts/gen-data.mjs            # latest daily file
//   node scripts/gen-data.mjs 2026-06-19 # a specific date

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

function pickDailyFile(dateArg) {
  if (dateArg) {
    const f = resolve(DAILY_DIR, `${dateArg}.json`);
    if (!existsSync(f)) throw new Error(`No daily file for ${dateArg}: ${f}`);
    return { date: dateArg, file: f };
  }
  const dates = readdirSync(DAILY_DIR)
    .map((n) => n.match(DATE_RE))
    .filter(Boolean)
    .map((m) => m[1])
    .sort();
  if (dates.length === 0) throw new Error(`No daily/*.json files in ${DAILY_DIR}`);
  const date = dates[dates.length - 1];
  return { date, file: resolve(DAILY_DIR, `${date}.json`) };
}

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

// Strip inline markdown noise (bold, code, stray markers) for clean UI text.
function clean(text) {
  return text
    .replace(/\*\*/g, "")
    .replace(/`/g, "")
    .replace(/\s+$/g, "")
    .trim();
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
    analysis,
  };
}

function main() {
  const { date, file } = pickDailyFile(process.argv[2]);
  const dailyRaw = readJson(file);
  const items = Array.isArray(dailyRaw.items) ? dailyRaw.items : [];
  const projects = items.map((it) => buildProject(it, date));
  const out = { date: dailyRaw.date ?? date, count: projects.length, projects };
  writeFileSync(OUT, JSON.stringify(out, null, 2) + "\n");
  console.log(
    `✓ wrote ${OUT}\n  date=${out.date} projects=${out.count} ` +
      `(${projects.map((p) => p.fullName).join(", ") || "none"})`
  );
}

main();
