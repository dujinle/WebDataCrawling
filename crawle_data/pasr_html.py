#!/usr/bin/python
#-*- coding:utf-8 -*-
import BeautifulSoup
import urllib2
class PaserHtml:
	def __init__(self):
		self.handle = BeautifulSoup;
		self.config = None;

	def load_conf(self,config):
		try:
			fd = open(config,'r');
			self.config = fd.readlines();
		except Exception as e:
			raise e;

	def paser_html(self,url,proxy,agent):
		try:
			#proxy like {'http':'127.0.0.1:8080'}
			proxy_support = urllib2.ProxyHandler(proxy);
			opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler);
			urllib2.install_opener(opener);
			request = urllib2.Request(url);
			#agent like 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
			request.add_header('User-Agent',agent);
			html = urllib2.urlopen(request).read();
			doc = self.handle(html);
			print doc;
		except Exception as e:
			raise e;

ph = PaserHtml();
ph.paser_html(
		'http://www.douguo.com/allrecipes',
		{'http':'127.0.0.1:8080'},
		'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
	);

