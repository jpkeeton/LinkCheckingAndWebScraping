import requests
import lxml.html

# This code is from: https://data-lessons.github.io/library-webscraping-DEPRECATED/04-lxml/

# response = requests.get('http://www.un.org/en/sc/documents/resolutions/2016.shtml')
response = requests.get('http://www.cnn.com')
tree = lxml.html.fromstring(response.text)
title_elem = tree.xpath('//title')[0]
# title_elem = tree.cssselect('title')[0]  # equivalent to previous XPath
print("title tag:", title_elem.tag)
print("title text:", title_elem.text_content())
print("title html:", lxml.html.tostring(title_elem))
print("title tag:", title_elem.tag)
print("title's parent's tag:", title_elem.getparent().tag)


