#!/usr/bin/python
#-*- coding:utf-8 -*-
import bs4
import re
from bs4 import BeautifulSoup
import urllib2

class PaserHtml:

	def __init__(self):
		self.data = dict;

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
			self.data.clear();
			for label in tags:
				tag = doc.select(label);
				if label[0] == '\.':
					tag = doc.find_all(class_ = re.compile(label[1:]));
				elif label[0] == '\#':
					tag = doc.find_all(id = re.compile(label[1:]));
				for tt in tag:
					self.looptag(tt);
		except Exception as e:
			print e;

	def looptag(self,tag):
		if tag.name == 'img':
			self.data[tag.attrs['alt']] = tag.attrs['original'];
		elif type(tag) == bs4.element.Tag:
			conts = tag.contents;
			for it in conts:
				self.looptag(it);
		elif type(tag) == bs4.element.NavigableString:
			data = self.delstr(tag,u'\n');
			data = self.delstr(data,u' ');
			if len(data) > 0:
				if not self.data.has_key('strs'):
					self.data['strs'] = list;
				self.data.append(data);

	def delstr(self,strs,diem):
		while strs.find(diem) != -1:
			strs = strs.replace(diem,'');
		return strs;

ph = PaserHtml();
doc = ph.get_html_object(
		'http://www.douguo.com/cookbook/190520.html',
		None,None
	);
ph.paser_html(doc,['table','.step']);
