提交要求

下载资源里的小作业文件夹，解压MapReduce Assignments(data).zip，按照作业说明,分别使用**Hadoop和Spark**完成6道题目。**所有作业要求能在之前搭建好的环境中进行测试并通过且结果正确，否者没有成绩**

完成的代码放在各个小题的文件夹中，如wordcount示例题目，python，java文件夹中分别是用python，java实现的hadoop程序，pyspark中是用spark实现的程序。

最终按如下要求提交：

├──学号姓名                  //所有作业放到以学号命名的文件夹中
│   ├── problem1                              // 小作业1  
│   │   ├── python                              // hadoop python 

│   │   ├── java                              // hadoop java  和 python 2选一

│   │   ├── pyspark                              // spark实现

……  // 小作业2-6如上

**文件严格按照如下规格命名：**

**hadoop python：题目名_mapper.py  题目名_reducer.py    如 :problem1_mapper.py  problem1_reducer.py**  

**hadoop java：题目名_mapper.java  题目名_reducer.java**

**spark :题目名_spark.py** 

打包成zip格式后提交。



docker run -it suhothayan/hadoop-spark-pig-hive:2.9.2

vim input.txt

hadoop fs -put input.txt input

hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.2.jar wordcount /user/root/input/input.txt /user/root/output/out

hadoop fs -getmerge /user/root/output/out result.txt

**Map-Reduce**

挂载本地目录到 docker 容器

```
docker run -it -v /home/jwjiang/BigData/problem6:/home/root/a_dir/ suhothayan/hadoop-spark-pig-hive:2.9.2
```

将文件倒入 hdfs 指定路径下，作为输入

```
hadoop fs -put /home/root/a_dir/matrix.json input
```

运行

```
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python /home/root/a_dir/python/problem6_mapper.py " -reducer " python /home/root/a_dir/python/problem6_reducer.py " -input /user/root/input/matrix.json -output /user/root/output/out
```

从 hdfs 获取结果到本地

```
hadoop fs -getmerge /user/root/output/out result.txt
```

**Spark**

挂载本地目录到 docker 容器

```
docker run -it -v /home/jwjiang/BigData/problem6:/home/root/a_dir/ suhothayan/hadoop-spark-pig-hive:2.9.2
```

将文件倒入 hdfs 指定路径下，作为输入

```
hadoop fs -put /home/root/a_dir/matrix.json input
```

运行

```
spark-submit home/root/a_dir/pyspark/problem6_spark.py
```

命令行运行

```
pyspark
sc.stop()
粘贴代码
```

