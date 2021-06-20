---
layout: single
title: Making Presentations from Spreadsheets
categories: 
- Blog
- Essays
subhead: Really it is better. Collaborate on the content in a structured, open way.
date: 2016-11-08
pubdate: November 8, 2016
img: slide1.png
---

A remember a few years back — well, now, maybe more than a few — while i was working at Code for America, we had the thoughtful idea of…

![](https://cdn-images-1.medium.com/max/800/1*2BWF57jB0a08HX0a2Uu0lw.png)
undefined

A remember a few years back — well, now, maybe more than a few — while i was working at Code for America, we had the thoughtful idea of including every since one of that year’s fellowship apps in the intro presentation at the annual Summit. Seems easy, no? Over a handful of teams working for just 11 months, that should be just a handful of slides, right?

No. **More like 30.**

So there we sat, our meager communications team, hammering away at Powerpoint to put together 30 slides, all with different content, but all with the same basic layout. With PPT’s auto-formatting — which hurt more than it helped, font sizes were askew, screenshots had different resolutions, and so on and so on. And then, of course, came edits from those teams, staff, and anyone else with an opinion.

At one point, I felt like giving my laptop, the [Office Space treatment](https://www.youtube.com/watch?v=N9wsjroVlu8).

undefined
undefined

So this year, when I was tasked with pulling together slides to pitch the City Council the 15 recommendations for the [RAILS grant program](https://sacmoie.github.io/RAILS/), I said:

**Not again.**

This year, I started with a clear bias: online instead of off, and collaborative instead of not. Easily, anyone savvy with HTML5 would jump to the number of great open-source projects that provide frameworks for lovely online presentations; and as many are hosted on github, collaboration is built in.

Problem: Not everyone I work now with knows what either HTML5 or github is — let alone both.

So I stepped back and thought about the ideal experience for me to do the “heavy-lifting” of design and formatting and my colleagues to edit and tweak. Effectively, I realized I wanted a very simple content management system (CMS) for slide, or put another way, a “data-driven” presentation.

![](https://cdn-images-1.medium.com/max/600/1*xFZIDukI3pjLKqZzlqenSQ.png)

Then I remembered how we approached a similar problem with [dashboard-ing in Los Angeles](https://medium.com/@abhinemani/government-dashboards-what-ought-we-do-b0dcc58f299d#.j7i2hkcyy): **Google Spreadsheets**, and a nice little bit of JS called [Tabletop](https://github.com/jsoma/tabletop). Wiring up those two enabled me then, and now, enabled clean, consistent, and elegant design and also general non-technical access and editing.

So here’s what we did:

*   Forked [Reveal.js](https://github.com/hakimel/reveal.js/) (what seems to be the standard-bearer for HTML5 presentations)
*   Added in some CSS for common look an feel on the “project” slides — the ones, which you’ll want to include common information, such as project name, descriptions, screenshots, etc. (Of course, you’ll still want others with introductory and conclusion slides.)
*   Set a doc in Google Spreadsheet with those same fields as headers, published it to the web, logged the spreadsheet unique ID, and entered in some placeholder content
*   Added the [TableTop.js](https://github.com/jsoma/tabletop) script to the repo — with the spreadsheet ID — and set up some javascript to pull the appropriate cells, buttressed with the appropriate CSS tags
*   Inserted a dummy div in my main html file and pointed the tabletop script at it
*   Turned on gh-pages, and _voila_: I had a “data-driven presentation, fully mobile responsive, printable, and shareable

[See for yourself](https://abhinemani.com/RAILS/2016/#/): [https://abhinemani.com/RAILS/2016/#/](https://abhinemani.com/RAILS/2016/#//)

Of course, the real benefit came from being able to share that Google Spreadsheet with all 15 organizations recommended for the grants, and the city staff I was collaborating with. Instead of having dozens and dozens of emails filling my inbox with “can you swap this pic for that?” or “our style guide doesn’t recommend use of the ampersand,” I simply shared everyone on the Google docs and let them have at it. I crowdsourced slide “creation” in an open, version-controlled way.

To boot, we now also had a shiny public-facing website for launch, already built, and generally agreed upon copy in an API-accessible format. (Read: this “presentation” basically teed up mostly of everything we might need for ongoing marketing and outreach.)

You can have a look at the code here: [https://github.com/abhinemani/RAILS/tree/gh-pages/2016](https://github.com/abhinemani/RAILS/tree/gh-pages/2016)

Sharing this story isn’t a vanity exercise — this really isn’t terribly clever or good code. No, I’m doing this for that next poor-man’s hacker asked to generate 30 consistent slides with 50 editors.

Have faith, you don’t need to take that baseball bat to your laptop.

At least not until the conference is over :)