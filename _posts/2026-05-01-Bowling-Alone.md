---
published: true
layout: single
title:  From &quot;Bowling Alone&quot; to Coding Alone
subhead: AI coding tools are eroding the mentorship, code review, and community that built software's social capital — and why we need to rebuild it on purpose.
categories:
  - Blog
tags:
  - AI
  - Society
  - Engineering
pubdate: 'May 17, 2026'
date: 2026-05-17
author: Abhi Nemani
img: coding-alone-1.png
---

I learned software through other people.

Not just from classes or manuals, but from strangers who answered questions, maintainers who pushed back on bad assumptions, colleagues who thought out loud, and civic technologists who believed that building together was part of the point. Some of the most important lessons I learned about technology were not really about code. They were about judgment, patience, trust, and the habits of working in public.

That is why AI coding tools feel both thrilling and unsettling. I use them constantly. [Cursor](https://www.cursor.com/), [Claude Code](https://www.anthropic.com/claude-code), [GitHub Copilot](https://github.com/features/copilot), and tools like them make me faster. They help me get unstuck. They let small teams and solo builders do things that used to require far more time, money, and institutional support.

But they also make it easier to bypass the people, practices, and public conversations that once formed developers. Now we can code alone.

What worries me is not that AI makes us code alone in a literal sense. The worry is that it lets us solve problems without passing through the social rituals that once made software a community: asking, explaining, reviewing, arguing, mentoring, and leaving traces for the next person.

![Changing the conversation](/img/coding-alone-2.png)

## The Social Capital of Useful Strangers

When Robert Putnam published [Bowling Alone](https://www.simonandschuster.com/books/Bowling-Alone-Revised-and-Updated/Robert-D-Putnam/9781982130848), his sharpest observation was that Americans had not stopped bowling. They had stopped bowling in leagues. The individual act persisted. The communal scaffolding disappeared.

Putnam’s concern was not bowling itself. It was social capital: the trust, reciprocity, shared norms, and weak ties that make cooperation easier. Leagues mattered because they taught people to show up, coordinate, disagree, forgive, and do small things for people outside their closest circle.

Software had its own version of that. Open-source projects, issue threads, code reviews, forums, hack nights, and standards bodies were not just places where technical work happened. They were places where technical social capital accumulated.

Marc Dunkelman’s [The Vanishing Neighbor](https://wwnorton.com/books/9780393352078) helps explain the specific layer being lost. We have not lost all relationships. We have lost the middle ring: not close family or friends, not broadcast audiences, but the people [“not as close as kith or kin, but not as distant as a mere acquaintance.”](https://www.washingtonpost.com/opinions/ej-dionne-where-goes-the-neighborhood/2014/08/10/8a137cde-1f39-11e4-ae54-0cfe1f974f8a_story.html)

Software culture once produced those relationships in abundance: the [Stack Overflow](https://stackoverflow.com/) stranger at 2 a.m., the open-source co-maintainer in another time zone, the senior engineer whose blog post taught you something years later, the person at a hack night who understood the weird API problem before you could explain it cleanly.

That was social capital in practical form. Not friendship exactly, and not professional networking in the LinkedIn sense. It was a loose web of trust and reciprocity among people who might never meet but still made one another better. You learned because someone else had left a trace. You contributed because someone else eventually would need one.

I [wrote earlier](https://abhinemani.com/blog/2024/12/28/Organizational-Kid/) about the collapse of institutional trust. Software’s commons was a strange exception: a place where showing up still meant something.

The visible artifact was code. The invisible output was judgment. A person learned what a good bug report looked like, how to ask a question without wasting other people’s time, why backward compatibility was moral as much as technical, and why “working” was not the same as “ready.” Cleverness was not the same as stewardship.

AI can explain these things. But explanation is different from participating in the practices that sustain them.

## What it Means to Code Alone

Software is entering its own bowling-alone moment. Developers are writing more code than ever, with astonishingly capable tools. The output looks healthy. The social layer is weakening.

The loss is easy to miss because nothing looks broken at first. The code still gets written. The bug still gets fixed. The developer may even be happier. What disappears is the small social transaction that used to surround the work.

You no longer have to explain your confusion to another person. You no longer have to wait for a maintainer. You no longer have to search through old threads and slowly discover how a community thinks. You no longer have to turn your private problem into public knowledge.

In many ways, that is a relief. But it is also a loss. Those rituals were not just inefficient ways of getting answers. They were how software created social capital. They turned strangers into a profession.

[Pair programming](https://www.agilealliance.org/glossary/pairing/) made the old ideal literal: one driver at the keyboard, one navigator thinking out loud. Companies like [Pivotal Labs](https://tanzu.vmware.com/labs) treated that practice as central to how software teams learned and worked. AI increasingly occupies the place once held by the second human. The driver is still there. The navigator is now a model.

The developer using an AI coding assistant is not alone in the old sense. They are in constant dialogue. But the dialogue is private, instantaneous, and unreciprocated. It solves the immediate problem while leaving little public residue: no searchable thread, no comment history, no record of false starts, no trace of the judgment that led from one approach to another.

The technical evidence points in the same direction. The [New York Times](https://www.nytimes.com/2026/04/06/technology/ai-code-overload.html) [has described](https://www.nytimes.com/2026/04/06/technology/ai-code-overload.html) a wave of AI-generated “code overload,” where companies struggle to review, secure, and assign responsibility for AI-generated work. A peer-reviewed study in [Nature Scientific Reports](https://www.nature.com/articles/s41598-024-61221-0) found that Stack Overflow traffic declined sharply after ChatGPT’s release, while Reddit developer communities did not see the same drop — a contrast the authors attribute to stronger social bonds. Stack Overflow question volume is reportedly [down roughly 76% from its 2017 peak](https://developers.slashdot.org/story/25/01/10/1729248/stackoverflow-usage-plummets-as-ai-chatbots-rise), while [81.5% of GitHub contributions](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) now happen in private repositories. Projects like [cURL](https://www.itpro.com/software/open-source/curl-open-source-bug-bounty-program-scrapped) and [Godot](https://www.pcgamer.com/software/platforms/open-source-game-engine-godot-is-drowning-in-ai-slop-code-contributions-i-dont-know-how-long-we-can-keep-it-up/) have faced growing burdens from low-quality AI-generated submissions.

But the core problem is not technical. It is social. AI gives us the answer without the relationship, the solution without the public trace, the productivity without the apprenticeship.

![Commons is going private](/img/coding-alone-3.png)

## Rebuilding the Leagues

The deeper problem is that AI is drawing from a commons it may also weaken. The models that make private development so seamless were trained on the public web: mailing list arguments, issue threads, Stack Overflow answers, and blog posts where developers thought out loud. That public record taught the models. Now the models answer questions privately.

The answer is not nostalgia. It is institution-building.

![Individual Outputs vs Community](/img/coding-alone-4.png)

Putnam’s later work, [The Upswing](https://www.simonandschuster.com/books/The-Upswing/Robert-D-Putnam/9781982129156), argues that civic infrastructure is not inherited. It is built. Software’s “we” period was built too. Open-source norms, code review culture, Stack Overflow, hackathons, and civic tech brigades were civic inventions. If they are eroding, we have to build new ones.

That means treating human software culture as infrastructure, not overhead. The question is not just how much code we can produce with AI. It is whether we can keep producing the trust, norms, mentorship, and social capital that make code worth relying on.

Hackathons, pair programming, open source, technical writing, and code review become more valuable, not less, because they preserve something AI does not automatically provide: a reason to be accountable to other people.

In the old world, the work produced the commons. In the new one, the commons will have to be built on purpose.

People are still bowling. The leagues will only come back if someone builds them.