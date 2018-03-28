#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
salesNumber = 0
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print "weekday:{0}, mean sale{1}".format(oldKey,float(salesTotal/salesNumber))
		salesTotal = 0
		salesNumber = 0
	oldKey = thisKey
	salesTotal += float(thisSale)
	salesNumber += 1

if oldKey != None:
	print "weekday:{0}, mean sale{1}".format(oldKey,float(salesTotal/salesNumber))