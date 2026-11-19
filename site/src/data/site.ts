// Everything on aeo-seo-skills.com that is specific to this site lives here.
// The components are shared with content-creation-skills.com; only this file,
// src/styles/tokens.css and public/ differ between the two.

export type Status = "available" | "building" | "soon";

export interface Skill {
  slug: string;
  blurb: string;
  status: Status;
  /** false for skills that don't have a folder in the repo yet */
  hasFolder?: boolean;
}

export interface SkillGroup {
  name: string;
  note?: string;
  skills: Skill[];
}

const repo = "https://github.com/kingscrosslabs/aeo-seo-skills";

export const site = {
  name: "AEO-SEO Skills",
  wordmark: "aeo-seo-skills",
  url: "https://aeo-seo-skills.com",
  repo,
  skillsPath: `${repo}/tree/main/skills`,
  install: "npx skills add kingscrosslabs/aeo-seo-skills",
  title: "AEO and SEO skills for AI agents | AEO-SEO Skills",
  description:
    "Open-source agent skills that get your site found in Google and quoted by ChatGPT, Perplexity and Google AI Overviews. Works in Claude Code, Codex and Cursor.",

  hero: {
    eyebrow: "Open source · MIT · By King's Cross Labs",
    headline: "AEO and SEO skills",
    highlight: "for AI agents",
    sub: "Skills that get your site found in Google and quoted by ChatGPT, Perplexity and Google AI Overviews. Built on real search data. You approve every brief and every page before it ships.",
  },

  what: {
    heading: "What are AEO-SEO skills?",
    body: [
      "A skill is a folder with a <code>SKILL.md</code> file that teaches your AI agent one job, step by step. Install it once and your agent knows when to use it.",
      "These skills treat SEO and AEO (answer engine optimization) as one job. The same page has to rank in Google and still make sense when ChatGPT lifts one paragraph out of it. So every page is written answer-first, backed by real search data, sourced facts and quotes from real people.",
    ],
    steps: [
      {
        title: "Install the skills",
        body: "One command adds them to Claude Code, Codex, Cursor or any agent that reads <code>SKILL.md</code>. Then connect OpenSEO for search data.",
      },
      {
        title: "Build your site profile",
        body: "<code>aeo-seo-setup</code> reads your repo and live site, asks you the rest, and writes an <code>aeo-seo/</code> folder: your domain, product, competitors and decisions.",
      },
      {
        title: "Ask for the work",
        body: "“Audit my site.” “Write a comparison page for us vs. X.” Your agent picks the right skill, does the research and stops for your approval.",
      },
    ],
  },

  skillsSection: {
    heading: "Popular AEO-SEO skills",
    sub: "Ten skills across three jobs: fix the site, write the pages, earn the links. They hand off to each other, and every one reads your site profile first.",
  },

  groups: [
    {
      name: "Site-wide",
      skills: [
        {
          slug: "aeo-seo-setup",
          blurb: "Builds your aeo-seo/ site profile by reading your repo and live site, interviewing you for the rest, and connecting OpenSEO.",
          status: "building",
        },
        {
          slug: "aeo-seo-technical-audit",
          blurb: "Audits your live site against 26 foundation checks, gives you a graded report, fixes what you pick and re-audits to prove it stuck.",
          status: "building",
        },
        {
          slug: "aeo-seo-weekly",
          blurb: "A weekly routine: reads Search Console, checks indexing, proposes the week's queries and lists the pages to update.",
          status: "soon",
        },
      ],
    },
    {
      name: "Pages",
      skills: [
        {
          slug: "topic-plan",
          blurb: "Proposes a cluster of 8 to 12 pages from real search data, scored, ordered and linked into the pages you already have.",
          status: "building",
        },
        {
          slug: "blog-post",
          blurb: "Researches, briefs, drafts and ships one post, with your approval before drafting and before publishing. Also updates old posts.",
          status: "building",
        },
        {
          slug: "comparison-page",
          blurb: "An “X alternative” or “you vs. X” page with sourced, dated facts about the competitor.",
          status: "building",
        },
        {
          slug: "feature-page",
          blurb: "A page for one integration or capability, using only facts your code or docs back up.",
          status: "building",
        },
        {
          slug: "use-case-page",
          blurb: "A page for one kind of customer, in their words, grounded in real customer evidence.",
          status: "building",
        },
      ],
    },
    {
      name: "Off-site",
      skills: [
        {
          slug: "forum-replies",
          blurb: "Drafts helpful replies to the Reddit and forum threads where people ask about your topic.",
          status: "soon",
          hasFolder: false,
        },
        {
          slug: "link-pitches",
          blurb: "Finds the lists and directories your buyers read and drafts the pitch to get on them.",
          status: "soon",
          hasFolder: false,
        },
      ],
    },
  ] satisfies SkillGroup[],

  agents: {
    heading: "Works with your agent",
    sub: "The skills use the open Agent Skills format: plain folders with a SKILL.md file. Any agent that loads skills can run them.",
    list: [
      { name: "Claude", icon: "claude" },
      { name: "Codex", icon: "codex" },
      { name: "Cursor", icon: "cursor" },
      { name: "Gemini CLI", icon: "geminicli" },
      { name: "GrokBot", icon: "grokbot" },
    ],
    footnote:
      "Not on the list? Clone the repo and copy the skill folders into your agent's skills folder. For Claude Code that's <code>.claude/skills/</code>.",
  },

  faqs: [
    {
      q: "What is AEO (answer engine optimization)?",
      a: "AEO is the work of getting your content quoted in AI answers from ChatGPT, Perplexity, Claude and Google AI Overviews. Answer engines pull a single passage that answers the question, so AEO means writing sections that each answer one question clearly, citing sources and making your site easy for AI crawlers to read.",
    },
    {
      q: "What's the difference between AEO and SEO?",
      a: "SEO gets a page ranked in Google's search results. AEO gets a passage from that page quoted in an AI-generated answer. They overlap heavily: AI engines mostly draw on pages that are indexed and trusted. These skills treat them as one job and write every page answer-first so it can do both.",
    },
    {
      q: "How do I get my website cited by ChatGPT and Perplexity?",
      a: "Make sure AI crawlers can reach your pages, then publish pages that answer the exact questions your buyers ask, with the answer in the first sentence of each section, real numbers, named sources and quotes from real people. The <code>aeo-seo-technical-audit</code> skill checks the crawl side; the page skills handle the writing.",
    },
    {
      q: "How do I show up in Google AI Overviews?",
      a: "Google builds AI Overviews from pages it already indexes and ranks, so the basics come first: a crawlable, indexed site and pages that rank for the query. Then write each section to answer one question directly. There's no separate switch to opt in, and no tool can guarantee a spot.",
    },
    {
      q: "Can Claude Code or Codex do SEO?",
      a: "Yes, with the right skills and data. On their own, coding agents guess at keywords and invent numbers. These skills give them a step-by-step method and connect them to real Search Console and keyword data through OpenSEO, so they can audit a site, plan topics and ship pages you approve.",
    },
    {
      q: "What are agent skills?",
      a: "Agent skills are folders with a <code>SKILL.md</code> file that teach an AI agent how to do one job. The agent reads each skill's short description and loads the full instructions only when a task needs them. Claude Code, Codex, Cursor and other agents support the format.",
    },
    {
      q: "How do I install the AEO-SEO skills?",
      a: "Run <code>npx skills add kingscrosslabs/aeo-seo-skills</code> and pick the skills you want, or copy the folders into your agent's skills folder (for Claude Code, <code>.claude/skills/</code>). Then connect OpenSEO and run <code>aeo-seo-setup</code> to build your site profile.",
    },
    {
      q: "Do I need a paid SEO tool to use these skills?",
      a: "You need an OpenSEO account. The skills use it for Search Console data, keyword volume and live search results, and they stop rather than guess a number if it isn't connected. Paid lookups use OpenSEO credits, and every result is cached so you never pay for the same data twice.",
    },
    {
      q: "Will AI-written content hurt my Google rankings?",
      a: "Google's guidance is that it rewards helpful content however it's made, and penalizes mass-produced pages written to game rankings. These skills write one page at a time, from real research and first-hand experience, and wait for your approval before anything ships.",
    },
    {
      q: "Are the AEO-SEO skills free?",
      a: "Yes. They're open source under the MIT licence. You pay only for your AI agent and any OpenSEO credits you use.",
    },
  ],

  closing: "Turn your agent into an AEO & SEO expert with these skills.",

  sister: {
    name: "content-creation-skills",
    url: "https://content-creation-skills.com",
    blurb: "Hooks, scripts, posts and newsletters in your voice.",
  },
};
