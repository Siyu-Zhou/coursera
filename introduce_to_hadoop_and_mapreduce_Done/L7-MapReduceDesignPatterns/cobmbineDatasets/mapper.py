#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    startId = line[0]
    if startId == 'id' or startId == 'user_ptr_id':
    	continue
    if len(line) == 19 :
    	data = line[0:4] + ['B'] + line[5:10]
    	print ("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))

    if len (line) == 5:
    	data = line[0:1] + ['A'] + line[1:5]
    	print ("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
        
