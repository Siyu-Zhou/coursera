#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0] == 'id':
		continue 
	if len(line) != 19:
		continue
	node_type = line[5]
	if line[5] == 'question':
		CorresId = line[0]
	if line[5] == 'answer':
		CorresId = line [7]
	bodylength = len(line[4])
	print("{0}\t{1}\t{2}".format(CorresId,node_type,bodylength))