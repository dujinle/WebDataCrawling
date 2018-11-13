#-*- coding:utf-8 -*-
#虚拟代理管理器
class Proxy:
	def __init__(self):
		self.proxys = dict();
		self.agents = dict();

	def load_proxy(self,pf):
		try:
			fd = open(pf,'r');
			while True:
				line = fd.readline();
				if not line:
					break;
				if not 'total_num' in self.proxys:
					self.proxys['total_num'] = 0;
				self.proxys['total_num'] += 1;
				if not 'proxy' in self.proxys:
					self.proxys['proxy'] = list();
				self.proxys['proxy'].append(line.strip('\n'));
			self.proxys['step'] = 0;
			fd.close();
		except Exception as e:
			raise e;
	def load_agent(self,pa):
		try:
			fd = open(pa,'r');
			while True:
				line = fd.readline();
				if not line:
					break;
				if not 'total_num' in self.agents:
					self.agents['total_num'] = 0;
				self.agents['total_num'] += 1;
				if not 'agent' in self.agents:
					self.agents['agent'] = list();
				self.agents['agent'].append(line.strip('\n'));
			self.agents['step'] = 0;
			fd.close();
		except Exception as e:
			raise e;

	def get_next_proxy(self):
		prox = dict();
		proxy = self.proxys['proxy'];
		step = self.proxys['step'];
		total_num = self.proxys['total_num'];
		if step >= total_num:
			self.proxys['step'] = 0;
			step = 0;
		prox['http'] = proxy[step];
		return prox;

	def get_next_agent(self):
		agent = self.agents['agent'];
		step = self.agents['step'];
		total_num = self.agents['total_num'];
		if step >= total_num:
			self.agents['step'] = 0;
			step = 0;
		return agent[step];
