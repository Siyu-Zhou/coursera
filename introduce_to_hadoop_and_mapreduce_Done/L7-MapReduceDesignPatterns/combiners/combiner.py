#!/usr/bin/python
from datetime import datetime
import sys

everydaySales={}
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	day, sale = data
	if(day not in everydaySales.keys()):
		everydaySales[day] = 0
	everydaySales[day] += float(sale)
for day in everydaySales.keys():
	print "{0}\t{1}".format(day, everydaySales[day])
