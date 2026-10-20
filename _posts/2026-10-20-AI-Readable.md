---
published: false
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
Paul Graham put the stakes in two sentences:

> To publish something on a paywalled site is to make it invisible. If AIs can't find it, then for all practical purposes it doesn't exist.
>
> These two sentences aren't 100% true yet, but they will only get truer.
>
> — Paul Graham ([@paulg](https://x.com/paulg/status/2111827351608725669))

Paywalls are rare in government. But a permit guide buried in a scanned PDF is invisible to an AI in much the same way. Residents already ask ChatGPT, Claude and Perplexity how to get a permit or what the council decided, and if the answer isn't readable, the AI answers anyway, from worse sources.

Right now everyone is thinking about building their own bot, government especially. I understand the instinct, but a question comes first: is your content readable by the AIs your residents already use? A bot is only as good as the content behind it, and clean content gets you found everywhere else too. It's an old argument of mine. In 2020 I wrote "[Ubers as Ambulances?](https://abhinemani.com/essays/2020/08/28/Ubers-as-Ambulances/)" ("And other ideas to make consumer apps more civic"), arguing for fewer new civic apps and more effort making the platforms people already use more civic. AI assistants are the newest of those platforms.

So over the weekend I tried it on my own site, working with Claude Code, Anthropic's AI coding agent, while I directed and made the judgment calls. Here's what we built, what broke, and what I'd tell anyone weighing the same project.

### Same address, two readers

The core idea is simple: a person and an AI agent can ask for the same page and each get the version built for them. Flip between them below to see what each receives for my recent essay on declining trust in local government.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-two-readers.html" title="Same address, two readers" width="100%" height="800" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

People get the designed page. An agent needs clean text, a title, a date and a link it can cite, not 40 KB of styling and scripts. Every browser and AI agent announces the format it prefers, and a growing number of agents now ask for Markdown, a plain-text format language models read easily. So I set up three small rules at Cloudflare, which sits in front of my site: two serve a page's Markdown copy at the same address when asked, and one adds headers pointing agents to my site guide and skills. Browsers see no difference. Agents get pages that are, on average, **77% smaller**. The trust essay goes from about 40 KB to 7.4 KB, every word intact. (N.B. Cloudflare sells a one-click version of this on a paid plan. Three rules on the free one did the job.)

![Same address, two readers: a person gets the designed page, an AI agent gets clean Markdown, 82% smaller](/img/ai-readable-two-readers.png)

Poke at it yourself. Pick a page and a request type, and you'll see the real response my site returned.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-request-playground.html" title="Send a request to abhinemani.com" width="100%" height="620" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### The essays, research and tools

Most of the work went into the writing itself: more than a decade of essays, plus [my research, lectures and tools for the GovTech field](https://abhinemani.com/academy/).

**A welcome mat and a map.** My robots.txt now names 13 AI crawlers outright. An [llms.txt](https://abhinemani.com/llms.txt) file, an emerging convention, acts as a front door: a short bio, how to attribute my work, and 111 links to every essay, lesson and case study, each with a one-line summary.

**A clean copy of every page.** All 105 full-text pages now have a Markdown twin, and even pages with no article text return a short summary instead of an error. For agents that want everything at once, [llms-full.txt](https://abhinemani.com/llms-full.txt) holds the whole archive in a single file.

**Charts as sentences.** Most agents can't run the JavaScript behind my interactive charts. My first pass left raw chart code in the Markdown, more than half of the trust essay's file. Now each chart arrives as one sentence carrying its data: trust in local government fell 13 points, from 54% to 41%, with the source attached. Flip the card to compare.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-before-after.html?card=charts" title="Charts as sentences: before and after" width="100%" height="480" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### The calculator and two agent skills

This is the part I'm most excited about. Being *readable* is table stakes. The next step is being *usable*: teaching an AI to do something the way I would. "Agent skills" are short instruction files an AI can load when a task calls for them. I published two, each with a checksum so an agent can confirm it hasn't been altered.

[**GovTech market sizing**](https://abhinemani.com/.well-known/agent-skills/govtech-market-sizing/SKILL.md) replaces the usual top-down guess from total public spending with my bottom-up method: size the market by jurisdiction tier, using real counts of governments, tiered pricing and realistic adoption. It points to my [GovTech TAM/SAM calculator](https://abhinemani.com/govtech-market/), built on 2022 Census of Governments finance data. [**Citing my work**](https://abhinemani.com/.well-known/agent-skills/cite-abhi-nemani/SKILL.md) tells an AI how to quote me faithfully, never to invent a quote, and to describe my role as of an essay's date, so a 2015 piece is credited to LA's Chief Data Officer, not whatever my title is today.

Here's the path an agent now takes through the site, from checking whether it's welcome to reading the whole archive. Step through it to see the real file at each stop.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-crawler-route.html" title="How an AI agent finds its way" width="100%" height="800" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### Saying clearly who I am

I asked ChatGPT to review the site cold. Its verdict was "very AI-friendly," and it caught something I'd missed: my site described me four different ways. The homepage, the About page, my structured data and my CV each had their own version, and an AI stitching them together got four answers. Now one sentence leads everywhere, and my homepage, which had no main headline in its code, finally has one that starts with my name:

> Abhi Nemani is a GovTech and finance entrepreneur, advisor and scholar with more than 15 years building technology and scaling innovation for the public sector.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-before-after.html?card=bio" title="One bio: before and after" width="100%" height="480" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

ChatGPT also offered a fair caveat: files like llms.txt and agent skills are "useful experiments," and ordinary, crawlable HTML still matters most.

### Testing it like it matters

Configuration isn't the same as working, so a suite of 100 automated tests checks the live site the way a browser, an AI agent and a crawler would see it. Looking at what an agent actually received surfaced problems no checklist would have: four links that pointed nowhere, and one of the AI's own fixes briefly stripping the address from every link. A before-and-after comparison caught that before it shipped. Humbling, and exactly the point. Today the site passes all 100 checks.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-scorecard.html" title="Every check, against the live site" width="100%" height="670" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### What I'd tell public-sector leaders and GovTech founders

**Before you build a bot, make your content readable.** A chatbot answers from what it can read, and so does every other AI your residents already use. (None of this is a knock on the clerks and webmasters working with the tools and procurement rules they were handed. It's a reason to give them better ones.)

**Readable comes first, then usable.** Clean text, clear headings, dates and canonical links matter more than any AI-specific file. After that, a procurement office could publish a skill for its bidding process, or a city one for its permits. You aren't only being found, you're shaping how the work gets done.

**Say who you are, once, and verify.** Pick one description and use it everywhere. Then test what a bot actually receives, because real problems hid in pages that looked fine.

### What I don't know yet

Readability is necessary, but it isn't sufficient. The open question is whether AI systems will actually cite this work. Each month I'll ask the same handful of questions ("Who are leading GovTech advisors?" "How big is the local government software market?") and see whether I show up, and how I'm described.

Graham is right that none of this is 100% true yet. But if AIs can't find your work, it doesn't exist for a growing number of readers, and I'd rather mine exist. It's early yet. If you're working on making government information readable by AI, I'd love to compare notes. Ask your favorite AI about GovTech market sizing, and let me know what it says.

<script>
window.addEventListener('message', function (e) {
  if (!e.data || e.data.type !== 'resize') return;
  document.querySelectorAll('iframe.agent-embed').forEach(function (f) {
    if (f.contentWindow === e.source) f.style.height = e.data.height + 'px';
  });
});
</script>
