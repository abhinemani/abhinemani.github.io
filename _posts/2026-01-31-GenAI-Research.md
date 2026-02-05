---
published: true
layout: single
title: How I built GenAI to listen, not just make.
subhead: What happens when you are interviewed by a machine.
categories:
  - Blog
tags:
  - AI
  - Data
  - Product
  - Research
pubdate: 'February 4, 2026'
date: 2026-02-04
author: Abhi Nemani
img: cronkite-cover.png
---
I spend an unreasonable amount of time answering market research questions.

Sometimes I’m responding directly—city leaders trying to make sense of a crowded GovTech market, investors probing for traction and risk, researchers looking for signal in what increasingly feels like noise. Other times, I’m building the research itself: conducting interviews, reading budgets and procurement documents, triangulating reports, trying to understand how institutions actually behave rather than how they describe themselves.

The questions themselves aren’t the problem. They’re usually reasonable, often thoughtful. What wore me down was the sense that my answers weren’t getting better—even as the tools around me supposedly improved. Too often, what I offered was stitched together from half-remembered conversations, secondhand analyses, and PDFs I’d skimmed but never fully absorbed. I wasn’t being careless. I was operating inside a system that makes accuracy expensive and confidence cheap.

At some point, I stopped trying to answer faster and started wondering why—after all this data, all these dashboards, all these tools—it was still so hard to answer *well*.

That frustration is what led me to build **Cronkite**, a simple AI-powered market research tool designed to help retain and interrogate context across fragmented sources. I initially thought of it as a workflow improvement: a way to reduce friction, retain institutional memory, and avoid starting from scratch every time a familiar question came back around. I did not expect it to change how I think about generative AI itself.

![Homepage of demo site](/img/cronkite-start.png) 

What surprised me wasn’t what the system could generate.

It was what it made visible.

## Limits of the Current Thinking
We’ve come to describe this moment as the rise of “Generative AI,” and it’s easy to see why. The most visible capability of these systems is their ability to produce language—summaries, drafts, strategies—quickly and fluently. In many contexts, that alone feels transformative.

But the way a technology first enters common use isn’t always where its most durable value lies.

By focusing so heavily on generation, we’ve implicitly positioned large language models as writing engines—tools that sit at the end of the research process. We ask them to help articulate conclusions, compress complexity, or refine arguments. Evidence gathering, context-building, and verification are still assumed to be human responsibilities.

A similar tension is beginning to surface in fields that depend heavily on research and judgment. In healthcare market research, for example, analysts are already noticing that as AI becomes better at producing content, something else quietly becomes more <a href="https://www.physicianleaders.org/articles/how-gen-ai-is-transforming-market-research)">valuable</a>: “As AI-generated content becomes more prevalent, the value of authentic, verifiable data <strong>increases rather than decreases</strong>.”

This observation captures something important. The risk isn’t that AI floods the world with bad answers. It’s that it makes **unearned certainty cheap**. In that environment, the scarce input isn’t articulation—it’s grounding.

## From Generation to Recovery
![Mobile Render](/img/cronkite-mobile.png) 

This distinction shaped how I approached building Cronkite. I wasn’t trying to automate insight or replace judgment. I was trying to reduce the friction involved in gathering and holding evidence—especially in local government, where the data is public but deeply fragmented. Procurement records, budget documents, council agendas, vendor registries, interview transcripts, policy memos—all of it describes the same institutional reality, but rarely in ways that align naturally.

![Desktop Render](/img/cronkite-home.png) 

Traditional research methods compensate for this fragmentation by relying on people: analysts conducting interviews, experts offering perspective, teams synthesizing findings into reports. I’ve worked with expert networks like GLG and Third Bridge, and while the people involved are capable, the process itself is often redundant. Each project starts close to zero, context accumulates unevenly, and much of the underlying evidence disappears once the final deck is delivered.

Rather than responding with synthesized conclusions, the system repeatedly returned adjacent material—documents, excerpts, and references that complicated the original claim instead of resolving it.

I wanted to take a different approach. Instead of asking the system to generate conclusions, Cronkite focuses on **recovery**: continuously collecting material, normalizing incompatible formats, and structuring information so that context compounds rather than resets. The AI’s role is not to decide what matters, but to ensure that what exists is visible and accessible.

![Cronkite Homepage](/img/cronkite-share.png) 

This can sound like a modest shift. In practice, it changes the entire posture of the system. You can ask questions that matter.

![Cronkite Homepage](/img/cronkite-interview.png) 

## Being Questioned by a Machine
The system worked in unexpected ways; it pushed me harder and gathered more information than a human interviewer has in my experience. And it seems that we can take broad ideas like AI into specific examples.

The clearest signal that this approach was different didn’t come from a dashboard. It came from the experience of being questioned. Here's an example: 

* **Conkite App**: How are cities thinking about AI right now?
* **User:** There’s a lot of interest.
* **Conkite App**: “Interest” isn’t actionable. What did they do as a result of that interest?
* **User:** Some conversations, a few pilots.
* **Conkite App**: Were those pilots funded as ongoing programs?
* **User:** No, mostly one-time.

I expected the interaction to feel constrained or mechanical. Instead, it was more demanding than many human-led conversations. The system didn’t politely fill in gaps or smooth over ambiguity. 

What stayed with me wasn’t the quality of the questions so much as how they felt to answer. The model wasn’t confrontational, but it was unyielding. It didn’t let me rely on shorthand or professional muscle memory. Answers that would pass unchallenged in a meeting—“budgets are tight,” “cities are interested,” “it depends”—simply didn’t move the conversation forward. Each time I tried to generalize, the model slowed things down and asked me to be specific in ways that were mildly uncomfortable, because they forced me to notice where I was leaning on experience rather than evidence.

![Cronkite Homepage](/img/cronkite-goodrobot.png) 

There was also something subtly disarming about the interaction. A human interviewer often gives you cues—agreement, skepticism, impatience—that shape how much you explain or defend. The model did none of that. It just kept asking, calmly and precisely, until the answer either became grounded or collapsed under its own vagueness. I found myself thinking more carefully, not because I was being judged, but because there was nowhere to hide. In that moment, GenAI stopped feeling like a tool for producing output and started feeling like a mirror for my own reasoning—one that reflected back not what I meant to say, but what I had actually substantiated. 

For the first time in my research work, I wasn’t deciding when a line of inquiry was “good enough” — the system was.

When an answer relied on shorthand—terms like “risk,” “support,” or “momentum”—it asked for clarification. When examples were missing, it didn’t move on for the sake of flow; it treated that absence as something worth examining. When evidence was incomplete, the system did not compensate. It stopped. Missing information was treated as a condition to resolve, not an inconvenience to bypass. And it pushes:

* **Conkite App**: How would you describe the current budget environment for cities?
* **User:** Budgets are pretty tight right now.
* **Conkite App**: “Tight” relative to what?
* **User:** Relative to the last few years — costs are up, revenues are uneven.
* **Conkite App**: Which costs increased the most?
* **User:** Labor and technology, mostly.
* **Conkite App**: Were those increases absorbed evenly across departments?
* **User:** No, some departments were protected.
* **Conkite App**: Which ones?
* **User:** Public safety, core operations.
* **Conkite App**: Then which departments absorbed the constraint?
* **User:** Finance, IT, grants management.
* **Conkite App**: Got it. Thanks for clarifying

That experience reframed how I think about common concerns around generative AI, particularly the risk of hallucination. In this context, the more salient risk wasn’t that the system would invent facts, but that humans would rely too heavily on confidence when evidence was incomplete. Used as a recovery tool rather than a generator, the AI didn’t obscure those gaps. It made them harder to ignore.

![Cronkite Homepage](/img/cronkite-sentiment.png) 

That experience reframed how I think about common concerns around generative AI, particularly the risk of hallucination. In this context, the more salient risk wasn’t that the system would invent facts, but that humans would rely too heavily on confidence when evidence was incomplete. Used as a recovery tool rather than a generator, the AI didn’t obscure those gaps. It made them harder to ignore.

## Implications for Research and the Market

![Cronkite Homepage](/img/cronkite-data.png) 

As AI-generated content becomes more common, fluent text is likely to become less distinctive. When anyone can produce a confident-sounding memo in seconds, the value of the memo itself declines. Scarcity shifts elsewhere—to provenance, cross-source synthesis, institutional context, and a clear understanding of what remains uncertain.

![Cronkite Homepage](/img/cronkite-sentiment.png) 

What the system consistently resisted was premature closure. It privileged traceability over polish, and specificity over speed.

This suggests a gradual change in where value accrues in the research market. Tools that emphasize synthesis without evidence may struggle to differentiate themselves. Tools that reduce the cost of assembling, contextualizing, and interrogating real-world information become more important—particularly in domains where decisions carry public consequence and scrutiny.


For government, this matters not because AI promises efficiency, but because it offers a way to make complexity more manageable without oversimplifying it. Lowering the cost of evidence gathering doesn’t eliminate judgment. It creates the conditions for better judgment.

![Cronkite Homepage](/img/cronkite-dash.png) 

## But sometimes, it doesn't work.

Any tehnology leader will be quick to remind you that most tools are buggy, and AI's habit of hallucinating ideas, we should be especially concered.

All AI tolls will grapple with this, bad code, bad chats, and bad robots. The challenge for AI builders, especially government ones, is how to balance the risk v. reward. And in the market research context, not just risk and reward, but also cost. Public sector organization should be open to exploring ways to minimize risk and cost while improving scale and quality. Turning human intevise funcations into machine-led approachs may help, but there are still a lot of questions. 

## Repositioning the Technology
![Cronkite Homepage](/img/cronkite-generation.png) 

None of this requires rejecting the generative capabilities of these systems. Writing, summarization, and synthesis remain useful. But they are most valuable when they rest on a stronger foundation.

Rather than thinking of generative AI primarily as a tool for producing answers, it may be more helpful to see it as **infrastructure for understanding**—something that helps recover, organize, and hold reality in view long enough for people to reason about it.

The future of research, at least in complex domains like government, is unlikely to hinge on generating more content. It will hinge on making existing information easier to assemble, examine, and trust.

That, more than anything, is the opportunity I didn’t fully appreciate until I got tired of answering the same questions—and started asking why they were so hard to answer well in the first place.
