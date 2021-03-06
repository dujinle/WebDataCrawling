#-*- coding : utf-8 -*-

import threading,logging,sys,traceback,json
sys.path.append('./crawle_data');
from proxy import Proxy
from crawle_download import CrawleDownload
from tasklist import TaskPool
import config

#-----------logger set-------------#
logfile = 'log.txt';
logger = logging.getLogger();
hdlr = logging.FileHandler(logfile);
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s');
hdlr.setFormatter(formatter);
logger.addHandler(hdlr);
logger.setLevel(logging.NOTSET);

mutex = threading.Lock()
class Crawle(threading.Thread):
	def __init__(self,proxy,task):
		threading.Thread.__init__(self);
		self.task = task;
		self.proxy = proxy;
		self.parse = CrawleDownload(config.base_url);
		self.hits = 0;

	def run(self):
		task = None;
		proxy = self.proxy.get_next_proxy();
		agent = self.proxy.get_next_agent();
		while True:
			if mutex.acquire():
				task = self.task.get_tasks(10);
				mutex.release();
			if task is None:
				break;
			if self.hits >= config.change:
				proxy = self.proxy.get_next_proxy();
				#agent = self.proxy.get_next_agent();
			for tk in task:
				try:
					tt = tk.split('\t');
					if len(tt) >= 1:
						logger.info('task url:' + tt[1] + ' proxy:' + proxy['http']);
						self.parse.begin(tt[1],None);
				except Exception as e:
					print(e)
					logger.error(format(e));
			self.hits += 1;

class CrawleMager:

	def main(self):
		proxy = Proxy();
		task = TaskPool();
		try:
			proxy.load_proxy(config.proxyfile);
			proxy.load_agent(config.agentfile);
			task.load_task(config.taskfile);
			pid = 0;
			while pid < config.pidnum:
				cr = Crawle(proxy,task);
				cr.start();
				pid += 1;
		except Exception as e:
			info = traceback.print_exc();
			logger.error(format(e));
			raise e;
cm = CrawleMager();
cm.main();
