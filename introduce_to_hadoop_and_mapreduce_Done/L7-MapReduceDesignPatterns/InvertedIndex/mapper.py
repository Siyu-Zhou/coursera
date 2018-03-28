#!/usr/bin/env python
import sys
import re
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
delimiters = ['.',',','$',';','!','?',':','"','(',')','[',']','<','>','#','=','-','/',' ']
regexPattern = '|'.join(map(re.escape, delimiters))
for line in reader:
	#check whether in the first line(title)
	nodeId = line[0]
	if nodeId == 'id':
		continue
	#check whether nodeId is empty
	if len(nodeId) == 0:
		nodeId = 'NA'
	body = line[4]
	if len(line[4]) == 0 :
		body = 'NA'
	body = re.split(regexPattern,body)
	for word in body:
		print "{0}\t{1}".format(word.lower(), nodeId)
	

