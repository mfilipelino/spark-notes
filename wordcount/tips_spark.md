---
title: tips spark
tags: 
notebook: 
---

```sh
sudo docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```

## hello world

```python
import pyspark 
sc = pyspark.SparkContext('local[*]')
# do something to prove it works
rdd = sc.parallelize(range(1000))
rdd.takeSample(False, 5)
```
```python
>>> [471, 724, 204, 729, 278]
```

```
token=S=s75:U=7d7504:E=16b37432cb6:C=163df91fe08:P=1cd:A=en-devtoken:V=2:H=dcdd0d8202c7efe9af20a15150fe4356
noteStore=https://www.evernote.com/shard/s75/notestore
```