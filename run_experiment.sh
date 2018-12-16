#!/bin/bash
perf record -F 99 -g python3 gendirs.py --dir /tmp/mydir --depth 4
perf script | ./FlameGraph/stackcollapse-perf.pl > out.perf-folded
./FlameGraph/flamegraph.pl out.perf-folded > perf-kernel.svg