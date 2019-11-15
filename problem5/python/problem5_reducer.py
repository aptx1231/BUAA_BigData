#!/usr/bin/env python

import sys
import json
 
string2id = {}

for line in sys.stdin:
    line = line.strip()
    trimmedNucleotide, seqId = line.split('\t', 1)

    idList = string2id.get(trimmedNucleotide, [])
    idList.append(seqId)
    string2id[trimmedNucleotide] = idList 

for s in string2id:
    print json.dumps(s)


 
