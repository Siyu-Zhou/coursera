#!/usr/bin/python

import sys
PostLength = 0
AnswerLength = 0
AveAnswerLength = 0
AnswerNum = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 3:
		continue
	CorresId,node_type,bodylength = data
	bodylength = float(bodylength)
	
	if oldKey and oldKey != CorresId:
		if AnswerNum != 0:
			AveAnswerLength = AnswerLength / AnswerNum
		else:
			AveAnswerLength = 0
		print("{0}\t{1}\t{2}".format(oldKey,PostLength,AveAnswerLength))
		PostLength = 0
		AnswerLength = 0
		AveAnswerLength = 0
		AnswerNum = 0

	if node_type == 'question':
		PostLength += bodylength
	if node_type == 'answer':
		AnswerLength += bodylength
		AnswerNum += 1
	oldKey = CorresId

if oldKey != None:
		if AnswerNum != 0:
			AveAnswerLength = AnswerLength / AnswerNum
		else:
			AveAnswerLength = 0
		print("{0}\t{1}\t{2}".format(oldKey,PostLength,AveAnswerLength))

