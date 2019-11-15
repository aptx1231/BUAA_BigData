from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("input/matrix.json")

t = textFile.map(lambda word: json.loads(word))
a = t.filter(lambda x: x[0]=='a')
b = t.filter(lambda x: x[0]=='b')
aa = a.flatMap(lambda x: [((x[1], i), [x]) for i in range(5)]).reduceByKey(lambda a,b:a+b)
bb = b.flatMap(lambda x: [((i, x[2]), [x]) for i in range(5)]).reduceByKey(lambda a,b:a+b)
res = aa.join(bb)

def f(x):
    a_rows = x[1][0]
    b_rows = x[1][1]
    result = 0
    for a in a_rows:
        for b in b_rows:
            if (a[2]==b[1]):  # match
                result += a[3] * b[3]
    if result != 0:
        print(json.dumps((x[0][0], x[0][1], result)))

res.foreach(f)
