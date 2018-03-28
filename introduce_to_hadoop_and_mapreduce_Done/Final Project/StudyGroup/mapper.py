#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0] == 'id':
		continue 
	if len(line) != 19:
		continue
	authorId = line[3]
	nodeType = line[5]

	if nodeType == 'question':
		CorresId = line[0]
		print("{0}\t{1}".format(CorresId,authorId))
	else:
		CorresId = line[7]
		print("{0}\t{1}".format(CorresId,authorId))

	