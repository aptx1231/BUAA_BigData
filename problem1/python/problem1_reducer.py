#!/usr/bin/env python

import sys
import json

key2name = {}
 
for line in sys.stdin:
    line = line.strip()
 
    key, filename = line.split('\t', 1)

    nameList = key2name.get(key, [])
    if filename not in nameList:
        nameList.append(filename)
    key2name[key] = nameList


for key in key2name:
	print json.dumps((key, key2name[key]))
 
