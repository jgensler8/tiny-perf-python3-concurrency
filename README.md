# Short Perf Tutorial on Python 3 Concurrency

## How to Use

1. Start the python 3 container

```
./run_docker.sh
$ apt-get install linux-tools
```

2. Edit `gendirs.py`

```
# Change Executor
# Change executor pool size
```

3. Run Experiment

```
$ ./run_experiment.sh
```

## Basic

```
real	0m6.127s
user	0m2.340s
sys	0m3.700s
```

![basic](./results/generic.svg)

## `ThreadPoolExecutor`

### 1

```
real	0m5.001s
user	0m1.930s
sys	0m3.000s
```

![thread-pool-executor-1](./results/thread-pool-executor-1.svg)

### 1000

```
real	0m12.564s
user	0m4.660s
sys	0m15.160s
```

![thread-pool-executor-1000](./results/thread-pool-executor-1000.svg)

## `ProcessPoolexecutor`

### 1

```
real	0m5.334s
user	0m1.990s
sys	0m3.280s
```

![process-pool-executor-1](./results/process-pool-executor-1.svg)

### 100

```
real	0m1.731s
user	0m3.580s
sys	0m4.610s
```

![process-pool-executor-100](./results/process-pool-executor-100.svg)

### 1000

```
real	0m14.524s
user	0m5.790s
sys	0m14.810s
```

![process-pool-executor-1000](./results/process-pool-executor-1000.svg)
