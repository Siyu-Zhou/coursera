#!/usr/bin/env python

import sys
import re
import collections

oldKey = None
NodeCollection = []
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisValue = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}\t{2}".format(oldKey, len(NodeCollection), NodeCollection)
		NodeColLection = []
	oldKey = thisKey
	NodeCollection.append(thisValue)
if oldKey != None:
	print "{0}\t{1}\t{2}".format(oldKey, len(NodeCollection), NodeCollection)
