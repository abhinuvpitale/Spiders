import urllib
from bs4 import BeautifulSoup
from sys import argv
import bs4
import unicodedata
import re

def getSearchTerm():
	print('Enter your search term - ')
	search_term = input()
	return search_term

def getPageCount():
	MAX = 10000
	print('Enter number of pages to find (-1 for all) - ')
	num_pages = input()
	if num_pages == -1:
		return MAX
	return int(num_pages)

def initGoodreadSpider(term):
	global target
	global url_base
	fileName = ''+term+'_goodread_quotes_'+'.txt'
	target = open(fileName,'w')
	url_base = "https://www.goodreads.com"

def printQuote():
	global target
	global soup
	tags_div = soup('div')
	for item in tags_div:
		text = str(item.get('class'))
		if 'quoteText' in text:				
			for inneritem in item.contents:
				if type(inneritem) == bs4.element.NavigableString:
					target.write(inneritem.encode("utf-8"))
					
			target.write('\n - ')
			target.write(item.a.text.encode("utf-8"))		
			target.write('\n \n')
			
			
def nextPage():
	global soup
	tags_a = soup('a')
	for item in tags_a:
		text = str(item.get('class'))
		if 'next_page' in text:	
			url_add = str(item['href'])
			num = re.findall('page=([0-9]*)&',url_add)
			curr = int(num[0])
			return curr,url_add

#Main Begins

if __name__ == '__main__':
	search_term = getSearchTerm()
	num_pages = getPageCount()
	initGoodreadSpider(search_term)

	url_add = "/quotes/search?q="+search_term+"&"

	old_curr = 0
	curr = 1

	while 1:
		old_curr = curr

		html = urllib.request.urlopen(''+url_base+url_add).read()
		soup = BeautifulSoup(html,'html.parser')
		pageNoText = str(curr)
		pageNoText = '-------------------PAGE'+pageNoText+'-------------------'
		target.write('\n\n\n')
		target.write(pageNoText)
		target.write('\n\n\n')
		printQuote()

		curr,url_add = nextPage()

		if curr>=num_pages:
			break

		if curr<old_curr:
			break

	target.close()
