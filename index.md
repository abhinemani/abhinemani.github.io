---
layout: home
permalink: /index.html
title: Home
tagline: When I speak aloud, publicly
tags: [about, Abhi Nemani, Code for America, pandas]
image:
  feature: budget.png
---
<div class="page-wrap author-page">
	<div class="author-header">
		<div class="wrap wrap-center">
			<div class="wrap_float">
				<div class="title-wrap">
					<div class="author-image">
						<img src="{{site.url}}/img/headshot.jpg" alt="" class="image-cover">
					</div>
					<h1 class="page-title">public servant.</h1>
                            </div>
                            <div class="post-description">
								<p>
									Over the last 10+ years, I've been help run and manage various transformational organizations, non-profits, governments, and startups, with an eye towards technology that helps people. I have written, spoken, and taught about my learnings in this emerging, exciting, and fun field of public innovation widely, and try my best here to share what I am seeing.
								</p>
                            </div>
                            <div class="socials">
                                <a class="soc-link">
                                    <img src="{{site.url}}/img/facebook-icon.svg" class="img-svg" alt="">
                                </a>
                                <a class="soc-link" href="https://twitter.com/@abhinemani">
                                    <img src="{{site.url}}/img/twitter-soc-icon.svg" class="img-svg" alt="">
                                </a>
                                <a class="soc-link" href="https://linkedin.com/in/abhinemani">
                                    <img src="{{site.url}}/img/linkedin-icon.png" class="img-svg" alt="">
                                </a>
                                <a class="soc-link" href="https://www.youtube.com/results?search_query=%22abhi+nemani%22">
                                    <img src="{{site.url}}/img/email-icon.png" class="img-svg" alt="">
                                </a>
                                <a class="soc-link" href="https://github.com/abhinemani">
                                    <img src="{{site.url}}/img/github-icon.png" class="img-svg" alt="">
                                </a>
                                <a class="soc-link" href="https://www.youtube.com/results?search_query=%22abhi+nemani%22">
                                    <img src="{{site.url}}/img/youtube-icon.svg" class="img-svg" alt="">
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="author-body">
                    <div class="wrap">
                        <div class="wrap_float">
                            <div class="wp-content">
                                <div class="wrap wrap-center">
                                    <h2>Public Innovation Resources</h2>
                                    <div class="block-columns gallery-columns columns-3 wide-columns lightgallery-off">
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <button class="zoom-btn"></button>
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/academy/resources.html"><img src="{{site.url}}/post-img/home/4.jpg" alt="List of Resources"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <button class="zoom-btn"></button>
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/academy/ecosystem.html"><img src="{{site.url}}/post-img/home/6.jpg" alt="Ecosystem"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <button class="zoom-btn"></button>
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/academy/primer.html"><img src="{{site.url}}/post-img/home/5.jpg" alt="Public Innnovation Primer"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <button class="zoom-btn"></button>
                                                <div class="img-wrap">
                                                    <a href="https://abhinemani.com/civictechcourse/lectures"><img src="{{site.url}}/post-img/home/1.jpg" alt="Lectures"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <button class="zoom-btn"></button>
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/blog.html"><img src="{{site.url}}/post-img/home/2.jpg" alt="Essays"></a>
                                                </div>
	                                         </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <button class="zoom-btn"></button>
                                                <div class="img-wrap">
                                                    <a href="https://govgeek.club"><img src="{{site.url}}/post-img/home/3.jpg" alt="GovGeek Community"></a>
                                                </div>
	                                         </figure>	
                                        </div>
                                    </div>
                                </div>
                            </div>
			                <div class="author-body">
			                    <div class="wrap">
			                        <div class="wrap_float">
			                            <div class="wp-content">
			                                <div class="wrap wrap-center">
			                                    <h2>Featured Essays</h2>
											</div>
										</div>
									</div>
								</div>
							</div>
                            <div class="post-items-list posts-two-columns">
								{% for post in site.posts limit:4 %}	
                                <a href="{{post.url}}" class="post-item">	
									{% if post.img  %}
                                    <img src="{{ site.url}}/post-img/{{post.img}}" alt="" class="post-bg-img">
									{% else %}
                                    <img src="{{ site.url}}/post-img/placeholder.jpg" alt="" class="post-bg-img">
									{% endif  %}
                                    <div class="post-tags">
									  {% if post %}
									    {% assign tags = post.tags %}
									  {% else %}
									    {% assign tags = page.tags %}
									  {% endif %}
									  {% for tag in tags %}
									  <div class="tag">{{ tag }}</div>
									  {% unless forloop.last %}&nbsp;{% endunless %}
									  {% endfor %}
                                    </div>
                                    <h3 class="post-title">
                                        {{ post.title }}
                                    </h3>
                                    <div class="post-info">
                                        <div class="post-author post-info-author">
                                            <div class="author-image">
                                                <img src="{{site.url}}/img/headshot.png" alt="" class="image-cover">
                                            </div>
                                            <span>Abhi Nemani</span>
                                        </div>
                                        <div class="post-date post-info-date">
                                            {{ post.pubdate }}
                                        </div>
                                    </div>
                                </a>
								{% endfor %}
                            </div>
                            <div>
								<a href="{{site.url}}/blog.html">
                                <div class="show-more-btn">
                                    <span>Read more...</span>
                                </div>
								</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>