#this is silmilar to inner join in SQl
#!/usr/bin/python

import sys
userResult = {}
nodeResult = {}
    
for line in sys.stdin:
	data = line.strip().split('\t')
	if data[4] == 'B':
		nodeResult[data[3]] = data[0:4] + data[5:10]
	if data[1] == 'A':
		userResult[data[0]] = data[2:6]
for key in userResult.keys():
	# inner join key need exist in two table 
	if nodeResult.has_key(key):
		output =  nodeResult[key] + userResult[key]
		print output
