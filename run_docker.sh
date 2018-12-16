#!/bin/bash

exec docker run \
  --rm \
  -it \
  -v $PWD:/workspace \
  --workdir=/workspace \
  --name python \
  --cap-add SYS_PTRACE \
  --cap-add SYS_ADMIN \
  python:3 bash
