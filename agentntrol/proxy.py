#!/usr/bin/python
#-*- coding:utf-8 -*-

class Proxy:
	def __init___(self):
		self.proxys = dict;
		self.agents = dict;

	def load_proxy(self,pf):
		try:
			fd = open(pf,'r');
			self.proxys['proxy'] = fd.readlines();
			self.proxys['step'] = 0;
			self.proxys['total_num'] = len(self.proxys['proxy']);
			fd.close();
		except Exception as e:
			raise e;
	def load_agent(self,pa):
		try:
			fd = open(pa,'r');
			self.agents['agent'] = fd.readlines();
			self.agents['step'] = 0;
			self.agents['total_num'] = len(self.agents['agent']);
			fd.close();
		except Exception as e:
			raise e;

	def get_next_proxy(self):
		proxy = self.proxys['proxy'];
		step = self.proxys['step'];
		total_num = self.proxys['total_num'];
		if step >= total_num:
			self.proxys['step'] = 0;
			step = 0;
		return proxy[step];

	def get_next_agent(self):
		agent = self.agents['agent'];
		step = self.agents['step'];
		total_num = self.agents['total_num'];
		if step >= total_num:
			self.agents['step'] = 0;
			step = 0;
		return agent[step];
