---
layout: home2
permalink: /cal/
title: Calendar
tagline: Schedule some time
tags: [about, Abhi Nemani, Code for America, pandas]
---
<section class="banner-section" style="background-image: url({{site.url}}/img/ethos-back.jpg); max-height: 400px;">
	<div class="wrap wrap-center ">
		<div class="wrap_float" style="min-height: 400px; padding: 100px 0 0 0;">
			<div class="section-content">
				<h2 class="page-title">
					Scheduling
				</h2>
				<p class="subtitle" style="color: white; line-height: 1.3em;">
					Use the form below to find a convenient time.
				</p>
				<div class="socials">
					<a class="soc-link" href="https://twitter.com/@abhinemani">
						<img src="{{site.url}}/img/twitter-soc-icon.svg" class="img-svg" alt="">
					</a>
					<a class="soc-link" href="https://linkedin.com/in/abhinemani">
						<img src="{{site.url}}/img/linkedin-icon.png" class="img-svg" alt="">
					</a>
					<a class="soc-link" href="mailto:abhi.nemani@gmail.com">
						<img src="{{site.url}}/img/email-icon.png" class="img-svg" alt="">
					</a>
					<a class="soc-link" href="https://github.com/abhinemani">
						<img src="{{site.url}}/img/github-icon.png" class="img-svg" alt="">
					</a>
				</div>
			</div>
		</div>
	</div>
</section>

<div class="page-wrap archive-page with-sidebar">
	<div class="archive-body">
		<div class="wrap">
			<div class="page-wrap-content">
				<div class="section-content wp-content">
					<div style="height: 100vh;">
						<!-- Cal inline embed code begins -->
<div style="width:100%;height:100%;overflow:scroll" id="my-cal-inline"></div>
<script type="text/javascript">
  (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if(typeof namespace === "string"){cal.ns[namespace] = cal.ns[namespace] || api;p(cal.ns[namespace], ar);p(cal, ["initNamespace", namespace]);} else p(cal, ar); return;} p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
Cal("init", "30min", {origin:"https://cal.com"});

  Cal.ns["30min"]("inline", {
    elementOrSelector:"#my-cal-inline",
    config: {"layout":"month_view"},
    calLink: "abhinemani/30min",
  });

  Cal.ns["30min"]("ui", {"hideEventTypeDetails":false,"layout":"month_view"});
  </script>
  <!-- Cal inline embed code ends -->
					</div>
			   </div>
			 </div>
			<div class="page-wrap-sidebar">
				<div class="sidebar-item subscribe-widget">
					<script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
<div class="elfsight-app-46eaba72-8498-4ea1-ae9b-7773d84c1ac4"></div>
				</div>				
			</div>
		</div>
	</div>
</div>