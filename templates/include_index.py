from string import Template


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