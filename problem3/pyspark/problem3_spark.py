from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("input/friends.json")

wordCount = textFile.map(lambda word:(json.loads(word)[0],1)).reduceByKey(lambda a,b:a+b)

def p(x):
    print(json.dumps(x))

wordCount.foreach(p)


