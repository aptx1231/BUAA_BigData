from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("input/dna.json")

wordCount = textFile.map(lambda word: (json.loads(word)[1][:-10], 1)).reduceByKey(lambda a,b:a+b).map(lambda x: x[0])

def p(x):
    print(json.dumps(x))

wordCount.foreach(p)


