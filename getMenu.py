import requests, json
from xml.etree.ElementTree import fromstring
from xmljson import parker, Parker

burtonWebpage = requests.get("https://carleton.cafebonappetit.com/cafe/burton/")

#burtonJson = json.dumps(parker.data(fromstring(str(burtonWebpage.text))))
burtonHtml = burtonWebpage.text

endCutOff = '''<section class="panel s-wrapper site-panel site-panel--dietary_preferences"
				id="icons"
				data-index="13"
				data-js="panel"
				data-type="dietary_preferences"
									data-jump-nav-title="Icons"
					data-url-key="icons"
								data-modular-content>
	
			<div class="l-container">'''
endCutOffIndex = burtonHtml.index(endCutOff)
trimmedHtml = burtonHtml[0:endCutOffIndex]
print(trimmedHtml)
frontCutOff = '''<script>
			(function() {
				Bamco = (typeof Bamco !== "undefined") ? Bamco : {};
				Bamco.api_url = {
					items: 'https://legacy.cafebonappetit.com/api/2/items?format=jsonp',
					cafes: 'https://legacy.cafebonappetit.com/api/2/cafes?format=jsonp',
					menus: 'https://legacy.cafebonappetit.com/api/2/menus?format=jsonp'
				};
				Bamco.current_cafe = {
					name: 'Burton',
					id: 244				};
				Bamco.view_tier = 1;'''
#frontCutOffIndex = trimmedHtml.index(frontCutOff)
#trimmedHtml = trimmedHtml[frontCutOffIndex::]


print(trimmedHtml)

# What we need to extract:
# Is it open or closed
# Each category
# Within each category, every menu item in it