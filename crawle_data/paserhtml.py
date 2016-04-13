#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
reload(sys);
sys.setdefaultencoding('utf-8');

import bs4
import re
from bs4 import BeautifulSoup
import urllib2
import json
import collections

class PaserHtml:

	def __init__(self):
		self.key = None;
		self.data = collections.OrderedDict();

	def get_html_object(self,url,proxy,agent,timeout):
		try:
			#proxy like {'http':'http://127.0.0.1:8080'}
			proxy_support = urllib2.ProxyHandler(proxy);
			opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler);
			urllib2.install_opener(opener);
			request = urllib2.Request(url);
			#agent like 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
			request.add_header('User-Agent',agent);
			urlopen = urllib2.urlopen(request,timeout = timeout);
			html = urlopen.read();
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
					if label == 'table':
						self.paser_table(tt,None);
						continue;
					self.looptag(tt);
		except Exception as e:
			print e;
	def paser_table(self,doc,tags):
		body = doc.tbody;
		for cont in body.contents:
			if cont.name == 'tr':
				tds = cont.contents;
				for td in tds:
					self.key = None;
					self.looptdtag(td,None);

	def looptdtag(self,td,key):
		if type(td) == bs4.element.Tag:
			tcont = td.contents;
			for tchild in tcont:
				self.looptdtag(tchild,key);
		elif type(td) == bs4.element.NavigableString:
			td = self.delstr(td,'\n');
			td = self.delstr(td,'\t');
			td = self.delstr(td,' ');
			if len(td) > 0:
				if self.key is None:
					self.key = td;
					self.data[self.key] = '';
				else:
					self.data[self.key] = td;

	def looptag(self,tag):
		if tag.name == 'img':
			self.data[tag.attrs['alt']] = tag.attrs['original'];
		elif type(tag) == bs4.element.Tag:
			conts = tag.contents;
			for it in conts:
				self.looptag(it);
		elif type(tag) == bs4.element.NavigableString:
			data = self.delstr(tag,u'\n');
			#data = self.delstr(data,u' ');
			if len(data) > 0:
				if not self.data.has_key('strs'):
					self.data['strs'] = list();
				self.data['strs'].append(data);

	def delstr(self,strs,diem):
		while strs.find(diem) != -1:
			strs = strs.replace(diem,'');
		return strs;

	def begin(self,url,proxy,agent,labels,timeout):
		try:
			doc = self.get_html_object(url,proxy,agent,timeout);
			self.paser_html(doc,labels);
		except Exception as e:
			raise e;

#pth = PaserHtml();
#pth.begin('http://www.douguo.com/cookbook/1355539.html',None,None,['table','.step','.xtieshi'],10);
#print json.dumps(pth.data,indent = 2,ensure_ascii = False);
