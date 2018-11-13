#-*- coding:utf-8 -*-
import sys,bs4,re,urllib3
from bs4 import BeautifulSoup

class CrawleDownload:

	def __init__(self,base_url):
		self.base_url = base_url;

	def get_html_object(self,url,proxy_ip):
		try:
			#proxy like {'http':'http://127.0.0.1:8080'}
			headers = {
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
			}
			if proxy_ip is None:
				http = urllib3.PoolManager();
				r = http.request('get',url,headers = headers)
#				print(r.data.decode())
				return r.data;
			else:
				proxy = urllib3.ProxyManager(proxy_ip,headers = headers)
				r = proxy.request('get',url)
				return r.data;
		except Exception as e:
			raise e;

	def begin(self,url,proxy_ip):
		try:
			doc = self.get_html_object(self.base_url + url,proxy_ip);
			pfile = url[url.rfind("/") + 1:];
			fp = open(pfile,'wb');
			fp.write(doc);
			fp.close();
		except Exception as e:
			raise e;

if __name__ == '__main__':
	pt = CrawleDownload('http://www.xiangqiqipu.com');
	pt.begin('/Uploads/201706/1fcd02a8-6126-4f85-a685-8e94482e5160.png');
