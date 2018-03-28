#!/usr/bin/env python
import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		IPaddress,identity,username,time,zone,method,path,querystring,statuscode,size = data
		print "{0}".format(IPaddress)