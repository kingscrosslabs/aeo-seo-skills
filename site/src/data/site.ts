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
    note: "Needs an OpenSEO account for search data.",
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
      "Claude Code",
      "Codex",
      "Cursor",
      "GitHub Copilot",
      "Gemini CLI",
      "OpenCode",
      "Windsurf",
      "Cline",
    ],
    footnote:
      "Not on the list? Clone the repo and copy the skill folders into your agent's skills folder. For Claude Code that's <code>.claude/skills/</code>.",
  },

  faqs: [
    {
      q: "What are AEO-SEO skills?",
      a: "They are open-source skills for AI agents that do search engine optimization (SEO) and answer engine optimization (AEO) together. Each one teaches your agent one job, like auditing your site, planning topics or writing a comparison page, using real search data.",
    },
    {
      q: "What's the difference between AEO and SEO?",
      a: "SEO gets a page ranked in Google's results. AEO gets a page quoted in AI answers from ChatGPT, Perplexity and Google AI Overviews. AEO rewards pages where each section answers one question on its own, so these skills write answer-first and cover both.",
    },
    {
      q: "Which AI agents can use them?",
      a: "Claude Code, Codex, Cursor and any agent that loads skills in the Agent Skills format (a folder with a <code>SKILL.md</code> file).",
    },
    {
      q: "How do I install them?",
      a: "Run <code>npx skills add kingscrosslabs/aeo-seo-skills</code> and pick the skills you want. Or clone the repo and copy the skill folders into your agent's skills folder. Then connect OpenSEO and run <code>aeo-seo-setup</code>.",
    },
    {
      q: "Do I need OpenSEO?",
      a: "Yes. Every skill uses OpenSEO for Search Console data, keyword volume and live search results, and stops if it isn't connected rather than guess a number. Paid calls use OpenSEO credits; the skills cache every result so nothing is bought twice.",
    },
    {
      q: "Do I have to tell my agent which skill to use?",
      a: "No. Describe what you want and your agent picks the skill from its description. You can also name it, for example “use blog-post”.",
    },
    {
      q: "Will they publish anything without me?",
      a: "No. Every brief and every page waits for your approval before it ships.",
    },
    {
      q: "Are the skills free?",
      a: "Yes. They're open source under the MIT licence. The only cost is your agent and any OpenSEO credits you use.",
    },
  ],

  sister: {
    name: "content-creation-skills",
    url: "https://content-creation-skills.com",
    blurb: "Hooks, scripts, posts and newsletters in your voice.",
  },
};
