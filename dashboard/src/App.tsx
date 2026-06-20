import { useMemo, useState } from "react";
import {
  Star,
  Flame,
  ArrowUpRight,
  Search,
  Moon,
  Sun,
  GitBranch,
  Tag,
  Scale,
  CalendarDays,
  Sparkles,
  TrendingUp,
  Trophy,
  Newspaper,
  Rss,
  Inbox,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import { Sheet, SheetContent, SheetClose } from "@/components/ui/sheet";
import { ScrollArea } from "@/components/ui/scroll-area";
import { cn } from "@/lib/utils";
import {
  editions,
  weekly,
  type Project,
  type Appearance,
  type NewsItem,
  type TrendRow,
} from "@/data";

const LANG_COLOR: Record<string, string> = {
  Python: "#3572A5",
  Shell: "#89e051",
  TypeScript: "#3178c6",
  JavaScript: "#f1e05a",
  Go: "#00ADD8",
  Rust: "#dea584",
  C: "#555555",
  "C++": "#f34b7d",
  Java: "#b07219",
  Ruby: "#701516",
};

function fmt(n: number): string {
  return n.toLocaleString("en-US");
}

function mmdd(d: string): string {
  return d.length >= 10 ? d.slice(5) : d;
}

type SortKey = "gained" | "total" | "newest";
type ViewKey = "current" | "board" | "news" | "weekly";

const NEWS_SOURCE_META: Record<string, { label: string; cls: string }> = {
  official: { label: "官方", cls: "border-accent/50 text-accent" },
  paper: { label: "论文", cls: "border-border text-muted-foreground" },
  hf: { label: "HF", cls: "border-border text-muted-foreground" },
  community: { label: "社区", cls: "border-border text-muted-foreground" },
};

const NEWS_TYPE_FILTERS = [
  { key: "全部", label: "全部" },
  { key: "official", label: "官方" },
  { key: "paper", label: "论文" },
  { key: "hf", label: "HF" },
  { key: "community", label: "社区" },
];

function matchesNews(n: NewsItem, q: string): boolean {
  if (!q) return true;
  return (
    n.title.toLowerCase().includes(q) ||
    n.summary.toLowerCase().includes(q) ||
    n.source.toLowerCase().includes(q) ||
    n.category.toLowerCase().includes(q)
  );
}

/** Aggregate of one project across all editions, for the leaderboard. */
type BoardEntry = Project & {
  editionsCount: number;
  totalGained: number;
  maxStreak: number;
};

function matchesFilters(p: Project, q: string, lang: string, cat: string): boolean {
  const matchLang = lang === "全部" || p.language === lang;
  const matchCat = cat === "全部" || p.category === cat;
  const matchQ =
    !q ||
    p.fullName.toLowerCase().includes(q) ||
    p.oneLiner.toLowerCase().includes(q) ||
    p.topics.some((t) => t.includes(q));
  return matchLang && matchCat && matchQ;
}

export default function App() {
  const [dark, setDark] = useState(false);
  const [editionIdx, setEditionIdx] = useState(0);
  const [view, setView] = useState<ViewKey>("current");
  const [query, setQuery] = useState("");
  const [lang, setLang] = useState<string>("全部");
  const [cat, setCat] = useState<string>("全部");
  const [sort, setSort] = useState<SortKey>("gained");
  const [newsScope, setNewsScope] = useState<"current" | "all">("current");
  const [newsType, setNewsType] = useState<string>("全部");
  const [active, setActive] = useState<Project | null>(null);

  const edition = editions[editionIdx];

  // Language chips reflect the active edition; category list spans all editions
  // so the dropdown is stable when switching views/dates.
  const languages = useMemo(() => {
    const set = new Set(edition.projects.map((p) => p.language).filter(Boolean));
    return ["全部", ...Array.from(set)];
  }, [edition]);

  const categories = useMemo(() => {
    const set = new Set<string>();
    editions.forEach((e) => e.projects.forEach((p) => p.category && set.add(p.category)));
    return ["全部", ...Array.from(set)];
  }, []);

  const totals = useMemo(() => {
    const stars = edition.projects.reduce((s, p) => s + p.starsTotal, 0);
    const gained = edition.projects.reduce((s, p) => s + p.starsGained, 0);
    return { stars, gained };
  }, [edition]);

  // Cross-edition aggregation (newest edition wins for display fields).
  const board = useMemo<BoardEntry[]>(() => {
    const map = new Map<string, BoardEntry>();
    editions.forEach((e) =>
      e.projects.forEach((p) => {
        const cur = map.get(p.id);
        if (!cur) {
          map.set(p.id, {
            ...p,
            editionsCount: 1,
            totalGained: p.starsGained,
            maxStreak: p.streakDays,
          });
        } else {
          cur.editionsCount += 1;
          cur.totalGained += p.starsGained;
          cur.maxStreak = Math.max(cur.maxStreak, p.streakDays);
          cur.starsTotal = Math.max(cur.starsTotal, p.starsTotal);
        }
      })
    );
    return [...map.values()].sort(
      (a, b) => b.totalGained - a.totalGained || b.starsTotal - a.starsTotal
    );
  }, []);

  const q = query.trim().toLowerCase();

  const filtered = useMemo(() => {
    const list = edition.projects.filter((p) => matchesFilters(p, q, lang, cat));
    return [...list].sort((a, b) => {
      if (sort === "total") return b.starsTotal - a.starsTotal;
      if (sort === "newest")
        return b.firstSeen.localeCompare(a.firstSeen) || b.starsGained - a.starsGained;
      return b.starsGained - a.starsGained;
    });
  }, [edition, q, lang, cat, sort]);

  const filteredBoard = useMemo(
    () => board.filter((p) => matchesFilters(p, q, lang, cat)),
    [board, q, lang, cat]
  );

  const news = edition.news ?? [];

  // Cumulative news across all editions, newest first, deduped by URL.
  const allNews = useMemo<NewsItem[]>(() => {
    const seen = new Set<string>();
    const out: NewsItem[] = [];
    for (const e of editions) {
      for (const n of e.news ?? []) {
        if (n.url && !seen.has(n.url)) {
          seen.add(n.url);
          out.push(n);
        }
      }
    }
    return out.sort((a, b) => (b.published || "").localeCompare(a.published || ""));
  }, []);

  const newsSource = newsScope === "all" ? allNews : news;
  const filteredNews = useMemo(
    () =>
      newsSource.filter(
        (n) =>
          matchesNews(n, q) && (newsType === "全部" || n.sourceType === newsType)
      ),
    [newsSource, q, newsType]
  );

  return (
    <div className={cn(dark && "dark")}>
      <div className="min-h-screen bg-background text-foreground paper-grain">
        <div className="mx-auto max-w-6xl px-5 pb-24 sm:px-8">
          {/* ── Masthead ───────────────────────────────────────── */}
          <header className="border-b-2 border-foreground pt-10">
            <div className="flex items-start justify-between gap-4">
              <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.25em] text-muted-foreground">
                <span className="font-mono-num">EDITION</span>
                <span>·</span>
                {editions.length > 1 ? (
                  <select
                    value={editionIdx}
                    onChange={(e) => {
                      setEditionIdx(Number(e.target.value));
                      setActive(null);
                    }}
                    className="font-mono-num border border-border bg-card px-1.5 py-0.5 text-[11px] tracking-normal outline-none focus:border-primary"
                    aria-label="选择日期"
                  >
                    {editions.map((e, i) => (
                      <option key={e.date} value={i}>
                        {e.date}
                      </option>
                    ))}
                  </select>
                ) : (
                  <span className="font-mono-num">{edition.date}</span>
                )}
              </div>
              <button
                onClick={() => setDark((d) => !d)}
                className="flex h-8 w-8 items-center justify-center border border-border text-muted-foreground transition-colors hover:text-foreground"
                aria-label="切换主题"
              >
                {dark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
              </button>
            </div>
            <h1 className="font-serif-sc mt-3 text-5xl font-bold leading-none tracking-tight sm:text-6xl">
              AI 项目日报
            </h1>
            <p className="mb-5 mt-3 max-w-xl text-sm leading-relaxed text-muted-foreground">
              每日追踪 GitHub 上正在爆发的 AI 工程项目 —— Star 增量、技术栈与深度解读。
              <span className="ml-1 text-foreground">
                {edition.date} 命中 <span className="font-mono-num font-semibold">{edition.count}</span> 个项目。
              </span>
            </p>
          </header>

          {/* ── Stat strip ─────────────────────────────────────── */}
          <section className="grid grid-cols-3 divide-x divide-border border-b border-border">
            <Stat label="命中项目" value={fmt(edition.count)} icon={<Sparkles className="h-3.5 w-3.5" />} />
            <Stat
              label="今日新增 Star"
              value={`+${fmt(totals.gained)}`}
              accent
              icon={<Flame className="h-3.5 w-3.5" />}
            />
            <Stat label="累计 Star" value={fmt(totals.stars)} icon={<Star className="h-3.5 w-3.5" />} />
          </section>

          {/* ── View tabs ──────────────────────────────────────── */}
          <div className="flex items-center gap-0 border-b border-border">
            <ViewTab
              active={view === "current"}
              onClick={() => setView("current")}
              icon={<Newspaper className="h-3.5 w-3.5" />}
              label="本期榜单"
            />
            <ViewTab
              active={view === "board"}
              onClick={() => setView("board")}
              icon={<Trophy className="h-3.5 w-3.5" />}
              label={`累计排行${editions.length > 1 ? ` · ${editions.length} 期` : ""}`}
            />
            <ViewTab
              active={view === "news"}
              onClick={() => setView("news")}
              icon={<Rss className="h-3.5 w-3.5" />}
              label={`AI 资讯${news.length ? ` · ${news.length}` : ""}`}
            />
            {weekly && (
              <ViewTab
                active={view === "weekly"}
                onClick={() => setView("weekly")}
                icon={<TrendingUp className="h-3.5 w-3.5" />}
                label="周报"
              />
            )}
          </div>

          {/* ── Controls (hidden in weekly view) ───────────────── */}
          {view !== "weekly" && (
          <section className="flex flex-col gap-3 py-6 md:flex-row md:items-center md:justify-between">
            <div className="relative w-full md:max-w-xs">
              <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder={view === "news" ? "搜索资讯标题、摘要或来源…" : "搜索项目、描述或标签…"}
                className="h-9 w-full border border-border bg-card pl-9 pr-3 text-sm outline-none focus:border-primary focus:ring-1 focus:ring-primary"
              />
            </div>
            <div className="flex flex-wrap items-center gap-2">
              {view !== "news" && (
                <>
                  <div className="flex flex-wrap gap-1.5">
                    {languages.map((l) => (
                      <button
                        key={l}
                        onClick={() => setLang(l)}
                        className={cn(
                          "border px-2.5 py-1 text-xs transition-colors",
                          lang === l
                            ? "border-foreground bg-foreground text-background"
                            : "border-border text-muted-foreground hover:text-foreground"
                        )}
                      >
                        {l}
                      </button>
                    ))}
                  </div>
                  <Separator orientation="vertical" className="hidden h-6 md:block" />
                </>
              )}
              {view !== "news" && categories.length > 1 && (
                <select
                  value={cat}
                  onChange={(e) => setCat(e.target.value)}
                  className="h-8 border border-border bg-card px-2 text-xs outline-none focus:border-primary"
                  aria-label="按分类筛选"
                >
                  {categories.map((c) => (
                    <option key={c} value={c}>
                      {c === "全部" ? "全部分类" : c}
                    </option>
                  ))}
                </select>
              )}
              {view === "current" && (
                <select
                  value={sort}
                  onChange={(e) => setSort(e.target.value as SortKey)}
                  className="h-8 border border-border bg-card px-2 text-xs outline-none focus:border-primary"
                  aria-label="排序"
                >
                  <option value="gained">按今日新增</option>
                  <option value="total">按累计 Star</option>
                  <option value="newest">按最新发现</option>
                </select>
              )}
              {view === "news" && (
                <>
                  <div className="flex gap-1.5">
                    {NEWS_TYPE_FILTERS.map((t) => (
                      <button
                        key={t.key}
                        onClick={() => setNewsType(t.key)}
                        className={cn(
                          "border px-2.5 py-1 text-xs transition-colors",
                          newsType === t.key
                            ? "border-foreground bg-foreground text-background"
                            : "border-border text-muted-foreground hover:text-foreground"
                        )}
                      >
                        {t.label}
                      </button>
                    ))}
                  </div>
                  <Separator orientation="vertical" className="hidden h-6 md:block" />
                  <select
                    value={newsScope}
                    onChange={(e) => setNewsScope(e.target.value as "current" | "all")}
                    className="h-8 border border-border bg-card px-2 text-xs outline-none focus:border-primary"
                    aria-label="资讯范围"
                  >
                    <option value="current">本期</option>
                    <option value="all">近期累计</option>
                  </select>
                </>
              )}
            </div>
          </section>
          )}

          {/* ── Body: current edition list OR cross-edition leaderboard ── */}
          {view === "current" ? (
            <main className="divide-y divide-border border-y border-border">
              {edition.projects.length === 0 ? (
                <EmptyState
                  title="本期 0 命中"
                  hint="今天没有符合标准的新 AI 项目上榜。流水线明天会继续追踪。"
                />
              ) : filtered.length === 0 ? (
                <EmptyState title="没有匹配的项目" hint="试试清除搜索或筛选条件。" />
              ) : (
                filtered.map((p, i) => (
                  <ProjectRow key={p.id} project={p} rank={i + 1} onOpen={() => setActive(p)} />
                ))
              )}
            </main>
          ) : view === "board" ? (
            <main>
              {filteredBoard.length === 0 ? (
                <div className="border-y border-border">
                  <EmptyState title="暂无排行数据" hint="清除筛选，或等待更多每日数据累计。" />
                </div>
              ) : (
                <>
                  <p className="pb-3 text-xs text-muted-foreground">
                    跨 {editions.length} 期累计 · 按累计 Star 增量排序
                  </p>
                  <div className="divide-y divide-border border-y border-border">
                    {filteredBoard.map((p, i) => (
                      <BoardRow key={p.id} entry={p} rank={i + 1} onOpen={() => setActive(p)} />
                    ))}
                  </div>
                </>
              )}
            </main>
          ) : view === "news" ? (
            <main>
              {newsSource.length === 0 ? (
                <div className="border-y border-border">
                  <EmptyState
                    title={newsScope === "all" ? "暂无资讯" : "本期暂无资讯"}
                    hint="资讯轨抓取 AI 公司官方博客、arXiv、HF、Reddit 与 Hacker News；这里暂无命中条目。"
                  />
                </div>
              ) : filteredNews.length === 0 ? (
                <div className="border-y border-border">
                  <EmptyState title="没有匹配的资讯" hint="试试清除搜索或来源筛选。" />
                </div>
              ) : (
                <>
                  <p className="pb-3 text-xs text-muted-foreground">
                    {newsScope === "all"
                      ? `近期累计 ${allNews.length} 条 · 一手动态来自官方博客 / arXiv / HF / Reddit / Hacker News`
                      : `${edition.date} · 一手动态来自官方博客 / arXiv / HF / Reddit / Hacker News`}
                  </p>
                  <div className="divide-y divide-border border-y border-border">
                    {filteredNews.map((n, i) => (
                      <NewsRow key={`${n.url}-${i}`} item={n} />
                    ))}
                  </div>
                </>
              )}
            </main>
          ) : (
            <WeeklyView />
          )}

          <footer className="mt-10 flex items-center justify-between text-[11px] uppercase tracking-[0.2em] text-muted-foreground">
            <span>my-daily-news pipeline</span>
            <span className="font-mono-num">{edition.date}</span>
          </footer>
        </div>

        {/* ── Detail reader ────────────────────────────────────── */}
        <Sheet open={!!active} onOpenChange={(o) => !o && setActive(null)}>
          <SheetContent
            side="right"
            className="w-full overflow-hidden border-l-border bg-background p-0 sm:max-w-xl"
          >
            {active && <Detail project={active} />}
          </SheetContent>
        </Sheet>
      </div>
    </div>
  );
}

function ViewTab({
  active,
  onClick,
  icon,
  label,
}: {
  active: boolean;
  onClick: () => void;
  icon: React.ReactNode;
  label: string;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "-mb-px flex items-center gap-1.5 border-b-2 px-1 py-3 text-sm transition-colors",
        active
          ? "border-foreground font-semibold text-foreground"
          : "border-transparent text-muted-foreground hover:text-foreground"
      )}
    >
      {icon}
      {label}
    </button>
  );
}

function EmptyState({ title, hint }: { title: string; hint: string }) {
  return (
    <div className="flex flex-col items-center gap-2 py-16 text-center">
      <Inbox className="h-8 w-8 text-muted-foreground/40" />
      <p className="font-serif-sc text-lg font-semibold">{title}</p>
      <p className="max-w-xs text-sm text-muted-foreground">{hint}</p>
    </div>
  );
}

function Stat({
  label,
  value,
  icon,
  accent,
}: {
  label: string;
  value: string;
  icon: React.ReactNode;
  accent?: boolean;
}) {
  return (
    <div className="px-2 py-5 first:pl-0 sm:px-5">
      <div className="flex items-center gap-1.5 text-[11px] uppercase tracking-wider text-muted-foreground">
        {icon}
        {label}
      </div>
      <div
        className={cn(
          "font-mono-num mt-1.5 text-2xl font-semibold tabular-nums sm:text-3xl",
          accent && "text-accent"
        )}
      >
        {value}
      </div>
    </div>
  );
}

function LangDot({ language }: { language: string }) {
  return (
    <span className="inline-flex items-center gap-1.5 text-xs text-muted-foreground">
      <span
        className="inline-block h-2.5 w-2.5 rounded-full"
        style={{ backgroundColor: LANG_COLOR[language] ?? "#9ca3af" }}
      />
      {language}
    </span>
  );
}

function ProjectRow({
  project: p,
  rank,
  onOpen,
}: {
  project: Project;
  rank: number;
  onOpen: () => void;
}) {
  return (
    <article
      onClick={onOpen}
      className="group grid cursor-pointer grid-cols-[auto_1fr_auto] gap-x-4 gap-y-2 py-6 transition-colors hover:bg-card sm:gap-x-6"
    >
      <div className="font-serif-sc pt-0.5 text-3xl font-bold leading-none text-muted-foreground/40 sm:pl-1">
        {String(rank).padStart(2, "0")}
      </div>

      <div className="min-w-0">
        <div className="flex flex-wrap items-center gap-2">
          <h2 className="font-serif-sc truncate text-xl font-semibold leading-tight group-hover:text-primary">
            {p.owner}/<span className="text-foreground">{p.name}</span>
          </h2>
          {p.isNew && (
            <Badge className="h-5 rounded-sm bg-accent px-1.5 text-[10px] font-bold uppercase tracking-wide text-accent-foreground hover:bg-accent">
              New
            </Badge>
          )}
          {p.streakDays > 1 && (
            <Badge
              variant="outline"
              className="h-5 rounded-sm border-border px-1.5 text-[10px] font-normal text-muted-foreground"
            >
              连榜 {p.streakDays} 天
            </Badge>
          )}
          {p.category && (
            <Badge
              variant="outline"
              className="h-5 rounded-sm border-border px-1.5 text-[10px] font-normal text-muted-foreground"
            >
              {p.category}
            </Badge>
          )}
        </div>

        <p className="mt-1.5 text-sm leading-relaxed text-foreground/80">{p.oneLiner}</p>

        <div className="mt-3 flex flex-wrap items-center gap-x-4 gap-y-1.5">
          <LangDot language={p.language} />
          <span className="font-mono-num inline-flex items-center gap-1 text-xs text-muted-foreground">
            <Star className="h-3.5 w-3.5" />
            {fmt(p.starsTotal)}
          </span>
          <span className="font-mono-num inline-flex items-center gap-1 text-xs font-semibold text-accent">
            <Flame className="h-3.5 w-3.5" />+{fmt(p.starsGained)}
          </span>
          <span className="hidden flex-wrap gap-1 sm:flex">
            {p.topics.slice(0, 3).map((t) => (
              <span key={t} className="text-[11px] text-muted-foreground/70">
                #{t}
              </span>
            ))}
          </span>
        </div>
      </div>

      <div className="hidden items-center self-center text-muted-foreground transition-colors group-hover:text-primary sm:flex">
        <ArrowUpRight className="h-5 w-5" />
      </div>
    </article>
  );
}

/** AI-news row — links out to the source article (opens in a new tab). */
function NewsRow({ item: n }: { item: NewsItem }) {
  const meta = NEWS_SOURCE_META[n.sourceType] ?? {
    label: n.sourceType || "其他",
    cls: "border-border text-muted-foreground",
  };
  return (
    <a
      href={n.url}
      target="_blank"
      rel="noopener noreferrer"
      className="group grid cursor-pointer grid-cols-[1fr_auto] items-start gap-x-4 py-4 transition-colors hover:bg-card"
    >
      <div className="min-w-0">
        <div className="mb-1 flex flex-wrap items-center gap-2">
          <Badge
            variant="outline"
            className={cn("h-5 rounded-sm px-1.5 text-[10px] font-medium", meta.cls)}
          >
            {meta.label}
          </Badge>
          {n.category && (
            <Badge
              variant="outline"
              className="h-5 rounded-sm border-border px-1.5 text-[10px] font-normal text-muted-foreground"
            >
              {n.category}
            </Badge>
          )}
        </div>
        <h2 className="text-sm font-medium leading-snug text-foreground/90 group-hover:text-primary">
          {n.summary || n.title}
        </h2>
        {n.summary && (
          <p className="mt-1 truncate text-xs text-muted-foreground/80">{n.title}</p>
        )}
        <div className="mt-1.5 flex flex-wrap items-center gap-x-3 text-[11px] text-muted-foreground">
          {n.source && <span>{n.source}</span>}
          {n.published && <span className="font-mono-num">{n.published}</span>}
        </div>
      </div>
      <div className="hidden items-center self-center text-muted-foreground transition-colors group-hover:text-primary sm:flex">
        <ArrowUpRight className="h-5 w-5" />
      </div>
    </a>
  );
}

/** Weekly view — project trend (hottest/rising/newcomers) + news digest. */
function WeeklyView() {
  if (!weekly) {
    return (
      <main className="border-y border-border">
        <EmptyState title="暂无周报" hint="周报告由每周定时任务生成，累积一周数据后呈现。" />
      </main>
    );
  }
  const p = weekly.project;
  const n = weekly.news;
  return (
    <main className="space-y-10 pt-2">
      {p && (
        <section>
          <h2 className="font-serif-sc mb-1 text-2xl font-bold">📈 项目周趋势</h2>
          <p className="mb-4 text-xs text-muted-foreground">
            截至 {p.date} · 近 {p.windowDays} 天上榜 {p.total} 个项目
          </p>
          <WeeklyTrendBlock title="🔥 本周最热" rows={p.hottest} kind="hottest" />
          <WeeklyTrendBlock title="📌 持续上榜" rows={p.rising} kind="rising" />
          <WeeklyTrendBlock title="🆕 本周新晋" rows={p.newcomers} kind="newcomer" />
        </section>
      )}
      {n && (
        <section>
          <h2 className="font-serif-sc mb-1 text-2xl font-bold">📰 资讯周回顾</h2>
          <p className="mb-4 text-xs text-muted-foreground">
            截至 {n.date} · 近 {n.windowDays} 天收录 {n.total} 条资讯
          </p>
          {Object.entries(n.byCategory).map(([cat, items]) => (
            <div key={cat} className="mb-5">
              <h3 className="mb-1 text-sm font-semibold text-muted-foreground">
                {cat}（{items.length}）
              </h3>
              <div className="divide-y divide-border border-y border-border">
                {items.map((it, i) => (
                  <NewsRow key={`${it.url}-${i}`} item={it} />
                ))}
              </div>
            </div>
          ))}
        </section>
      )}
    </main>
  );
}

function WeeklyTrendBlock({
  title,
  rows,
  kind,
}: {
  title: string;
  rows: TrendRow[];
  kind: "hottest" | "rising" | "newcomer";
}) {
  return (
    <div className="mb-5">
      <h3 className="mb-1 text-sm font-semibold text-muted-foreground">{title}</h3>
      {rows.length === 0 ? (
        <p className="py-3 text-sm text-muted-foreground/70">本期无</p>
      ) : (
        <div className="divide-y divide-border border-y border-border">
          {rows.map((r, i) => (
            <a
              key={r.fullName}
              href={r.url}
              target="_blank"
              rel="noopener noreferrer"
              className="group flex items-center gap-3 py-3 transition-colors hover:bg-card"
            >
              <span className="font-serif-sc w-6 text-center text-lg font-bold text-muted-foreground/40">
                {i + 1}
              </span>
              <div className="min-w-0 flex-1">
                <div className="truncate text-sm font-medium group-hover:text-primary">
                  {r.fullName}
                </div>
                {r.oneLiner && (
                  <div className="truncate text-xs text-muted-foreground/80">{r.oneLiner}</div>
                )}
              </div>
              <div className="font-mono-num shrink-0 text-right text-xs">
                <span className="font-semibold text-accent">+{fmt(r.weeklyGain)}⭐</span>
                <span className="ml-2 text-muted-foreground">
                  {kind === "rising"
                    ? `${r.appearDays} 天`
                    : kind === "newcomer"
                    ? r.firstSeen
                    : fmt(r.starsTotal)}
                </span>
              </div>
            </a>
          ))}
        </div>
      )}
    </div>
  );
}

/** Leaderboard row — compact, emphasises cumulative gain + streak. */
function BoardRow({
  entry: p,
  rank,
  onOpen,
}: {
  entry: BoardEntry;
  rank: number;
  onOpen: () => void;
}) {
  const medal = rank <= 3;
  return (
    <article
      onClick={onOpen}
      className="group grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-x-4 py-4 transition-colors hover:bg-card sm:gap-x-6"
    >
      <div
        className={cn(
          "font-serif-sc w-8 text-center text-2xl font-bold leading-none",
          medal ? "text-accent" : "text-muted-foreground/40"
        )}
      >
        {rank}
      </div>

      <div className="min-w-0">
        <div className="flex flex-wrap items-center gap-2">
          <h2 className="font-serif-sc truncate text-base font-semibold leading-tight group-hover:text-primary">
            {p.owner}/<span className="text-foreground">{p.name}</span>
          </h2>
          {p.maxStreak > 1 && (
            <Badge
              variant="outline"
              className="h-5 rounded-sm border-border px-1.5 text-[10px] font-normal text-muted-foreground"
            >
              连榜 {p.maxStreak} 天
            </Badge>
          )}
          <span className="text-[11px] text-muted-foreground/70">上榜 {p.editionsCount} 期</span>
        </div>
        <div className="mt-1 flex flex-wrap items-center gap-x-3 gap-y-1">
          <LangDot language={p.language} />
          {p.category && (
            <span className="text-[11px] text-muted-foreground/70">{p.category}</span>
          )}
        </div>
      </div>

      <div className="text-right">
        <div className="font-mono-num inline-flex items-center gap-1 text-sm font-semibold text-accent">
          <Flame className="h-3.5 w-3.5" />+{fmt(p.totalGained)}
        </div>
        <div className="font-mono-num mt-0.5 flex items-center justify-end gap-1 text-[11px] text-muted-foreground">
          <Star className="h-3 w-3" />
          {fmt(p.starsTotal)}
        </div>
      </div>
    </article>
  );
}

/** Compact star-gain trend across the project's appearances. */
function Trend({ appearances }: { appearances: Appearance[] }) {
  if (!appearances.length) return null;

  const W = 480;
  const H = 96;
  const padX = 8;
  const padTop = 16;
  const padBottom = 22;
  const chartH = H - padTop - padBottom;
  const maxGain = Math.max(...appearances.map((a) => a.starsGained), 1);
  const n = appearances.length;
  const slot = (W - padX * 2) / n;
  const barW = Math.min(slot * 0.5, 36);

  return (
    <section>
      <h3 className="font-serif-sc flex items-center gap-2 text-base font-semibold">
        <span className="inline-block h-3 w-1 bg-primary" />
        上榜走势
        <span className="font-mono-num text-xs font-normal text-muted-foreground">
          · 共 {n} 次
        </span>
      </h3>
      <div className="mt-3 w-full overflow-hidden rounded-sm border border-border bg-card/60 p-2">
        <svg viewBox={`0 0 ${W} ${H}`} className="h-24 w-full" preserveAspectRatio="none">
          {appearances.map((a, i) => {
            const h = Math.max((a.starsGained / maxGain) * chartH, 2);
            const x = padX + slot * i + (slot - barW) / 2;
            const y = padTop + (chartH - h);
            return (
              <g key={a.date + i}>
                <rect x={x} y={y} width={barW} height={h} rx={2} className="fill-accent" />
                <text
                  x={x + barW / 2}
                  y={y - 4}
                  textAnchor="middle"
                  className="fill-foreground"
                  style={{ fontSize: 11, fontFamily: "IBM Plex Mono, monospace" }}
                >
                  +{fmt(a.starsGained)}
                </text>
                <text
                  x={x + barW / 2}
                  y={H - 7}
                  textAnchor="middle"
                  className="fill-muted-foreground"
                  style={{ fontSize: 10, fontFamily: "IBM Plex Mono, monospace" }}
                >
                  {mmdd(a.date)}
                </text>
              </g>
            );
          })}
        </svg>
      </div>
      <p className="mt-2 flex items-center gap-1 text-xs text-muted-foreground">
        <TrendingUp className="h-3.5 w-3.5" />
        每次上榜的当日 Star 增量
      </p>
    </section>
  );
}

function Detail({ project: p }: { project: Project }) {
  return (
    <div className="flex h-full flex-col">
      {/* header */}
      <div className="border-b-2 border-foreground px-6 pb-5 pt-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            {p.isNew && (
              <Badge className="h-5 rounded-sm bg-accent px-1.5 text-[10px] font-bold uppercase text-accent-foreground hover:bg-accent">
                New
              </Badge>
            )}
            {p.category && (
              <span className="text-[11px] uppercase tracking-wider text-muted-foreground">
                {p.category}
              </span>
            )}
          </div>
          <SheetClose className="text-xs uppercase tracking-wider text-muted-foreground hover:text-foreground">
            关闭 ✕
          </SheetClose>
        </div>
        <h2 className="font-serif-sc mt-2 text-2xl font-bold leading-tight">
          {p.owner}/{p.name}
        </h2>
        <p className="mt-1.5 text-sm leading-relaxed text-foreground/80">{p.oneLiner}</p>

        <a
          href={p.url}
          target="_blank"
          rel="noreferrer"
          className="mt-3 inline-flex items-center gap-1 text-xs font-medium text-primary hover:underline"
        >
          {p.url.replace("https://", "")}
          <ArrowUpRight className="h-3.5 w-3.5" />
        </a>

        <div className="mt-4 grid grid-cols-2 gap-x-4 gap-y-2 text-xs sm:grid-cols-4">
          <Meta icon={<Star className="h-3.5 w-3.5" />} label="累计" value={fmt(p.starsTotal)} />
          <Meta
            icon={<Flame className="h-3.5 w-3.5" />}
            label="今日"
            value={`+${fmt(p.starsGained)}`}
            accent
          />
          <Meta icon={<Tag className="h-3.5 w-3.5" />} label="版本" value={p.latestRelease || "—"} />
          <Meta icon={<Scale className="h-3.5 w-3.5" />} label="许可" value={p.license || "—"} />
        </div>
      </div>

      {/* body */}
      <ScrollArea className="flex-1">
        <div className="px-6 py-6">
          {p.topics.length > 0 && (
            <div className="mb-6 flex flex-wrap gap-1.5">
              {p.topics.map((t) => (
                <span
                  key={t}
                  className="rounded-sm bg-secondary px-1.5 py-0.5 text-[11px] text-secondary-foreground"
                >
                  #{t}
                </span>
              ))}
            </div>
          )}

          <div className="mb-6 flex flex-wrap items-center gap-x-4 gap-y-1.5 text-xs text-muted-foreground">
            {p.language && (
              <span className="inline-flex items-center gap-1">
                <GitBranch className="h-3.5 w-3.5" />
                {p.language}
              </span>
            )}
            {p.createdAt && (
              <span className="inline-flex items-center gap-1">
                <CalendarDays className="h-3.5 w-3.5" />
                创建 {p.createdAt}
              </span>
            )}
            {p.firstSeen && (
              <span className="inline-flex items-center gap-1">
                <CalendarDays className="h-3.5 w-3.5" />
                首次上榜 {p.firstSeen}
              </span>
            )}
          </div>

          <div className="space-y-7">
            <Trend appearances={p.appearances} />
            {p.analysis.map((sec) => (
              <section key={sec.heading}>
                <h3 className="font-serif-sc flex items-center gap-2 text-base font-semibold">
                  <span className="inline-block h-3 w-1 bg-primary" />
                  {sec.heading}
                </h3>
                {sec.body && (
                  <p className="mt-2 text-sm leading-7 text-foreground/85">{sec.body}</p>
                )}
                {sec.bullets && (
                  <ul className="mt-2 space-y-1.5">
                    {sec.bullets.map((b, idx) => (
                      <li key={idx} className="flex gap-2 text-sm leading-6 text-foreground/85">
                        <span className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-accent" />
                        <span>{b}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </section>
            ))}
          </div>
        </div>
      </ScrollArea>
    </div>
  );
}

function Meta({
  icon,
  label,
  value,
  accent,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  accent?: boolean;
}) {
  return (
    <div>
      <div className="flex items-center gap-1 text-[10px] uppercase tracking-wider text-muted-foreground">
        {icon}
        {label}
      </div>
      <div
        className={cn("font-mono-num mt-0.5 truncate text-sm font-semibold", accent && "text-accent")}
      >
        {value}
      </div>
    </div>
  );
}
