# isc

# Get start
path example
```bash
  MPI_PATH: /opt/openmpi # Path to MPI library. The benchmarks have been tested with OpenMPI version 1.10.2.
  CUDA_PATH: /usr/local/cuda # Path to CUDA library. The benchmarks have been tested with version 7.5.18.
  CUDNN_PATH:  /home/wit/cuda #Path to CUDNN library. The benchmarks have been tested with version 5.0.
  NCCL_PATH: /home/wit/nccl-2.0.5-3 #Path to NCCL library. NCCL library is available at https://github.com/NVIDIA/nccl. The benchmarks have been tested with commit b3a9e1333d9e2e1b8553b5843ba1ba4f7c79739d
  ARCH: 20
```
[check Compute Capability](https://developer.nvidia.com/cuda-gpus)

make example
```bash
make CUDA_PATH=/usr/local/cuda CUDNN_PATH=/usr/local/cuda MPI_PATH=/opt/openmpi NCCL_PATH=/home/wit/nccl-2.0.5-3 ARCH=sm_30
```
Note: nccl2 must change ```build/bin``` to ```bin``` and ```build/lib``` to ```lib``` in  ``code/nvidia/MakeFile``

export example

```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/:/home/wit/cuda/lib64/:/home/wit/nccl-2.0.5-3/lib/:/home/wit/nccl-2.0.5-3/lib/
```
```
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/:/usr/lib/x86_64-linux-gnu/:/home/wit/nccl-2.0.5-3/lib/:/home/wit/nccl-2.0.5-3/lib/
```

command
```
/usr/local/cuda/bin/nvcc conv_bench.cu -DPAD_KERNELS=1 -o bin/conv_bench -I ../kernels/ -I /usr/local/cuda/include -I /home/user1/cuda/include/ -L /home/user1/cuda/lib64/ -L /usr/local/cuda/lib64 -lcurand -lcudnn --generate-code arch=compute_30,code=sm_30 -std=c++11

```

run docker
```
nvidia-docker run --name deepbench --rm -ti  nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04 bash
```

## environment

| name | gcc | cuda Toolkit | Cudnn | gpu | os | pass? | note
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| meaka | 4.8.4 | 9.0 | 9.0 | c2050 x2 | centos 7 | No | gpu not support
| 92 | 6.3 | 9.0 | 9.0 | 1080 | ubuntu 16.04 | No | build fail
| 91 | 5.4.0 | 9.0 | 9.0 | k40 | ubuntu 17.04 | Yes | use nvidia-docker

## Result

```bash
> root@1bba7e82e3b5:~/DeepBench/code/nvidia/bin# ./rnn_bench 
```

| type | hidden | N | timesteps | precision | fwd_time | bwd_time |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| vanilla | 1760 | 16 | 50 | half | 24956 | 14012|
| vanilla | 1760 | 32 | 50 | half | 29701 | 29868|
| vanilla | 1760 | 64 | 50 | half | 29406 | 31098|
| vanilla | 1760 | 128 | 50 | half | 34755 | 35602|
| vanilla | 2048 | 16 | 50 | half | 31474 | 18988|
| vanilla | 2048 | 32 | 50 | half | 35944 | 36173|
| vanilla | 2048 | 64 | 50 | half | 36138 | 37601|
| vanilla | 2048 | 128 | 50 | half | 44101 | 45371|
| vanilla | 2560 | 16 | 50 | half | 47704 | 25964|
| vanilla | 2560 | 32 | 50 | half | 45153 | 44642|
| vanilla | 2560 | 64 | 50 | half | 44936 | 46444|
| vanilla | 2560 | 128 | 50 | half | 86739 | 63148|
| lstm | 512 | 16 | 25 | half | 5544 | 3685|
| lstm | 512 | 32 | 25 | half | 5894 | 16888|
| lstm | 512 | 64 | 25 | half | 6000 | 16822|
| lstm | 512 | 128 | 25 | half | 7066 | 16846|
| lstm | 1024 | 16 | 25 | half | 16692 | 10974|
| lstm | 1024 | 32 | 25 | half | 12189 | 32360|
| lstm | 1024 | 64 | 25 | half | 12226 | 32461|
| lstm | 1024 | 128 | 25 | half | 22772 | 33934|
| lstm | 2048 | 16 | 25 | half | 58859 | 34638|
| lstm | 2048 | 32 | 25 | half | 41558 | 67095|
| lstm | 2048 | 64 | 25 | half | 42381 | 69523|
| lstm | 2048 | 128 | 25 | half | 81286 | 86872|
| lstm | 4096 | 16 | 25 | half | 217817 | 124205|
| lstm | 4096 | 32 | 25 | half | 159526 | 142910|
| lstm | 4096 | 64 | 25 | half | 160383 | 173339|
| lstm | 4096 | 128 | 25 | half | 283996 | 400587|
| lstm | 1536 | 8 | 50 | half | 39442 | 21086|
| lstm | 1536 | 16 | 50 | half | 69014 | 38579|
| lstm | 1536 | 32 | 50 | half | 55694 | 95103|
| lstm | 256 | 16 | 150 | half | 16541 | 14857|
| lstm | 256 | 32 | 150 | half | 20465 | 49300|
| lstm | 256 | 64 | 150 | half | 21610 | 50370|
| gru | 2816 | 32 | 1500 | half | 3400682 | 4155681|
| gru | 2816 | 32 | 750 | half | 1704113 | 2080208|
| gru | 2816 | 32 | 375 | half | 854418 | 1040876|
| gru | 2816 | 32 | 187 | half | 426487 | 519967|
| gru | 2048 | 32 | 1500 | half | 2178991 | 3028861|
| gru | 2048 | 32 | 750 | half | 1092300 | 1517456|
| gru | 2048 | 32 | 375 | half | 548354 | 759563|
| gru | 2048 | 32 | 187 | half | 274133 | 379981|
| gru | 1536 | 32 | 1500 | half | 1010622 | 2149587|
| gru | 1536 | 32 | 750 | half | 508620 | 1077109|
| gru | 1536 | 32 | 375 | half | 255781 | 540406|
| gru | 1536 | 32 | 187 | half | 128934 | 271631|
| gru | 2560 | 32 | 1500 | half | 3002000 | 3779189|
| gru | 2560 | 32 | 750 | half | 1503594 | 1892139|
| gru | 2560 | 32 | 375 | half | 754150 | 947140|
| gru | 2560 | 32 | 187 | half | 376348 | 473270|
| gru | 512 | 32 | 1 | half | 249 | 541|
| gru | 1024 | 32 | 1500 | half | 596599 | 1447135|
| gru | 1024 | 64 | 1500 | half | 615169 | 1468933


