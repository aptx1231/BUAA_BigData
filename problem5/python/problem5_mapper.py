#!/usr/bin/env python
	
import sys
import json
 
for line in sys.stdin:
    line = line.strip()

    dnaseq = json.loads(line)

    seqId = dnaseq[0]
    nucleotide = dnaseq[1]
    trimmedNucleotide = nucleotide[:-10]

    print '%s\t%s' % (trimmedNucleotide, seqId)

