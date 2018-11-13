#-*- coding:utf-8 -*-
import sys,bs4,re,urllib3
from bs4 import BeautifulSoup

class ParseTask:

	def __init__(self):
		self.data = dict();

	def get_html_object(self,url,proxy_ip,agent):
		try:
			#proxy like {'http':'http://127.0.0.1:8080'}
			headers = {
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
			}
			if proxy_ip is None:
				http = urllib3.PoolManager();
				r = http.request('get',url,headers = headers)
#				print(r.data.decode())
				doc = BeautifulSoup(r.data.decode(),'html5lib');
#				print(doc);
				return doc;
			else:
				proxy = urllib3.ProxyManager(proxy_ip,headers = headers)
				r = proxy.request('get',url)
				doc = BeautifulSoup(r.data.decode(),'html5lib');
#				print(doc);
				return doc;
			'''
			proxy_support = urllib3.ProxyHandler(proxy);
			opener = urllib3.build_opener(proxy_support,urllib3.HTTPHandler);
			urllib3.install_opener(opener);
			request = urllib3.Request(url);
			#agent like 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
			request.add_header('User-Agent',agent);
			html = urllib3.urlopen(request).read();
			doc = BeautifulSoup(html);
			return doc;
			'''
		except Exception as e:
			raise e;

	#解析html内容
	def parse_html(self,doc,tags):
		try:
			if len(self.data) > 0:
				self.data.clear();
			for label in tags:
				tag = doc.select(label);
				for tt in tag:
					self.looptag(tt);
		except Exception as e: raise e;

	def looptag(self,tag):
		if tag.name == 'img':
			attrs = tag.attrs;
			if 'src' in attrs and 'alt' in attrs:
				self.data[attrs['alt']] = attrs['src'];

	def begin(self,url,proxy,agent,labels,fp):
		try:
			doc = self.get_html_object(url,proxy,agent);
			self.parse_html(doc,labels);
			for key in self.data.keys():
				fp.write(key + '\t' + self.data[key] + '\n');
		except Exception as e:
			raise e;
'''
if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('Usage:%s outfile' %sys.argv[0]);
		sys.exit(-1);
	pfile = sys.argv[1];
	pt = PaserTask();
	pt.begin('http://www.xiangqiqipu.com/Category/List-102-1.html',
		None,None,['img'],
		pfile
	);
'''
