from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("input/friends.json")

wordCount = textFile.flatMap(lambda word: (((json.loads(word)[0], json.loads(word)[1]), 1), ((json.loads(word)[1], json.loads(word)[0]), 1))).reduceByKey(lambda a,b:a+b).filter(lambda x: x[1] == 1).map(lambda x: x[0])

def p(x):
    print(json.dumps(x))

wordCount.foreach(p)


