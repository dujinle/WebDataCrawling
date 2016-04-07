#!/usr/bin/python
#-*- coding:utf-8 -*-
class Proxy:
	def __init___(self):
		self.proxys = None;
		self.step = 0;
		self.total_num = 0;

	def load_proxy(self,pf):
		try:
			fd = open(pf,'r');
			if self.proxys is None:
				self.proxys = fd.readlines();
				self.total_num = len(self.proxys);
		except Exception as e:
			raise e;
	def get_next_proxy(self):
		if self.step >= self.total_num:
			self.step = 0;
		return self.proxys[self.step];

