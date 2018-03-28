#!/usr/bin/python

import sys
IdDict = {}
oldKey = None
for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue
	
	if oldKey and oldKey != data[0]:
		print "{0}\t{1}".format(oldKey,IdDict[oldKey])
		IdDict={}

	oldKey = data[0]
	authorId = data[1]
	if IdDict.has_key(oldKey):
		IdDict[oldKey].append(authorId)
	else:
		IdDict[oldKey] = []
		IdDict[oldKey].append(authorId)
if oldKey != None:
	print "{0}\t{1}".format(oldKey,IdDict[oldKey])