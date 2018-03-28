#for prject-P1 
#give a sales breakdown by product category across all of our stores
import sys
salesTotal = 0
salesnumber =0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}\t{2}".format(oldKey, salesTotal, salesnumber)
		salesTotal = 0
		salesnumber = 0
	oldKey = thisKey
	salesTotal += float(thisSale)
	salesnumber += 1

if oldKey != None:
	print "{0}\t{1}\t{2}".format(oldKey, salesTotal, salesnumber)


