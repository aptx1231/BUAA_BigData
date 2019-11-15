#!/usr/bin/env python

import sys
import json

id2record = {}
 
for line in sys.stdin:
    line = line.strip()
 
    order_id, value = line.split('\t', 1)
    record = json.loads(value)

    valueList = id2record.get(order_id, [])
    valueList.append(record)
    id2record[order_id] = valueList


result = []
for order_id in id2record:
    valueList = id2record[order_id]
    for vl in valueList:
        if vl[0] == 'order':
            order = vl
    for vl in valueList:
        if vl[0] == 'line_item':
            result.append((order + vl))

for item in result:
	print json.dumps(item)
 
