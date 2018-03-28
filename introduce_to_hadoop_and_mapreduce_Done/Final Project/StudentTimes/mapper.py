#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	authorId = line[3]
	if authorId == 'author_id':
		continue
	authorId = line[3]
	currenHour = line[8]
	print("{0}\t{1}".format(authorId,currenHour))
	