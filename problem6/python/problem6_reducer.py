#!/usr/bin/env python

import sys
import json
 
poi2value = {}

for line in sys.stdin:
    line = line.strip()

    poi, value = line.split('\t', 1)
    poi = tuple(json.loads(poi))
    value = json.loads(value)

    valueList = poi2value.get(poi, [])
    valueList.append(value)
    poi2value[poi] = valueList 

for key in poi2value:
    values = poi2value[key]  # (key[0],key[1]) useful list
    a_rows = filter(lambda x : x[0] == 'a', values)
    b_rows = filter(lambda x : x[0] == 'b', values)
    # print a_rows, b_rows
    result = 0
    for a in a_rows:
        for b in b_rows:
            if (a[2]==b[1]):  # match
                result += a[3] * b[3]

    # emit non-zero results
    if result != 0:
        print json.dumps((key[0], key[1], result))


 
