from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("input/records.json")

t = textFile.map(lambda x: (json.loads(x)[1], json.loads(x)))

order = t.filter(lambda x: x[1][0]=="order")
line_item = t.filter(lambda x: x[1][0]=="line_item")

def p(x):
    print(json.dumps(x))

ans = order.join(line_item).map(lambda x: x[1][0]+x[1][1])
ans.foreach(p)
