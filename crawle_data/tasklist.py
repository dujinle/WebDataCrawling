#-*- coding:utf-8 -*-

class TaskPool:
	def __init__(self):
		self.task = list();
		self.task_id = 0;
		self.task_num = 0;

	def load_task(self,tfile):
		try:
			fp = open(tfile,'r');
			while True:
				line = fp.readline();
				if not line: break;
				self.task.append(line.strip('\n'));
				self.task_num += 1;
		except Exception as e: raise e;

	#return n tasks
	def get_tasks(self,n):
		tid = self.task_id;
		tnum = self.task_num;
		if tid >= tnum:
			return None;
		if tid + n >= tnum:
			self.task_id = tnum;
			return self.task[tid:];
		self.task_id += n;
		return self.task[tid:tid + n - 1];
