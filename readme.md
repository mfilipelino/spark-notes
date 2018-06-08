---
title: tips spark
tags: 
notebook: 
---

## run notebook spark

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