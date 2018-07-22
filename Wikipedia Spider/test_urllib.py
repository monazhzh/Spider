# import urllib.request
# import http.cookiejar

# url = "http://www.baidu.com"

# print("First method")
# response1 = urllib.request.urlopen(url);
# print(response1.getcode())
# print(len(response1.read()))


# print("Second method")
# request = urllib.request.Request(url)
# request.add_header("use-agent", "Mozilla/5.0")
# response2 = urllib.request.urlopen(request);
# print(response2.getcode())
# print(len(response2.read()))

# print("Third method")
# cj = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# urllib.request.install_opener(opener)
# response3 = urllib.request.urlopen(url)
# print(response3.getcode())
# print(cj)
# print(response3.read())

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print("get all links")
links = soup.find_all('a')
for link in links:
	print(link.name, link['href'], link.get_text())

print("get Lacie link")
link_node = soup.find('a', href = "http://example.com/lacie")
print(link_node.name, link_node['href'], link_node.get_text())


print('regular')
link_node = soup.find('a', href = re.compile(r"ill"))
print(link_node.name, link_node['href'], link_node.get_text())

print('class')
p_node = soup.find('p', class_ = 'title')
print(p_node.name, p_node.get_text())

