---
layout: home2
permalink: /index.html
title: Abhi Nemani
subhead: public servant. Fmr Chief Data Officer, Los Angeles, Chief Innovation Officer, Sacramento, Code for America.
tags: [about, Abhi Nemani, Code for America, pandas]
img: main-social.jpg
---
<section class="banner-section" style="background-image: url(../img/GD-shot.jpg);">
	<div class="wrap wrap-center ">
		<div class="wrap_float">
			<div class="section-content">
				<div class="location">public servant. fmr #localgov CDO/CIO; #civictech @UChicago; @codeforamerica</div>
				<h2 class="page-title">
					Showing What's Possible in Government through Technology
				 </h2>
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
					 <div class="buttons">
					 <a href="/blog" class="btn"><span>Latest Stories</span></a>
					 <a href="/about" class="btn border-btn"><span>About me</span></a>
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
					<h2><a href="/academy"><img src="{{site.url}}/img/PIA-logo.png" style="margin: 10px auto 0px auto; max-width: 300px;"></a></h2>
					<div class="block-columns gallery-columns columns-3 wide-columns lightgallery-off">
						<div class="block-column">
							<figure class="block-caption img-caption">
								<div class="img-wrap">
									<a href="{{site.url}}/academy/">
										<img src="{{site.url}}/img/home/2.jpg" alt="Lessons">
									</a>
								</div>
							</figure>
						</div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/lessons/primer/"><img src="{{site.url}}/img/home/1.jpg" alt="Primer"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/lessons/ecosystem/"><img src="{{site.url}}/img/home/3.jpg" alt="Ecosystem"></a>
                                                </div>
                                            </figure>
                                        </div>
                                        <div class="block-column">
                                            <figure class="block-caption img-caption">
                                                <div class="img-wrap">
                                                    <a href="{{site.url}}/community"><img src="{{site.url}}/img/home/4.jpg" alt="Community"></a>
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
                                                    <a href="{{site.url}}/resources/"><img src="{{site.url}}/img/home/6.jpg" alt="Resources"></a>
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
                                    <span>More Essays & News</span>
                                </div>
								</a>
                            </div>
                        </div>
                    </div>
	                <div class="author-body">
	                    <div class="wrap">
	                        <div class="wrap_float">
	                            <div class="wp-content">
	                                <div class="wrap wrap-center">
										<h2>In the News</h2>
										<div class="block-columns gallery-columns columns-4">
											{% for press in site.press limit:8 %}  
											<div class="block-column">
												<figure class="block-caption img-caption">
													<div class="img-wrap">
														<a href="{{ press.url }}"><img src="{{site.url}}/img/{{ press.image.thumb }}" alt=""></a>
													</div>
													<figcaption class="caption-text">{{ press.title }}</figcaption>
												</figure>
											</div>
											{% endfor %}
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
                </div>
