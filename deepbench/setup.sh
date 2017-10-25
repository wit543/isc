#!/bin/sh

apt-get update && apt-get install -y git vim && apt-get clean && rm -rf /var/lib/apt/lists/*

cd ~

git clone https://github.com/baidu-research/DeepBench.git

cd DeepBench/code/nvidia/

make CUDA_PATH=/usr/local/cuda CUDNN_PATH=/usr/local/cuda ARCH=sm_35

