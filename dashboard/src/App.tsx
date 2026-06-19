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
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import { Sheet, SheetContent, SheetClose } from "@/components/ui/sheet";
import { ScrollArea } from "@/components/ui/scroll-area";
import { cn } from "@/lib/utils";
import { daily, type Project } from "@/data";

const LANG_COLOR: Record<string, string> = {
  Python: "#3572A5",
  Shell: "#89e051",
  TypeScript: "#3178c6",
  JavaScript: "#f1e05a",
  Go: "#00ADD8",
  Rust: "#dea584",
};

function fmt(n: number): string {
  return n.toLocaleString("en-US");
}

type SortKey = "gained" | "total" | "newest";

export default function App() {
  const [dark, setDark] = useState(false);
  const [query, setQuery] = useState("");
  const [lang, setLang] = useState<string>("全部");
  const [sort, setSort] = useState<SortKey>("gained");
  const [active, setActive] = useState<Project | null>(null);

  const languages = useMemo(() => {
    const set = new Set(daily.projects.map((p) => p.language));
    return ["全部", ...Array.from(set)];
  }, []);

  const totals = useMemo(() => {
    const stars = daily.projects.reduce((s, p) => s + p.starsTotal, 0);
    const gained = daily.projects.reduce((s, p) => s + p.starsGained, 0);
    return { stars, gained };
  }, []);

  const filtered = useMemo(() => {
    let list = daily.projects.filter((p) => {
      const matchLang = lang === "全部" || p.language === lang;
      const q = query.trim().toLowerCase();
      const matchQ =
        !q ||
        p.fullName.toLowerCase().includes(q) ||
        p.oneLiner.toLowerCase().includes(q) ||
        p.topics.some((t) => t.includes(q));
      return matchLang && matchQ;
    });
    list = [...list].sort((a, b) => {
      if (sort === "total") return b.starsTotal - a.starsTotal;
      if (sort === "newest")
        return b.firstSeen.localeCompare(a.firstSeen) || b.starsGained - a.starsGained;
      return b.starsGained - a.starsGained;
    });
    return list;
  }, [query, lang, sort]);

  return (
    <div className={cn(dark && "dark")}>
      <div className="min-h-screen bg-background text-foreground paper-grain">
        <div className="mx-auto max-w-6xl px-5 pb-24 sm:px-8">
          {/* ── Masthead ───────────────────────────────────────── */}
          <header className="border-b-2 border-foreground pt-10">
            <div className="flex items-start justify-between gap-4">
              <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.25em] text-muted-foreground">
                <span className="font-mono-num">EDITION · {daily.date}</span>
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
                今日命中 <span className="font-mono-num font-semibold">{daily.count}</span> 个项目。
              </span>
            </p>
          </header>

          {/* ── Stat strip ─────────────────────────────────────── */}
          <section className="grid grid-cols-3 divide-x divide-border border-b border-border">
            <Stat label="命中项目" value={fmt(daily.count)} icon={<Sparkles className="h-3.5 w-3.5" />} />
            <Stat
              label="今日新增 Star"
              value={`+${fmt(totals.gained)}`}
              accent
              icon={<Flame className="h-3.5 w-3.5" />}
            />
            <Stat label="累计 Star" value={fmt(totals.stars)} icon={<Star className="h-3.5 w-3.5" />} />
          </section>

          {/* ── Controls ───────────────────────────────────────── */}
          <section className="flex flex-col gap-3 py-6 md:flex-row md:items-center md:justify-between">
            <div className="relative w-full md:max-w-xs">
              <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="搜索项目、描述或标签…"
                className="h-9 w-full border border-border bg-card pl-9 pr-3 text-sm outline-none focus:border-primary focus:ring-1 focus:ring-primary"
              />
            </div>
            <div className="flex flex-wrap items-center gap-2">
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
              <select
                value={sort}
                onChange={(e) => setSort(e.target.value as SortKey)}
                className="h-8 border border-border bg-card px-2 text-xs outline-none focus:border-primary"
              >
                <option value="gained">按今日新增</option>
                <option value="total">按累计 Star</option>
                <option value="newest">按最新发现</option>
              </select>
            </div>
          </section>

          {/* ── Project list ───────────────────────────────────── */}
          <main className="divide-y divide-border border-y border-border">
            {filtered.map((p, i) => (
              <ProjectRow key={p.id} project={p} rank={i + 1} onOpen={() => setActive(p)} />
            ))}
            {filtered.length === 0 && (
              <div className="py-16 text-center text-sm text-muted-foreground">没有匹配的项目。</div>
            )}
          </main>

          <footer className="mt-10 flex items-center justify-between text-[11px] uppercase tracking-[0.2em] text-muted-foreground">
            <span>my-daily-news pipeline</span>
            <span className="font-mono-num">{daily.date}</span>
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
          <Badge
            variant="outline"
            className="h-5 rounded-sm border-border px-1.5 text-[10px] font-normal text-muted-foreground"
          >
            {p.category}
          </Badge>
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
            <span className="text-[11px] uppercase tracking-wider text-muted-foreground">
              {p.category}
            </span>
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
          <Meta icon={<Tag className="h-3.5 w-3.5" />} label="版本" value={p.latestRelease} />
          <Meta icon={<Scale className="h-3.5 w-3.5" />} label="许可" value={p.license} />
        </div>
      </div>

      {/* body */}
      <ScrollArea className="flex-1">
        <div className="px-6 py-6">
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

          <div className="mb-6 flex flex-wrap items-center gap-x-4 gap-y-1.5 text-xs text-muted-foreground">
            <span className="inline-flex items-center gap-1">
              <GitBranch className="h-3.5 w-3.5" />
              {p.language}
            </span>
            <span className="inline-flex items-center gap-1">
              <CalendarDays className="h-3.5 w-3.5" />
              创建 {p.createdAt}
            </span>
            <span className="inline-flex items-center gap-1">
              <CalendarDays className="h-3.5 w-3.5" />
              发现 {p.firstSeen}
            </span>
          </div>

          <div className="space-y-7">
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
