#!/usr/bin/env python

import sys
import json
 
friendship = {}
 
for line in sys.stdin:
    line = line.strip()
 
    name1, name2 = line.split('\t', 1)

    valueList = friendship.get(name1, [])
    valueList.append(name2)
    friendship[name1] = valueList

    # valueList = friendship.get(name2, [])
    # valueList.append(name1)
    # friendship[name2] = valueList

# print friendship

for person in friendship:
    list_of_friends = friendship[person]
    
    friendCount = {}
    for friend in list_of_friends:
        friendCount.setdefault(friend, 0)
        friendCount[friend] = friendCount[friend] + 1
    # print friendCount
    asymfriends = filter(lambda x : friendCount[x] == 1, friendCount.keys())
    # print asymfriends
    for friend in asymfriends:
        print json.dumps((person, friend))


 
