---
published: false
layout: single
title: Making my site readable by AI
subhead: My writing now has two audiences, the people who read it and the AI systems that read it on their behalf. Here's how I rebuilt my site for both, and what I learned along the way.
categories:
  - Blog
tags:
  - AI
  - GovTech
  - Technology
pubdate: 'October 20, 2026'
date: 2026-10-20
author: Abhi Nemani
img: ai-readable-two-readers.png
---
My website now has two audiences: the people who read it, and the AI systems that increasingly read it on their behalf.

When someone asks ChatGPT, Claude or Perplexity how cities buy technology, or how big the local government software market is, those tools go looking for sources. For over a decade I've written about exactly those questions. If an AI can't read that work cleanly, it either skips it or gets it wrong.

So last week I spent an evening making abhinemani.com genuinely readable by AI. I did it with an AI coding agent working alongside me, which felt fitting. Here's what we built, what broke along the way, and what I'd tell any public-sector leader or GovTech founder thinking about the same thing.

### Same address, two readers

The core idea is simple: a person and an AI agent can visit the same page and each get the version built for them. Try it below. Flip between a person and an AI agent to see what each one actually receives when they ask for my recent essay on declining trust in local government.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-two-readers.html" title="Same address, two readers" width="100%" height="800" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

A person gets the designed page, with navigation, typography and interactive charts. An agent doesn't need any of that. It needs clean text, a title, a date and a link it can cite. Wrapping that text in 40 KB of styling and scripts just adds noise and cost.

Web browsers and AI agents announce what format they prefer. Agents increasingly ask for Markdown, a plain-text format that language models read easily. So I set up two small rules at Cloudflare, which sits in front of my site:

- When a request asks for Markdown, Cloudflare quietly serves the page's Markdown copy at the very same address.
- Every response now carries a header pointing agents to my site guide and my agent skills, before they parse a single line.

Browsers see no difference. Agents get a page that is, on average, **77% smaller** than the HTML. The trust essay goes from 40.1 KB to 7.4 KB, with every word intact.

You can poke at the rules yourself. Pick a page and the kind of request a client sends, and you'll see the real response my site returned, along with which rule made it happen. Try the GovTech calculator or a page that doesn't exist: the rules leave both alone, so nothing ever breaks.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-request-playground.html" title="Send a request to abhinemani.com" width="100%" height="620" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### The blog and the Public Innovation Academy

Most of the work went into the writing itself: more than a decade of essays, plus the [Public Innovation Academy](https://abhinemani.com/academy/)'s free guides to how local government buys and builds technology.

**A map for AI.** I added an [llms.txt](https://abhinemani.com/llms.txt) file, an emerging convention that acts as a front door for AI. It gives a short bio, guidance on how to attribute my work, and an index of 111 links: every essay, Academy lesson and portfolio case study, each with a one-line summary. It also asks AI systems to check an essay's date before describing my current role, since my title in 2014 isn't my title today.

**A clean copy of every page.** Every essay, lesson and case study now has a Markdown twin with the title, canonical URL, date and tags at the top. That's 105 full-text pages. Even the 46 pages with no article text, like press clippings, return a short summary instead of an error. For agents that want everything at once, [llms-full.txt](https://abhinemani.com/llms-full.txt) holds the whole archive in a single file.

**Charts as sentences.** Several recent essays use interactive charts drawn by JavaScript, which most agents can't run. My first pass left the chart's raw code in the Markdown, more than half of the trust essay's file. Now each chart arrives as one sentence carrying its data. Flip the card to compare.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-before-after.html?card=charts" title="Charts as sentences: before and after" width="100%" height="480" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

**Cleaning up the archive.** My older posts came over from Medium years ago, carrying stray HTML, embedded tweets and coded punctuation. All of it is now plain text: links, quotes and all 906 em dashes. Yes, I counted. Readers on the site see no change, but an agent now gets a tweet as a clean quote instead of a block of markup.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-before-after.html?card=tweets" title="Embedded tweets: before and after" width="100%" height="480" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### The calculator and two agent skills

This is the part I'm most excited about. Being *readable* is table stakes. The next step is being *usable*: teaching an AI how to do something the way I would.

"Agent skills" are short instruction files an AI can load when a task calls for them. I published two at a [standard discovery address](https://abhinemani.com/.well-known/agent-skills/index.json), each with a checksum so an agent can confirm it hasn't been altered.

![Two agent skills: GovTech market sizing, which sizes the local government market bottom-up and links to the TAM/SAM calculator, and citing my work, which covers attribution and my roles by date](/img/ai-readable-agent-skills.png)

**GovTech market sizing.** Founders and investors constantly ask how big the local government market really is for their product. Too often the answer is a top-down guess from total public spending. [This skill](https://abhinemani.com/.well-known/agent-skills/govtech-market-sizing/SKILL.md) teaches an AI my bottom-up method instead: size the market by jurisdiction tier, using real counts of governments, tiered pricing and realistic adoption rates. It points to my [GovTech TAM/SAM calculator](https://abhinemani.com/govtech-market/), which does the math for every U.S. local government using 2022 Census of Governments finance data. The calculator now also appears in my site guide and sitemap, so agents can find it.

**Citing my work.** [The second skill](https://abhinemani.com/.well-known/agent-skills/cite-abhi-nemani/SKILL.md) tells an AI how to quote and summarize me faithfully: where to find the clean text, how to attribute it, and never to invent a quote. It also lists my roles by date, from Code for America to Los Angeles, Sacramento and Euna Solutions. That way a 2015 essay gets described as written by LA's Chief Data Officer, not by whatever my title is today.

My hope is that the next time someone asks an AI to size a GovTech market, it reaches for a method built on real data rather than a guess.

Put together, here's the path an AI agent now takes through the site, from checking whether it's welcome to reading the whole archive. Step through it to see the real file at each stop.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-crawler-route.html" title="How an AI agent finds its way" width="100%" height="800" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### Saying clearly who I am

Once the plumbing worked, I asked a different AI, ChatGPT, to review the site cold. Its verdict was "very AI-friendly." It also caught something I'd missed entirely: my site described me four different ways.

The homepage called me "a leader in Government Technology for over a decade." The About page said "I help leaders, investors and companies build GovTech that scales." My structured data said "Founder, GovTech Consultant, Advisor & Investor." My CV said "Civic technology executive." None of those is wrong, but an AI stitching together a description of me gets four answers.

Now one sentence leads everywhere a search engine or AI looks: the meta descriptions, the structured data, link previews, the site guide and the CV.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-before-after.html?card=bio" title="One bio: before and after" width="100%" height="480" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

The review also noticed that my homepage had no main headline in its code. The big tagline was styled to look like one, but technically it wasn't. The page looks exactly the same today, but its top-level heading now starts with my name.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-before-after.html?card=h1" title="Homepage headline: before and after" width="100%" height="480" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### Testing it like it matters

Configuration isn't the same as working. So everything gets checked against the live site by a suite of 100 automated tests, now saved in the site's code so I can rerun it anytime.

The tests fetch every page in my sitemap three ways: as a browser, as an AI asking for Markdown, and directly as its Markdown copy. They confirm the major AI crawlers, from OpenAI, Anthropic and Perplexity, get through without being blocked. They also try to trip up the Cloudflare rules, for example by making sure a missing page still returns an honest error instead of an invented one.

Testing paid off. Looking at what an agent actually received surfaced problems no checklist would have:

- Half of one essay's Markdown was leftover chart code.
- Embedded tweets arrived as raw HTML.
- Four links in two posts pointed nowhere.
- One of the AI agent's own fixes briefly stripped the address from every link. The comparison caught it before it shipped.

All of those are fixed. Today the site passes all 100 checks. Open any group to see what it covers.

<iframe class="agent-embed" src="https://abhinemani.com/embed/agent-scorecard.html" title="Every check, against the live site" width="100%" height="670" loading="lazy" style="border: none; display: block; margin: 20px auto;"></iframe>

### What I'd tell public-sector leaders and GovTech founders

**Your next reader may not be a person.** Residents already ask AI tools how to get a permit, where to pay a bill or what a council decided. If a city's information is buried in PDFs and JavaScript, AI will answer anyway, from worse sources.

**Readable comes first.** Clean text, clear headings, dates and canonical links matter more than any AI-specific file. Most of this work is good web hygiene with a new reason to care.

**Then make your expertise usable.** Agent skills are early, but the idea is powerful. A procurement office could publish a skill for its bidding process. A GovTech company could publish one for its integrations. You aren't only being found, you're shaping how the work gets done.

**Say who you are, once.** Pick one clear description of your organization or yourself, and use it everywhere.

**Verify, don't assume.** Test what a bot actually receives. We found real problems that looked fine on paper.

The open question is whether AI systems will actually cite this work. That's what I'll be watching next. In the meantime, if you're working on making government information readable by AI, I'd love to compare notes. Ask your favorite AI about GovTech market sizing, and let me know what it says.

<script>
window.addEventListener('message', function (e) {
  if (!e.data || e.data.type !== 'resize') return;
  document.querySelectorAll('iframe.agent-embed').forEach(function (f) {
    if (f.contentWindow === e.source) f.style.height = e.data.height + 'px';
  });
});
</script>
