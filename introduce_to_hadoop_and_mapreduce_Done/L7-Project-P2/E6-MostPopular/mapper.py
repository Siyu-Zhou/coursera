#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		IPaddress,identity,username,time,zone,method,path,querystring,statuscode,size = data
		path = re.sub(r"^http://www.the-associates.co.uk", "", path)
		print "{0}".format(path)
