#for prject-P1 
#not for different store, just select highest sales in all stores
import sys
salesTotal = 0
salesnumber =0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	salesTotal += float(thisSale)
	salesnumber += 1


print "{0}\t{1}\t{2}".format(oldKey, salesTotal, salesnumber)


