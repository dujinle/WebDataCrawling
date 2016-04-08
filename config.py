#!/usr/bin/python
#-*- coding :utf-8 -*-
###代理的文件
proxyfile = "./data/proxyes.txt";
agentfile = "./data/agent.txt";

### n次请求之后更换一次代理
change = 3;
###最多提取n层节点
maxlink = 3;

####每层节点规则参数
tag = {
	'1':['li'],
	'2':['table'],
	'3':'null'
};
