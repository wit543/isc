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
make CUDA_PATH=/usr/local/cuda CUDNN_PATH=/home/wit/cuda MPI_PATH=/opt/openmpi NCCL_PATH=/home/wit/nccl-2.0.5-3 ARCH=sm_30
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

