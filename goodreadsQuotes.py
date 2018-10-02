import urllib.request
from bs4 import BeautifulSoup
from sys import argv
import bs4
import unicodedata
import re
import json

# search_term = 'fun'
# num_pages = 10


def GoodReadsQuotes(search_term,num_pages):

    file_name = ''+search_term+'_goodread_quotes_'+'.json'
    target = open(file_name,'w')
    url_base = "https://www.goodreads.com"
    url_add = "/quotes/search?q="+search_term+"&"

    old_curr = 0
    curr = 1
    quote =  {}
    while num_pages > 0:
        old_curr = curr
        html = urllib.request.urlopen(''+url_base+url_add).read()
        soup = BeautifulSoup(html,'html.parser')
        print('reading page'+str(curr))

        tags_div = soup('div')
        for item in tags_div:
            text = str(item.get('class'))
            if 'quoteText' in text:
                quote_str = ''
                for inneritem in item.contents:
                    if type(inneritem) == bs4.element.NavigableString:
                        quote_str = quote_str + str(inneritem)

                start = str.index(quote_str,'“')
                end = str.index(quote_str,'”')
                quote_str = quote_str[start+1:end-1]
                if item.a:
                    quote[item.a.text] = quote_str


        tags_a = soup('a')
        for item in tags_a:
            text = str(item.get('class'))
            if 'next_page' in text:
                url_add = str(item['href'])
                num = re.findall('page=([0-9]*)&', url_add)
                curr = int(num[0])
                break
        if curr < old_curr:
            break
        num_pages = num_pages - 1
    target.write(json.dumps(quote))