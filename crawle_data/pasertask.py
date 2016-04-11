#!/usr/bin/python
#-*- coding:utf-8 -*-
import bs4
import re
from bs4 import BeautifulSoup
import urllib2
import sys
reload(sys);
sys.setdefaultencoding('utf-8');

class PaserTask:

	def __init__(self):
		self.data = dict();

	def get_html_object(self,url,proxy,agent):
		try:
			#proxy like {'http':'http://127.0.0.1:8080'}
			proxy_support = urllib2.ProxyHandler(proxy);
			opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler);
			urllib2.install_opener(opener);
			request = urllib2.Request(url);
			#agent like 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
			request.add_header('User-Agent',agent);
			html = urllib2.urlopen(request).read();
			doc = BeautifulSoup(html);
			return doc;
		except Exception as e:
			raise e;

	def paser_html(self,doc,tags):
		try:
			if len(self.data) > 0:
				self.data.clear();
			for label in tags:
				tag = doc.select(label);
				for tt in tag:
					self.looptag(tt);
		except Exception as e:
			print e;

	def looptag(self,tag):
		if tag.name == 'a':
			attrs = tag.attrs;
			if attrs.has_key('href') and attrs.has_key('title'):
				self.data[attrs['title']] = attrs['href'];
		elif type(tag) == bs4.element.Tag:
			conts = tag.contents;
			for it in conts:
				self.looptag(it);

	def begin(self,url,proxy,agent,labels,pfile):
		try:
			doc = self.get_html_object(url,proxy,agent);
			self.paser_html(doc,labels);
			fp = open(pfile,'w');
			for key in self.data.keys():
				fp.write(key + '\t' + self.data[key] + '\n');
			fp.close();
		except Exception as e:
			raise e;
if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'Usage:%s outfile' %sys.argv[0];
		sys.exit(-1);
	pfile = sys.argv[1];
	pt = PaserTask();
	pt.begin('http://www.douguo.com/allrecipes',
		None,None,['a[target="_blank"]'],
		pfile
	);
