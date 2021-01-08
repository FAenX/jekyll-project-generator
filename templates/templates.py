from string import Template

index_template = Template(
'''---
layout: default
title: title
headline: software development company
---


{% include index.html %}


''')

gemfile = Template('''
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll"
''')


config = Template('''
url: $URL
title: $TITLE

plugins:
  - jekyll-seo-tag
  - jekyll-sitemap


exclude:
  - Gemfile
  - Gemfile.lock
  - README.md
  - LICENCE

''')


include_html = Template('''
<section class="hero is-fullheight" id="hero">

		<img class="animate-on-visibility background" alt="" src="{{ site.baseurl }}/assets/images/img2.jpg">
		
				
		{% include navigation.html %}
		
		
		
		<div class="hero-body pt-6">	
			<div class="container">		
				<div class="columns">
					<div class="column pr-6">
						<div class="animate__animated animate__bounce text-right">
							<h2 class="is-size-2">{ {{ page.herotitle }} }
								<span class="has-text-weight-bold is-purple">{{ page.herominititle }}</span>
								<span class="has-text-weight-bold is-orange">.</span>
								<br>
								{{ page.headline }}
							</h2>						
							
							<br> Nairobi </p> 
							<a class="button is-rounded btn-banner mt-6 has-text-white-ter">
								Learn more
							</a>
						</div>
					</div>
				</div>
			</div>		
		</div>
	
</section>

''')


default_layout = Template('''
<!DOCTYPE html>
<html>
  <head>
    {% seo %}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/scss/main.css">
	  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
  </head>
  <body>
    {{ content }}



    <script async src='{{ site.baseurl }}/assets/js/index.js'></script>
	<script defer src="https://use.fontawesome.com/releases/v5.14.0/js/all.js"></script>
  </body>
</html>

''')
