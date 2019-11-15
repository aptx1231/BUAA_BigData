#!/usr/bin/env python

import sys
import json
 
word2count = {}
 
for line in sys.stdin:
    line = line.strip()
 
    word, count = line.split('\t', 1)

    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        pass

for word in word2count:
    if word2count[word] == 1:
        name1, name2 = word.split(',', 1)
        print json.dumps((name1, name2))

