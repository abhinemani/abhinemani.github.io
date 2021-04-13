---
layout: home
permalink: /search/index.html
title: Search
tagline: Search site
tags: [about, Abhi Nemani, Code for America, pandas]
---
<div class="page-wrap author-page">
    <div class="breadcrumbs">
        <div class="wrap wrap-center">
            <div class="wrap_float">
                <a href="index.html">Home</a> / <span class="current">Search</span>
            </div>
        </div>
    </div>
    <div class="author-header">
        <div class="wrap wrap-center">
            <div class="wrap_float">
                <div class="section-content wp-content">
					<h2>Search</h2>
					<div id="search">
						<input type="text" class="search" id="search-input" placeholder="search...">
					<ul id="results-container"></ul>
					</div>
					<script src="{{site.url}}/js/search-script.js" type="text/javascript"></script>
					<script>
					SimpleJekyllSearch({
					  searchInput: document.getElementById('search-input'),
					  resultsContainer: document.getElementById('results-container'),
					  json: '{{site.url}}/search.json'
					})
					</script>
                </div>
            </div>
        </div>
    </div>