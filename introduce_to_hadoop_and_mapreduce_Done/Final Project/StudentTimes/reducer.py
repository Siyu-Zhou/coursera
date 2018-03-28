#!/usr/bin/python

import sys
hourCount = {}
hourCount = hourCount.fromkeys(range(24),0)
oldKey = None

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue
	if oldKey and oldKey != data[0]:
		maxHour = max(hourCount.values())
		for hourKey, value in hourCount.items():
			if value == maxHour :
				print "{0}\t{1}".format(oldKey, hourKey)
		hourCount = {}
		hourCount = hourCount.fromkeys(range(24),0)
	oldKey = data[0]
	currentHour = int(data[1].split(" ")[1][0:2])
	hourCount[currentHour] += 1
	


if oldKey != None:
	maxHour = max(hourCount.values())
	for hourKey, value in hourCount.items():
		if value == maxHour :
			print "{0}\t{1}".format(oldKey, hourKey)
