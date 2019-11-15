#!/usr/bin/env python
	
import sys
import json
 
for line in sys.stdin:
    line = line.strip()

    record = json.loads(line)

    order_id = record[1]
    value = record
    
    print '%s\t%s' % (order_id, json.dumps(value))


