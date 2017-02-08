# Solving the Tricky Turtles puzzle

![](http://img2.everafterguide.com/1_cjfX-RtrzFtwFCjRYZeEj6qU4=/product_images/full/e41a4883da06d4e8a33b1538c924790d8c45b07c/the-scrambled-jigsaw-puzzle-tricky-turtles-by-blue-opal.jpg)

This script uses Apache Spark to solve all possible board solutions in parallel.

To run, call with something like:

```bash
time spark-2.1.0-bin-hadoop2.7/bin/spark-submit --master spark://192.168.178.210:7077 --py-files turtles.py --conf spark.python.worker.memory=4g --conf spark.driver.memory=4g --conf spark.executor.memory=3g game.py  > job.log 2> job.err
```
