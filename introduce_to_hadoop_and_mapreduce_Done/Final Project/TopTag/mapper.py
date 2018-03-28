#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0] == 'id':
		continue 
	if len(line) != 19:
		continue
	if line[5] =='question':
		tagslist = line[2].split()
		for tag in tagslist:
			print tag