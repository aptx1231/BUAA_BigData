from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("input/books.json")

wordCount = textFile.map(lambda x: (list(set(json.loads(x)[1].split())), json.loads(x)[0])).flatMap(lambda x: [(i,[x[1]]) for i in x[0]]).reduceByKey(lambda a,b:a+b)

def p(x):
    print(json.dumps(x))

wordCount.foreach(p)
