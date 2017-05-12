from bs4 import BeautifulSoup
import urllib
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wk = xlsxwriter.Workbook('proflist.xlsx')
ws = wk.add_worksheet()

file = 'prof_list.txt'
target = open(file,'w')
url_base = "https://www.ece.vt.edu/people/faculty"
html = urllib.urlopen(''+url_base).read()
soup = BeautifulSoup(html,'html.parser')

tags_a = soup('a')
links = []
for item in tags_a:
	link =  str(item.get('href'))
	if 'profile' in link:
		links.append(link)
	#target.write(item['href'].encode("utf-8"))
	#target.write('\n')
	#target.write('\n')
	
i=0;
j=0;

print len(links)	
for link in links:
	url = link
	html_basic = urllib.urlopen(''+url).read()
	soup_basic = BeautifulSoup(html_basic,'html.parser')
	tags_p = soup_basic('p')	
	ws.write(i,j,link.encode("utf-8"))
	j = j + 1;

	for item in tags_p:	
		if item.get('class') is not None:
			if 'sidepd-20' in str(item.get('class')[0]):
				ws.write(i,j,item.text.encode("utf-8"))
				j = j+1
				
	i =i + 1
	j = 0
	print i
	
	
		#	for inneritem in item:
		#		target.write(inneritem.encode('utf-8'))
		#		target.write('-------------------\n--------------------')
		#if 'person-key-info' in str(item.get('class')[0]):
		#	print item

'''		
for item in links:
	url = item
	html_basic = urllib.urlopen(''+url).read()
	soup_basic = BeautifulSoup(html_basic,'html.parser')
	tags_p = soup('p')
	target.write(item)
	target.write('\n \n')
	target.write('------------------------------------------------------')
	target.write(item)
	for inneritem in tags_p:
		target.write(inneritem.encode('utf-8'))
		target.write('\n')
	target.write('\n \n \n \n \n
'''	
wk.close()
target.close()
