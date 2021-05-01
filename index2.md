---
layout: home2
permalink: /alpha/
title: Home
subhead: public servant. Fmr Chief Data Officer, Los Angeles, Chief Innovation Officer, Sacramento, Code for America.
tags: [about, Abhi Nemani, Code for America, pandas]
img: placeholder.jpg
---
<section class="banner-section" style="background-image: url(../img/tour-banner.jpg);">
	<div class="wrap wrap-center ">
		<div class="wrap_float">
			<div class="section-content">
				<div class="location">public innovation.</div>
				<h2 class="page-title">
					 I'm a fan of technology, government, and interesting ideas.
				 </h2>
				 <p class="subtitle">
					 Canoeing in Canada from $500
				 </p>
				 <div class="buttons">
					 <a data-href="#book-now" class="btn getModal"><span>Book Now</span></a>
					 <a href="tour-list-fullwidth.html" class="btn border-btn"><span>Choose tour</span></a>
				 </div>
			 </div>
		 </div>
	</div>
</section>
<div class="author-body">
	<div class="wrap">
		<div class="wrap_float">
			<div class="wp-content">
				<div class="wrap wrap-center">
					<h2>Public Innovation Academy</h2>
					<div class="block-columns gallery-columns columns-3 wide-columns lightgallery-off">
						<div class="block-column">
							<figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/academy/"><img src="{{site.url}}/img/home/2.jpg" alt="Lessons"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/lessons/1-primer/"><img src="{{site.url}}/img/home/1.jpg" alt="Primer"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/lessons/2-ecosystem/"><img src="{{site.url}}/img/home/3.jpg" alt="Ecosystem"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="https://govgeek.club"><img src="{{site.url}}/img/home/4.jpg" alt="Community"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/blog/"><img src="{{site.url}}/img/home/5.jpg" alt="Essays"></a>
                                                </div>
	                                         </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/lessons/4-resources/"><img src="{{site.url}}/img/home/6.jpg" alt="Resources"></a>
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
								{% for post in site.categories.Essays limit:4 %}	
                                <a href="{{post.url}}" class="post-item">	
									{% if post.img  %}
                                    <img src="{{ site.url}}/img/{{post.img}}" alt="" class="post-bg-img">
									{% else %}
                                    <img src="{{ site.url}}/img/placeholder.jpg" alt="" class="post-bg-img">
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
                                                <img src="{{site.url}}/img/headshot.jpg" alt="" class="image-cover">
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
								<a href="{{site.url}}/blog/">
                                <div class="show-more-btn">
                                    <span>Read more...</span>
                                </div>
								</a>
                            </div>
                        </div>
                    </div>
                </div>