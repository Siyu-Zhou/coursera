#!/usr/bin/python

import sys
tagDict={}

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 1:
		continue
	tag = data[0]
	if tagDict.has_key(tag):
		tagDict[tag] += 1
	else:
		tagDict[tag] = 1
top10 = sorted(tagDict, key = lambda x : tagDict[x], reverse=True)[0:10]
for line in top10:
	print "{0}\t{1}".format(line,tagDict[line])
