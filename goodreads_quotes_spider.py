import urllib
from bs4 import BeautifulSoup
from sys import argv
import bs4
import unicodedata
target = open('goodread_quotes.txt','w')

url = "https://www.goodreads.com/quotes"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('div')
for item in tags:
	text = str(item.get('class'))
	if 'quoteText' in text:				
		for inneritem in item.contents:
			if type(inneritem) == bs4.element.NavigableString:
				target.write(inneritem.encode("utf-8"))
				target.write('\n - ')
				
		target.write(item.a.string)
		target.write('\n \n')
			#try :
			#	print "THIS IS IT\n",inneritem
			#except UnicodeEncodeError:
			#	print str(unicodeData.encode('ascii', 'ignore'))
		#target.write(str(item))
		#target.write('\n \n')
target.close()