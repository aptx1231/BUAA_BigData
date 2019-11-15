#!/usr/bin/env python
	
import sys
import json
 
for line in sys.stdin:
    line = line.strip()

    record = json.loads(line)

    name1 = record[0]
    name2 = record[1]
    
    print '%s,%s\t%s' % (name1, name2, 1)
    print '%s,%s\t%s' % (name2, name1, 1)

