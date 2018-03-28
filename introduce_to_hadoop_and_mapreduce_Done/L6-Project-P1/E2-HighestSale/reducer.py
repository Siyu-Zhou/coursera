#for prject-P1 
#give a sales breakdown by product category across all of our stores
#!/usr/bin/env python
import sys
highsale = 0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	thisSale = float(thisSale)
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, highsale)
		highsale = 0
	oldKey = thisKey
	#if highsale < thisSale:
	#		highsale = thisSale
	highsale = max(highsale, thisSale)

if oldKey != None:
	print "{0}\t{1}".format(oldKey, highsale)


