#!/usr/bin/env python
	
import sys
import json
 
for line in sys.stdin:
    line = line.strip()

    record = json.loads(line)

    if record[0] == 'a':
    	i = record[1]
    	for j in range(5):
           print '%s\t%s' % (json.dumps((i, j)), json.dumps(record))
    elif record[0] == 'b':
        j = record[2]
        for i in range(5):
           print '%s\t%s' % (json.dumps((i, j)), json.dumps(record))
    else:
        pass


