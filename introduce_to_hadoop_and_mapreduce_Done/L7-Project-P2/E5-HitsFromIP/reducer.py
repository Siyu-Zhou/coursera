#!/usr/bin/env python
import sys

TotalHits = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split()

	if len(data) != 1:
		continue

	thisKey = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, TotalHits)
		TotalHits = 0
	oldKey = thisKey
	TotalHits += 1
if oldKey != None:
	print "{0}\t{1}".format(oldKey, TotalHits)
