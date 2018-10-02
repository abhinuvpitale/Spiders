import urllib.request
from bs4 import BeautifulSoup
from sys import argv
import bs4
import unicodedata
import re

url_base = "https://www.theverge.com"
html = urllib.request.urlopen(''+url_base).read()
soup = BeautifulSoup(html,'html.parser')
tags_span = soup('a')
target = open('test.docx','w')

for item in tags_span:
	text = item.get('data-analytics-link')
	if 'article' == text:
		target.write('---------------------------------------------------------------------------------------\n')
		target.write(str(item.text.encode('utf-8')))
		target.write('\n')
