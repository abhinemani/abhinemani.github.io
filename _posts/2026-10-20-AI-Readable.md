---
published: true
layout: single
title: 'An easy way to launch your AI strategy: become bot friendly'
subhead: As an experiment, I spent some time optimizing my own site for AI. Here's how, and what I learned.
categories:
  - Blog
tags:
  - AI
  - GovTech
  - Technology
pubdate: 'October 20, 2026'
date: 2026-10-20
author: Abhi Nemani
img: ai-readable-hero.jpg
---
Right now, most organizations' AI strategy comes down to one of two moves: build (or buy) their own AI bot, or lock their content away from AI training. Neither gives people what they actually want, which is reliable answers inside the bots they already use, like Claude, ChatGPT and Perplexity.

It reminds me of the Web 2.0 days, when every city wanted its own transit app. The real win turned out to be getting Google to ingest the transit data, so directions showed up where riders already were. I've long argued for making the apps people already use [more civic](https://abhinemani.com/essays/2020/08/28/Ubers-as-Ambulances/), and AI assistants are the newest of those apps.

So I ran two experiments. First, I checked how ready America's five largest cities are for the AI their residents already use. Then I tried making my own site as readable as possible.

### Readable by accident

People increasingly ask a chatbot about trash pickup, permits or parking tickets instead of searching a city website. That makes the website a source document for a machine, not just a page for a person. So on October 20 I audited New York, Los Angeles, Chicago, Houston and Phoenix, following the path an AI agent actually walks through a site. Is it welcome? Is there a map? Does the content arrive as readable text? Does the site say clearly who it is, point to usable data, and stay current?

<iframe class="agent-embed" src="https://abhinemani.com/embed/city-ai-scorecard.html" title="How AI-ready are America's five largest city websites?" width="100%" height="720" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

Los Angeles edges out Phoenix and New York, Houston trails, and Chicago is effectively closed to an agent at the front door. No city clears even two-thirds of the checks.

The clearest finding is in the rows where every city fails. None names an AI crawler, none publishes an llms.txt, and none uses structured data to tell a machine "this is the official government of this city." Every AI bot falls under a generic robots.txt rule written for an earlier web. These sites are readable mostly by accident. That matters because AI crawlers do three different jobs: gathering training data, indexing for AI search, and fetching a page live because a resident just asked a question. A city might welcome the last two and decline the first, but it can only make that choice by naming the crawlers. Silence isn't a policy; it's a default.

Each city falls short in its own way:

- **Los Angeles** is readable, with a working sitemap and good metadata, but its homepage doesn't point an agent to open data. LA was ranked the #1 open data city when I was its Chief Data Officer, and today an agent landing on lacity.gov gets no signpost to it.
- **Phoenix** has a clean robots.txt pointing to a fresh sitemap, but its news and calendar showed my fetcher "Loading…" beside an alert that read "This alert has expired." A person sees a working page; a machine sees a broken one.
- **New York** has solid plumbing but no homepage path to its open data, one of the richest in the country.
- **Houston** has no real robots.txt (the address returns the homepage), no sitemap, and a footer that still reads "© 2022," though it does link its open data and finance portals.
- **Chicago** refuses agents at its homepage, robots.txt and sitemap, while an interior page still features a 2018 pension address by Mayor Rahm Emanuel, with nothing to tell an AI it's history. Blocking robots.txt is especially self-defeating: it's where well-behaved crawlers learn the rules, so a block there turns away exactly the bots that would have listened.

None of this is negligence. City web teams run huge, aging systems on thin budgets, and AI crawlers have [hammered government servers](https://www.thedroptimes.com/node/50960). Chicago's block is more likely a firewall rule aimed at that traffic than a policy about AI. But blunt blocks and silent defaults leave residents' chatbot answers to chance. A few governments are deciding on purpose: [Maryland published the first state llms.txt](https://technical.ly/civics/maryland-uses-llms-txt-to-guide-ai-chatbots/) in January, after counting nearly 12 million requests from 15 AI crawlers in a single month.

### What I tried on my own site

To see what readable *by design* takes, I spent a weekend on my own site with Claude Code, Anthropic's AI coding agent, while I directed and made the judgment calls. Four changes did most of the work.

**Same address, two readers.** A person and an AI agent can ask for the same page and each get the version built for them. Three small rules at Cloudflare serve a page's Markdown copy at the same address when an agent asks for it, and point agents to my site guide and skills. Browsers see no difference. Agents get pages that are, on average, **77% smaller**, every word intact. Flip between them:

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-two-readers.html" title="Same address, two readers" width="100%" height="800" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

**A welcome mat and a map.** My robots.txt names 13 AI crawlers outright, and an [llms.txt](https://abhinemani.com/llms.txt) file acts as a front door: a short bio, how to attribute my work, and 111 links to every essay, lesson and case study. All 105 full-text pages have a clean Markdown twin, and interactive charts now arrive as sentences carrying their data.

**Usable, not just readable.** I published two "agent skills," short instruction files an AI loads when a task calls for them. [One](https://abhinemani.com/.well-known/agent-skills/govtech-market-sizing/SKILL.md) teaches my bottom-up method for sizing the GovTech market and points to my [TAM/SAM calculator](https://abhinemani.com/govtech-market/), built on 2022 Census of Governments finance data. [The other](https://abhinemani.com/.well-known/agent-skills/cite-abhi-nemani/SKILL.md) tells an AI how to quote me faithfully and describe my role as of an essay's date, which is the same stale-truth problem as Chicago's 2018 page, at personal scale.

**One clear identity.** Asked to review the site cold, ChatGPT called it "very AI-friendly," but caught that my site described me four different ways. Now one sentence leads everywhere, and my homepage finally has a main headline that starts with my name.

A suite of 100 automated tests checks all of it against the live site. It caught real problems, including one of the AI's own fixes briefly stripping the address from every link. If you want to dig in, you can [send requests to my site](https://abhinemani.com/embed/agent-request-playground.html), [follow an agent's path](https://abhinemani.com/embed/agent-crawler-route.html) or [see every check](https://abhinemani.com/embed/agent-scorecard.html).

### What I'd tell public-sector leaders and GovTech founders

**Before you build a bot, make your content readable.** A chatbot answers from what it can read, and so does every other AI your residents already use. (None of this is a knock on the clerks and webmasters working with the tools and procurement rules they were handed. It's a reason to give them better ones.)

**Decide about AI out loud.** Name the AI crawlers in robots.txt. Welcome AI search and live fetches made on a resident's behalf, and make a deliberate call on training. Never block robots.txt itself.

**Fix the basics first.** A working sitemap, text that reads without JavaScript, dates on everything and current content matter more than any AI-specific file. An llms.txt is a useful signal of intent, but it's a community convention, not an official standard, and support varies.

**Point machines to your data, and say who you are.** Link your open data portal from the homepage, and add structured data that says "this is the official city government." Pick one description and use it everywhere.

**Then make it usable, and verify.** A procurement office could publish a skill for its bidding process, or a city one for its permits. Then test what a bot actually receives, because real problems hide in pages that look fine.

### What I don't know yet

Readability is necessary, but it isn't sufficient. The open question is whether AI systems will actually cite this work. Each month I'll ask the same handful of questions ("Who are leading GovTech advisors?" "How big is the local government software market?") and see whether I show up, and how I'm described. I'll rerun the city audit too, and expand it to the 25 largest cities. Today's is a one-day snapshot run with an AI fetching tool, with every check weighted equally, so treat it as a smoke test rather than a ranking.

Paul Graham [put it bluntly](https://x.com/paulg/status/2111827351608725669) recently: if AIs can't find something, "then for all practical purposes it doesn't exist." He admits that isn't 100% true yet, but it will only get truer, and I'd rather my work exist. It's early yet. If you're working on making government information readable by AI, I'd love to compare notes, and if you'd like this audit run on your city, let me know.

<script>
window.addEventListener('message', function (e) {
  if (!e.data || e.data.type !== 'resize') return;
  document.querySelectorAll('iframe.agent-embed').forEach(function (f) {
    if (f.contentWindow === e.source) f.style.height = e.data.height + 'px';
  });
});
</script>
