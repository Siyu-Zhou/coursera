#!/usr/bin/env python
import sys

currentHits = 0
oldKey = None

maxHits = 0
maxhitpath = None

for line in sys.stdin:
	data = line.strip().split()

	if len(data) != 1:
		continue

	thisKey = data
	if oldKey and oldKey != thisKey:
		if maxHits < currentHits:
			maxhitpath = oldKey
			maxHits = currentHits
		currentHits = 0
	oldKey = thisKey
	currentHits += 1


if oldKey != None:
	if maxHits < currentHits:
		maxhitpath = oldKey
		maxHits = currentHits
	print "{0}\t{1}".format(maxhitpath, maxHits)
