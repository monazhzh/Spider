import urllib.parse
from bs4 import BeautifulSoup
import re

class HtmlParser(object):

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href = re.compile(r"/wiki/"))
		for link in links:
			new_url = link['href']
			new_full_url = urllib.parse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, page_url, soup):
		res_data = {}
		res_data['url'] = page_url

		 #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
		 #<h1 id="firstHeading" class="firstHeading" lang="en">Python (programming language)</h1>
		title_node = soup.find('h1', class_ = "firstHeading")
		res_data['title'] = title_node.get_text()

		#<div class="lemma-summary" label-module="lemmaSummary">
		#<p><b>Python</b>
		summary_node = soup.find('p')
		res_data['summary'] = summary_node.get_text()

		return res_data

	
	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data
