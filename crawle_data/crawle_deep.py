#-*- coding:utf-8 -*-
import sys,bs4,re,urllib3
from bs4 import BeautifulSoup
from crawle_tasklist import ParseTask

class CrawleDeep:

	def __init__(self,base_url,proxy_ip,labels,parse_task):
		self.data = list();
		self.base_url = base_url;
		self.proxy_ip = proxy_ip;
		self.labels = labels;
		self.parse_task = parse_task;

	def get_html_object(self,url):
		try:
			#proxy like {'http':'http://127.0.0.1:8080'}
			headers = {
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
			}
			if self.proxy_ip is None:
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
	def parse_html(self,doc):
		try:
			for label in self.labels:
				tag = doc.select(label);
				for tt in tag:
					self.looptag(tt);
		except Exception as e: raise e;

	def looptag(self,tag):
		if tag.name == 'a':
			attrs = tag.attrs;
			if 'href' in attrs and 'rel' in attrs:
				if attrs['rel'].pop() == 'next':
					url = self.base_url + attrs['href'];
					self.data.append(url);
					doc = self.get_html_object(url);
					self.parse_html(doc);

	def begin(self,url,pfile):
		try:
			self.data.append(url);
			doc = self.get_html_object(url);
			self.parse_html(doc);
			fp = open(pfile,'w');
			for key in self.data:
				self.parse_task.begin(key,self.proxy_ip,None,['img'],fp)
			fp.close();
		except Exception as e:
			raise e;

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('Usage:%s outfile' %sys.argv[0]);
		sys.exit(-1);
	pfile = sys.argv[1];
	pt = CrawleDeep('http://www.xiangqiqipu.com',None,['a'],ParseTask());
	pt.begin('http://www.xiangqiqipu.com/Category/List-102-1.html',
		pfile
	);
