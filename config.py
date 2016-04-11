#!/usr/bin/python
#-*- coding :utf-8 -*-

# the proxys file
proxyfile = './data/proxyes.txt';
agentfile = './data/agent.txt';
taskfile = './data/tasklist.txt';

# request n times then change the proxy
change = 3;

# how many thread will be run
pidnum = 10;
# timeout
timeout = 2;

# tag to be load
labels = ['table','.step','.xtieshi'];
