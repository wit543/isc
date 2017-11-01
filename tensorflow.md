
```sh
# install git
apt update & apt install git vim curl wget 

# install bazel 
sudo apt install openjdk-8-jdk

echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | apt-key add -

apt update && apt install -y bazel

# get tensorflow
git clone https://github.com/tensorflow/tensorflow
cd tensorflow
git checkout r1.4

# install dependency
apt install python3-numpy python3-dev python3-pip python3-wheel
apt install libcupti-dev  # install gpu dependency
pip3 install --upgrade pip
pip3 install six numpy wheel
pip3 install py-cpuinfo portpicker numpy
```

option
```bash
# clang 
apt install llvm build-essential clang-4.0

# openmpi
apt install libopenmpi-dev

```

option
```bash
location of python
Python library path
jemalloc
Google Cloud Platform support
Hadoop File System support
Amazon S3 File System support
XLA JIT support
GDR support
VERBS support
OpenCL support
# if no
  CUDA support
  CUDA SDK version you want to use, e.g. 7.0.
  location where CUDA 9.0 toolkit is installed
  cuDNN version you want to use
  location where cuDNN 7 library is installed
  list of comma-separated Cuda compute capabilities
  clang as CUDA compiler
  MPI support
# if yes 
  C++ compiler
  C compiler
  ComputeCpp for SYCL 1.2 # if choose opencl
```

configure
```bash
root@013e4b961ffd:/tensorflow# ./configure 
You have bazel 0.7.0 installed.
Please specify the location of python. [Default is /usr/bin/python]: /usr/bin/python3


Found possible Python library paths:
  /usr/local/lib/python3.5/dist-packages
  /usr/lib/python3/dist-packages
Please input the desired Python library path to use.  Default is [/usr/local/lib/python3.5/dist-packages]

Do you wish to build TensorFlow with jemalloc as malloc support? [Y/n]: y
jemalloc as malloc support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Google Cloud Platform support? [Y/n]: y
Google Cloud Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Hadoop File System support? [Y/n]: y
Hadoop File System support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Amazon S3 File System support? [Y/n]: y
Amazon S3 File System support will be enabled for TensorFlow.

Do you wish to build TensorFlow with XLA JIT support? [y/N]: y
XLA JIT support will be enabled for TensorFlow.

Do you wish to build TensorFlow with GDR support? [y/N]: y
GDR support will be enabled for TensorFlow.

Do you wish to build TensorFlow with VERBS support? [y/N]: y
VERBS support will be enabled for TensorFlow.

Do you wish to build TensorFlow with OpenCL support? [y/N]: n
No OpenCL support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]: y
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use, e.g. 7.0. [Leave empty to default to CUDA 8.0]: 9.0


Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]: 


Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 6.0]: 7.0


Please specify the location where cuDNN 7.0 library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:


Invalid path to cuDNN 7.0 toolkit. None of the following files can be found:
/usr/local/cuda-9.0/lib64/libcudnn.so.7.0
/usr/local/cuda-9.0/libcudnn.so.7.0
/usr/lib/x86_64-linux-gnu/libcudnn.so.7.0
Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 6.0]: 7       


Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:


Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size. [Default is: 3.5,5.2]3.0,3.5,3.7,5.2


Do you want to use clang as CUDA compiler? [y/N]: n
nvcc will be used as CUDA compiler.

Please specify which gcc should be used by nvcc as the host compiler. [Default is /usr/bin/gcc]: 


Do you wish to build TensorFlow with MPI support? [y/N]: y
MPI support will be enabled for TensorFlow.

Please specify the MPI toolkit folder. [Default is /usr]: y


Invalid path to the MPI Toolkit. y/include or False cannot be found
Please specify the MPI toolkit folder. [Default is /usr]: /usr/bin/


Invalid path to the MPI Toolkit. /usr/bin/include or False cannot be found
Please specify the MPI toolkit folder. [Default is /usr]: /usr/local/openmpi


Invalid path to the MPI Toolkit. /usr/local/openmpi/include or False cannot be found
Please specify the MPI toolkit folder. [Default is /usr]: /usr/lib/openmpi


Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]:   


Add "--config=mkl" to your bazel command to build with MKL support.
Please note that MKL on MacOS or windows is still not supported.
If you would like to use a local MKL instead of downloading, please set the environment variable "TF_MKL_ROOT" every time before build.
Configuration finished
```

open mpi

```
cd /root
wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz
tar xvf openmpi-*
cd openmpi-*
./configure --prefix="/root/.openmpi"
make
make install
echo export PATH="$PATH:/root/.openmpi/bin" >> /root/.bashrc
echo export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/root/.openmpi/lib/" >> /root/.bashrc

```

```
Required build parameters:
  TF_DOCKER_BUILD_TYPE=gpu
  TF_DOCKER_BUILD_IS_DEVEL=yes
  TF_DOCKER_BUILD_DEVEL_BRANCH=

Optional build parameters:
  TF_DOCKER_BUILD_CENTRAL_PIP=http://ci.tensorflow.org/view/Nightly/job/nightly-python35-linux-cpu/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow--cp35-cp35m-manylinux1_x86_64.whl
  TF_DOCKER_BUILD_IMAGE_NAME=
  TF_DOCKER_BUILD_VERSION=
  TF_DOCKER_BUILD_PORT=
  TF_DOCKER_BUILD_PUSH_CMD=
ERROR: TF_DOCKER_BUILD_DEVEL_BRANCH is missing for devel docker build
[boss@CudaL tensorflow]$ export TF_DOCKER_BUILD_DEVEL_BRANCH=devel-gpu-cuda9-cudnn7
[boss@CudaL tensorflow]$ tensorflow/tools/docker/parameterized_docker_build.sh
Required build parameters:
  TF_DOCKER_BUILD_TYPE=gpu
  TF_DOCKER_BUILD_IS_DEVEL=yes
  TF_DOCKER_BUILD_DEVEL_BRANCH=devel-gpu-cuda9-cudnn7

Optional build parameters:
  TF_DOCKER_BUILD_CENTRAL_PIP=http://ci.tensorflow.org/view/Nightly/job/nightly-python35-linux-cpu/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow--cp35-cp35m-manylinux1_x86_64.whl
  TF_DOCKER_BUILD_IMAGE_NAME=
  TF_DOCKER_BUILD_VERSION=
  TF_DOCKER_BUILD_PORT=
  TF_DOCKER_BUILD_PUSH_CMD=
```


[tensorflow export config](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker)

```bash
export TF_DOCKER_BUILD_IS_DEVEL=YES
export TF_DOCKER_BUILD_TYPE=GPU
export TF_DOCKER_BUILD_PYTHON_VERSION=PYTHON3
export TF_DOCKER_BUILD_DEVEL_BRANCH=r1.4
export TF_DOCKER_BUILD_IMAGE_NAME=dockerTF
export TF_DOCKER_BUILD_VERSION=0.1
export TF_DOCKER_BUILD_PORT=6789
export NIGHTLY_VERSION="1.head"
export TF_DOCKER_BUILD_CENTRAL_PIP=$(echo ${TF_DOCKER_BUILD_PYTHON_VERSION} | sed s^PYTHON2^http://ci.tensorflow.org/view/Nightly/job/nightly-matrix-cpu/TF_BUILD_IS_OPT=OPT,TF_BUILD_IS_PIP=PIP,TF_BUILD_PYTHON_VERSION=${TF_DOCKER_BUILD_PYTHON_VERSION},label=cpu-slave/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow-${NIGHTLY_VERSION}-cp27-cp27mu-manylinux1_x86_64.whl^ | sed s^PYTHON3^http://ci.tensorflow.org/view/Nightly/job/nightly-python35-linux-cpu/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow-${NIGHTLY_VERSION}-cp35-cp35m-manylinux1_x86_64.whl^)

# tensorflow/
tensorflow/tools/docker/parameterized_docker_build.sh
```

## run

```bash
docker run -p 8890:8888 --name w1 -it boss/test:latest bash
docker run -p 2222:2222 --name w1 -it boss/tensor:lastest bash
python3 isac.py --job_name="ps" --task_index=0
python3 isac.py --job_name="worker" --task_index=0
```
## Result

1 worker
``` bash
root@11f4fcf17414:~/tensorflow-example# python3 isac.py --job_name="worker" --task_index=0
2017-10-30 14:05:10.187873: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-10-30 14:05:10.188938: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_UNKNOWN
2017-10-30 14:05:10.188991: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:152] no NVIDIA GPU device is present: /dev/nvidia0 does not exist
E1030 14:05:10.189143742      60 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-10-30 14:05:10.195727: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-10-30 14:05:10.196475: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
Variables initialized ...
2017-10-30 14:05:11.034132: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 32f2f4c30290824a with config: 
WARNING:tensorflow:Standard services need a 'logdir' passed to the SessionManager
Step: 101,  Epoch:  1,  Batch: 100 of 550,  Cost: 9.3442,  AvgTime: 2.68ms
Step: 201,  Epoch:  1,  Batch: 200 of 550,  Cost: 9.0956,  AvgTime: 1.87ms
Step: 301,  Epoch:  1,  Batch: 300 of 550,  Cost: 7.6957,  AvgTime: 1.88ms
Step: 401,  Epoch:  1,  Batch: 400 of 550,  Cost: 7.7638,  AvgTime: 1.88ms
Step: 501,  Epoch:  1,  Batch: 500 of 550,  Cost: 7.6099,  AvgTime: 1.92ms
Step: 551,  Epoch:  1,  Batch: 550 of 550,  Cost: 7.2564,  AvgTime: 0.97ms
Step: 651,  Epoch:  2,  Batch: 100 of 550,  Cost: 6.8655,  AvgTime: 2.54ms
Step: 751,  Epoch:  2,  Batch: 200 of 550,  Cost: 7.8118,  AvgTime: 1.87ms
Step: 851,  Epoch:  2,  Batch: 300 of 550,  Cost: 7.5587,  AvgTime: 1.86ms
Step: 951,  Epoch:  2,  Batch: 400 of 550,  Cost: 6.1079,  AvgTime: 1.85ms
Step: 1051,  Epoch:  2,  Batch: 500 of 550,  Cost: 7.5817,  AvgTime: 1.85ms
Step: 1101,  Epoch:  2,  Batch: 550 of 550,  Cost: 6.0909,  AvgTime: 0.91ms
Step: 1201,  Epoch:  3,  Batch: 100 of 550,  Cost: 6.4242,  AvgTime: 2.41ms
Step: 1301,  Epoch:  3,  Batch: 200 of 550,  Cost: 6.4984,  AvgTime: 1.81ms
Step: 1401,  Epoch:  3,  Batch: 300 of 550,  Cost: 6.7009,  AvgTime: 1.87ms
Step: 1501,  Epoch:  3,  Batch: 400 of 550,  Cost: 6.5520,  AvgTime: 1.86ms
Step: 1601,  Epoch:  3,  Batch: 500 of 550,  Cost: 5.6854,  AvgTime: 1.86ms
Step: 1651,  Epoch:  3,  Batch: 550 of 550,  Cost: 5.2038,  AvgTime: 0.95ms
Step: 1751,  Epoch:  4,  Batch: 100 of 550,  Cost: 5.6384,  AvgTime: 2.55ms
Step: 1851,  Epoch:  4,  Batch: 200 of 550,  Cost: 5.3745,  AvgTime: 1.87ms
Step: 1951,  Epoch:  4,  Batch: 300 of 550,  Cost: 5.5229,  AvgTime: 1.87ms
Step: 2051,  Epoch:  4,  Batch: 400 of 550,  Cost: 5.8770,  AvgTime: 1.83ms
Step: 2151,  Epoch:  4,  Batch: 500 of 550,  Cost: 4.8132,  AvgTime: 1.86ms
Step: 2201,  Epoch:  4,  Batch: 550 of 550,  Cost: 5.8295,  AvgTime: 0.93ms
Step: 2301,  Epoch:  5,  Batch: 100 of 550,  Cost: 5.8646,  AvgTime: 2.43ms
Step: 2401,  Epoch:  5,  Batch: 200 of 550,  Cost: 6.2025,  AvgTime: 1.89ms
Step: 2501,  Epoch:  5,  Batch: 300 of 550,  Cost: 5.5218,  AvgTime: 1.85ms
Step: 2601,  Epoch:  5,  Batch: 400 of 550,  Cost: 5.4285,  AvgTime: 1.87ms
Step: 2701,  Epoch:  5,  Batch: 500 of 550,  Cost: 5.3155,  AvgTime: 1.88ms
Step: 2751,  Epoch:  5,  Batch: 550 of 550,  Cost: 5.2243,  AvgTime: 0.92ms
Step: 2851,  Epoch:  6,  Batch: 100 of 550,  Cost: 5.2342,  AvgTime: 2.50ms
Step: 2951,  Epoch:  6,  Batch: 200 of 550,  Cost: 4.2231,  AvgTime: 1.84ms
Step: 3051,  Epoch:  6,  Batch: 300 of 550,  Cost: 5.3939,  AvgTime: 1.81ms
Step: 3151,  Epoch:  6,  Batch: 400 of 550,  Cost: 5.7847,  AvgTime: 1.84ms
Step: 3251,  Epoch:  6,  Batch: 500 of 550,  Cost: 5.0320,  AvgTime: 1.83ms
Step: 3301,  Epoch:  6,  Batch: 550 of 550,  Cost: 5.4229,  AvgTime: 0.93ms
Step: 3401,  Epoch:  7,  Batch: 100 of 550,  Cost: 5.2380,  AvgTime: 2.42ms
Step: 3501,  Epoch:  7,  Batch: 200 of 550,  Cost: 4.7412,  AvgTime: 1.87ms
Step: 3601,  Epoch:  7,  Batch: 300 of 550,  Cost: 5.2927,  AvgTime: 1.83ms
Step: 3701,  Epoch:  7,  Batch: 400 of 550,  Cost: 4.8251,  AvgTime: 1.84ms
Step: 3801,  Epoch:  7,  Batch: 500 of 550,  Cost: 5.1251,  AvgTime: 1.88ms
Step: 3851,  Epoch:  7,  Batch: 550 of 550,  Cost: 5.3676,  AvgTime: 0.92ms
Step: 3951,  Epoch:  8,  Batch: 100 of 550,  Cost: 4.6891,  AvgTime: 2.53ms
Step: 4051,  Epoch:  8,  Batch: 200 of 550,  Cost: 5.3651,  AvgTime: 1.83ms
Step: 4151,  Epoch:  8,  Batch: 300 of 550,  Cost: 4.8926,  AvgTime: 1.84ms
Step: 4251,  Epoch:  8,  Batch: 400 of 550,  Cost: 4.6569,  AvgTime: 1.87ms
Step: 4351,  Epoch:  8,  Batch: 500 of 550,  Cost: 4.1090,  AvgTime: 1.82ms
Step: 4401,  Epoch:  8,  Batch: 550 of 550,  Cost: 4.7689,  AvgTime: 0.93ms
Step: 4501,  Epoch:  9,  Batch: 100 of 550,  Cost: 4.7638,  AvgTime: 2.39ms
Step: 4601,  Epoch:  9,  Batch: 200 of 550,  Cost: 5.4104,  AvgTime: 1.86ms
Step: 4701,  Epoch:  9,  Batch: 300 of 550,  Cost: 5.0772,  AvgTime: 1.83ms
Step: 4801,  Epoch:  9,  Batch: 400 of 550,  Cost: 4.3574,  AvgTime: 1.85ms
Step: 4901,  Epoch:  9,  Batch: 500 of 550,  Cost: 4.9240,  AvgTime: 1.86ms
Step: 4951,  Epoch:  9,  Batch: 550 of 550,  Cost: 4.5696,  AvgTime: 0.92ms
Step: 5051,  Epoch: 10,  Batch: 100 of 550,  Cost: 5.0474,  AvgTime: 2.54ms
Step: 5151,  Epoch: 10,  Batch: 200 of 550,  Cost: 4.3111,  AvgTime: 1.83ms
Step: 5251,  Epoch: 10,  Batch: 300 of 550,  Cost: 4.7492,  AvgTime: 1.90ms
Step: 5351,  Epoch: 10,  Batch: 400 of 550,  Cost: 4.2753,  AvgTime: 1.89ms
Step: 5451,  Epoch: 10,  Batch: 500 of 550,  Cost: 3.8826,  AvgTime: 1.89ms
Step: 5501,  Epoch: 10,  Batch: 550 of 550,  Cost: 5.1053,  AvgTime: 0.92ms
Step: 5601,  Epoch: 11,  Batch: 100 of 550,  Cost: 4.2995,  AvgTime: 2.39ms
Step: 5701,  Epoch: 11,  Batch: 200 of 550,  Cost: 4.2454,  AvgTime: 1.88ms
Step: 5801,  Epoch: 11,  Batch: 300 of 550,  Cost: 4.7430,  AvgTime: 1.89ms
Step: 5901,  Epoch: 11,  Batch: 400 of 550,  Cost: 4.1425,  AvgTime: 1.86ms
Step: 6001,  Epoch: 11,  Batch: 500 of 550,  Cost: 4.9476,  AvgTime: 1.83ms
Step: 6051,  Epoch: 11,  Batch: 550 of 550,  Cost: 4.7388,  AvgTime: 0.94ms
Step: 6151,  Epoch: 12,  Batch: 100 of 550,  Cost: 4.4027,  AvgTime: 2.48ms
Step: 6251,  Epoch: 12,  Batch: 200 of 550,  Cost: 4.2996,  AvgTime: 1.86ms
Step: 6351,  Epoch: 12,  Batch: 300 of 550,  Cost: 5.2491,  AvgTime: 1.88ms
Step: 6451,  Epoch: 12,  Batch: 400 of 550,  Cost: 4.1889,  AvgTime: 1.83ms
Step: 6551,  Epoch: 12,  Batch: 500 of 550,  Cost: 4.6197,  AvgTime: 1.87ms
Step: 6601,  Epoch: 12,  Batch: 550 of 550,  Cost: 4.3870,  AvgTime: 0.93ms
Step: 6701,  Epoch: 13,  Batch: 100 of 550,  Cost: 4.1196,  AvgTime: 2.41ms
Step: 6801,  Epoch: 13,  Batch: 200 of 550,  Cost: 4.0981,  AvgTime: 1.86ms
Step: 6901,  Epoch: 13,  Batch: 300 of 550,  Cost: 3.7777,  AvgTime: 1.85ms
Step: 7001,  Epoch: 13,  Batch: 400 of 550,  Cost: 4.1155,  AvgTime: 1.87ms
Step: 7101,  Epoch: 13,  Batch: 500 of 550,  Cost: 4.1399,  AvgTime: 1.87ms
Step: 7151,  Epoch: 13,  Batch: 550 of 550,  Cost: 4.6489,  AvgTime: 0.91ms
Step: 7251,  Epoch: 14,  Batch: 100 of 550,  Cost: 4.4053,  AvgTime: 2.51ms
Step: 7351,  Epoch: 14,  Batch: 200 of 550,  Cost: 3.8478,  AvgTime: 1.83ms
Step: 7451,  Epoch: 14,  Batch: 300 of 550,  Cost: 3.7163,  AvgTime: 1.84ms
Step: 7551,  Epoch: 14,  Batch: 400 of 550,  Cost: 4.0953,  AvgTime: 1.86ms
Step: 7651,  Epoch: 14,  Batch: 500 of 550,  Cost: 4.1946,  AvgTime: 1.84ms
Step: 7701,  Epoch: 14,  Batch: 550 of 550,  Cost: 4.1216,  AvgTime: 0.93ms
Step: 7801,  Epoch: 15,  Batch: 100 of 550,  Cost: 4.2850,  AvgTime: 2.42ms
Step: 7901,  Epoch: 15,  Batch: 200 of 550,  Cost: 3.8390,  AvgTime: 1.85ms
Step: 8001,  Epoch: 15,  Batch: 300 of 550,  Cost: 3.6235,  AvgTime: 1.86ms
Step: 8101,  Epoch: 15,  Batch: 400 of 550,  Cost: 3.9709,  AvgTime: 1.84ms
Step: 8201,  Epoch: 15,  Batch: 500 of 550,  Cost: 4.3143,  AvgTime: 1.85ms
Step: 8251,  Epoch: 15,  Batch: 550 of 550,  Cost: 4.4041,  AvgTime: 0.91ms
Step: 8351,  Epoch: 16,  Batch: 100 of 550,  Cost: 4.2922,  AvgTime: 2.53ms
Step: 8451,  Epoch: 16,  Batch: 200 of 550,  Cost: 3.8886,  AvgTime: 1.89ms
Step: 8551,  Epoch: 16,  Batch: 300 of 550,  Cost: 3.8897,  AvgTime: 1.86ms
Step: 8651,  Epoch: 16,  Batch: 400 of 550,  Cost: 3.7968,  AvgTime: 1.83ms
Step: 8751,  Epoch: 16,  Batch: 500 of 550,  Cost: 3.7267,  AvgTime: 1.82ms
Step: 8801,  Epoch: 16,  Batch: 550 of 550,  Cost: 3.6240,  AvgTime: 0.92ms
Step: 8901,  Epoch: 17,  Batch: 100 of 550,  Cost: 4.1018,  AvgTime: 2.40ms
Step: 9001,  Epoch: 17,  Batch: 200 of 550,  Cost: 4.0881,  AvgTime: 1.90ms
Step: 9101,  Epoch: 17,  Batch: 300 of 550,  Cost: 3.4485,  AvgTime: 1.85ms
Step: 9201,  Epoch: 17,  Batch: 400 of 550,  Cost: 3.8627,  AvgTime: 1.85ms
Step: 9301,  Epoch: 17,  Batch: 500 of 550,  Cost: 3.4397,  AvgTime: 1.84ms
Step: 9351,  Epoch: 17,  Batch: 550 of 550,  Cost: 4.3097,  AvgTime: 0.94ms
Step: 9451,  Epoch: 18,  Batch: 100 of 550,  Cost: 3.5674,  AvgTime: 2.50ms
Step: 9551,  Epoch: 18,  Batch: 200 of 550,  Cost: 4.4662,  AvgTime: 1.87ms
Step: 9651,  Epoch: 18,  Batch: 300 of 550,  Cost: 3.7075,  AvgTime: 1.85ms
Step: 9751,  Epoch: 18,  Batch: 400 of 550,  Cost: 3.9736,  AvgTime: 1.82ms
Step: 9851,  Epoch: 18,  Batch: 500 of 550,  Cost: 4.0748,  AvgTime: 1.84ms
Step: 9901,  Epoch: 18,  Batch: 550 of 550,  Cost: 3.5877,  AvgTime: 0.93ms
Step: 10001,  Epoch: 19,  Batch: 100 of 550,  Cost: 3.7883,  AvgTime: 2.42ms
Step: 10101,  Epoch: 19,  Batch: 200 of 550,  Cost: 3.7816,  AvgTime: 1.85ms
Step: 10201,  Epoch: 19,  Batch: 300 of 550,  Cost: 3.8793,  AvgTime: 1.85ms
Step: 10301,  Epoch: 19,  Batch: 400 of 550,  Cost: 3.9815,  AvgTime: 1.81ms
Step: 10401,  Epoch: 19,  Batch: 500 of 550,  Cost: 3.4859,  AvgTime: 1.85ms
Step: 10451,  Epoch: 19,  Batch: 550 of 550,  Cost: 3.8769,  AvgTime: 0.93ms
Step: 10551,  Epoch: 20,  Batch: 100 of 550,  Cost: 3.5068,  AvgTime: 2.54ms
Step: 10651,  Epoch: 20,  Batch: 200 of 550,  Cost: 3.4267,  AvgTime: 1.86ms
Step: 10751,  Epoch: 20,  Batch: 300 of 550,  Cost: 3.5571,  AvgTime: 1.80ms
Step: 10851,  Epoch: 20,  Batch: 400 of 550,  Cost: 3.3178,  AvgTime: 1.84ms
Step: 10951,  Epoch: 20,  Batch: 500 of 550,  Cost: 4.2102,  AvgTime: 1.83ms
Step: 11001,  Epoch: 20,  Batch: 550 of 550,  Cost: 3.9396,  AvgTime: 0.94ms
Test-Accuracy: 0.28
Total Time: 21.75s
Final Cost: 3.9396
done
```

Distributed

```
172.17.0.6 ps 0
172.17.0.7 worker 0
172.17.0.8 worker 1
172.17.0.9 worker 2
```

172.17.0.7 worker 0
```bash
root@2d286f371ae1:~/tensorflow-example# python3 isac.py --job_name="worker" --task_index=0
2017-10-30 13:56:05.964870: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-10-30 13:56:05.965992: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_UNKNOWN
2017-10-30 13:56:05.966053: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:152] no NVIDIA GPU device is present: /dev/nvidia0 does not exist
E1030 13:56:05.966240503   11051 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-10-30 13:56:05.973078: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.6:2222}
2017-10-30 13:56:05.973183: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.8:2222, 2 -> 172.17.0.9:2222}
2017-10-30 13:56:05.974092: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
Variables initialized ...
2017-10-30 13:56:09.813486: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 7d124e627930e634 with config: 
WARNING:tensorflow:Standard services need a 'logdir' passed to the SessionManager
Step: 323,  Epoch:  1,  Batch: 100 of 550,  Cost: 8.0130,  AvgTime: 7.66ms
Step: 628,  Epoch:  1,  Batch: 200 of 550,  Cost: 7.9205,  AvgTime: 7.02ms
Step: 922,  Epoch:  1,  Batch: 300 of 550,  Cost: 6.6985,  AvgTime: 6.77ms
Step: 1225,  Epoch:  1,  Batch: 400 of 550,  Cost: 6.7547,  AvgTime: 6.99ms
Step: 1510,  Epoch:  1,  Batch: 500 of 550,  Cost: 5.1637,  AvgTime: 6.75ms
Step: 1649,  Epoch:  1,  Batch: 550 of 550,  Cost: 6.2986,  AvgTime: 3.41ms
Step: 1969,  Epoch:  2,  Batch: 100 of 550,  Cost: 5.8836,  AvgTime: 7.68ms
Step: 2270,  Epoch:  2,  Batch: 200 of 550,  Cost: 5.2364,  AvgTime: 6.88ms
Step: 2569,  Epoch:  2,  Batch: 300 of 550,  Cost: 4.7818,  AvgTime: 6.89ms
Step: 2881,  Epoch:  2,  Batch: 400 of 550,  Cost: 5.3908,  AvgTime: 7.12ms
Step: 3177,  Epoch:  2,  Batch: 500 of 550,  Cost: 4.7687,  AvgTime: 7.17ms
Step: 3316,  Epoch:  2,  Batch: 550 of 550,  Cost: 4.4412,  AvgTime: 3.48ms
Step: 3630,  Epoch:  3,  Batch: 100 of 550,  Cost: 5.2354,  AvgTime: 7.56ms
Step: 3929,  Epoch:  3,  Batch: 200 of 550,  Cost: 5.5947,  AvgTime: 6.83ms
Step: 4230,  Epoch:  3,  Batch: 300 of 550,  Cost: 5.4431,  AvgTime: 6.81ms
Step: 4535,  Epoch:  3,  Batch: 400 of 550,  Cost: 5.6250,  AvgTime: 6.95ms
Step: 4820,  Epoch:  3,  Batch: 500 of 550,  Cost: 4.2648,  AvgTime: 6.89ms
Step: 4961,  Epoch:  3,  Batch: 550 of 550,  Cost: 4.6853,  AvgTime: 3.49ms
Step: 5282,  Epoch:  4,  Batch: 100 of 550,  Cost: 4.6951,  AvgTime: 7.65ms
Step: 5576,  Epoch:  4,  Batch: 200 of 550,  Cost: 4.5051,  AvgTime: 6.78ms
Step: 5882,  Epoch:  4,  Batch: 300 of 550,  Cost: 4.8619,  AvgTime: 6.98ms
Step: 6175,  Epoch:  4,  Batch: 400 of 550,  Cost: 4.4956,  AvgTime: 6.67ms
Step: 6467,  Epoch:  4,  Batch: 500 of 550,  Cost: 4.4217,  AvgTime: 6.97ms
Step: 6610,  Epoch:  4,  Batch: 550 of 550,  Cost: 4.6963,  AvgTime: 3.37ms
Step: 6926,  Epoch:  5,  Batch: 100 of 550,  Cost: 4.1808,  AvgTime: 7.76ms
Step: 7235,  Epoch:  5,  Batch: 200 of 550,  Cost: 4.4014,  AvgTime: 7.09ms
Step: 7529,  Epoch:  5,  Batch: 300 of 550,  Cost: 4.0674,  AvgTime: 6.80ms
Step: 7834,  Epoch:  5,  Batch: 400 of 550,  Cost: 3.9788,  AvgTime: 6.93ms
Step: 8124,  Epoch:  5,  Batch: 500 of 550,  Cost: 4.7550,  AvgTime: 6.94ms
Step: 8268,  Epoch:  5,  Batch: 550 of 550,  Cost: 4.0674,  AvgTime: 3.46ms
Step: 8581,  Epoch:  6,  Batch: 100 of 550,  Cost: 3.2985,  AvgTime: 7.64ms
Step: 8881,  Epoch:  6,  Batch: 200 of 550,  Cost: 3.7770,  AvgTime: 6.88ms
Step: 9180,  Epoch:  6,  Batch: 300 of 550,  Cost: 4.2799,  AvgTime: 6.83ms
Step: 9475,  Epoch:  6,  Batch: 400 of 550,  Cost: 3.5545,  AvgTime: 6.81ms
Step: 9774,  Epoch:  6,  Batch: 500 of 550,  Cost: 3.9732,  AvgTime: 7.15ms
Step: 9915,  Epoch:  6,  Batch: 550 of 550,  Cost: 4.0003,  AvgTime: 3.46ms
Step: 10229,  Epoch:  7,  Batch: 100 of 550,  Cost: 4.3231,  AvgTime: 7.66ms
Step: 10520,  Epoch:  7,  Batch: 200 of 550,  Cost: 3.2128,  AvgTime: 6.62ms
Step: 10817,  Epoch:  7,  Batch: 300 of 550,  Cost: 3.6272,  AvgTime: 6.79ms
Step: 11110,  Epoch:  7,  Batch: 400 of 550,  Cost: 3.3275,  AvgTime: 6.75ms
Step: 11401,  Epoch:  7,  Batch: 500 of 550,  Cost: 3.8873,  AvgTime: 6.91ms
Step: 11553,  Epoch:  7,  Batch: 550 of 550,  Cost: 3.3907,  AvgTime: 3.52ms
Step: 11865,  Epoch:  8,  Batch: 100 of 550,  Cost: 3.4472,  AvgTime: 7.80ms
Step: 12167,  Epoch:  8,  Batch: 200 of 550,  Cost: 3.2880,  AvgTime: 6.88ms
Step: 12472,  Epoch:  8,  Batch: 300 of 550,  Cost: 2.7876,  AvgTime: 6.98ms
Step: 12768,  Epoch:  8,  Batch: 400 of 550,  Cost: 3.5377,  AvgTime: 6.78ms
Step: 13062,  Epoch:  8,  Batch: 500 of 550,  Cost: 3.3089,  AvgTime: 7.08ms
Step: 13213,  Epoch:  8,  Batch: 550 of 550,  Cost: 3.8207,  AvgTime: 3.50ms
Step: 13511,  Epoch:  9,  Batch: 100 of 550,  Cost: 3.4736,  AvgTime: 7.44ms
Step: 13804,  Epoch:  9,  Batch: 200 of 550,  Cost: 3.1147,  AvgTime: 6.71ms
Step: 14104,  Epoch:  9,  Batch: 300 of 550,  Cost: 3.2752,  AvgTime: 6.95ms
Step: 14409,  Epoch:  9,  Batch: 400 of 550,  Cost: 2.8697,  AvgTime: 6.92ms
Step: 14698,  Epoch:  9,  Batch: 500 of 550,  Cost: 3.1282,  AvgTime: 7.03ms
Step: 14850,  Epoch:  9,  Batch: 550 of 550,  Cost: 2.9043,  AvgTime: 3.44ms
Step: 15157,  Epoch: 10,  Batch: 100 of 550,  Cost: 2.7438,  AvgTime: 7.66ms
Step: 15462,  Epoch: 10,  Batch: 200 of 550,  Cost: 2.9382,  AvgTime: 7.01ms
Step: 15765,  Epoch: 10,  Batch: 300 of 550,  Cost: 2.7797,  AvgTime: 6.97ms
Step: 16063,  Epoch: 10,  Batch: 400 of 550,  Cost: 2.9750,  AvgTime: 6.90ms
Step: 16353,  Epoch: 10,  Batch: 500 of 550,  Cost: 3.0788,  AvgTime: 6.89ms
Step: 16504,  Epoch: 10,  Batch: 550 of 550,  Cost: 2.6676,  AvgTime: 3.48ms
Step: 16814,  Epoch: 11,  Batch: 100 of 550,  Cost: 3.4074,  AvgTime: 7.79ms
Step: 17117,  Epoch: 11,  Batch: 200 of 550,  Cost: 2.7658,  AvgTime: 6.92ms
Step: 17432,  Epoch: 11,  Batch: 300 of 550,  Cost: 2.5751,  AvgTime: 7.21ms
Step: 17730,  Epoch: 11,  Batch: 400 of 550,  Cost: 2.5423,  AvgTime: 6.84ms
Step: 18019,  Epoch: 11,  Batch: 500 of 550,  Cost: 2.8442,  AvgTime: 7.00ms
Step: 18163,  Epoch: 11,  Batch: 550 of 550,  Cost: 2.6327,  AvgTime: 3.39ms
Step: 18473,  Epoch: 12,  Batch: 100 of 550,  Cost: 2.3739,  AvgTime: 7.66ms
Step: 18774,  Epoch: 12,  Batch: 200 of 550,  Cost: 3.0102,  AvgTime: 6.87ms
Step: 19066,  Epoch: 12,  Batch: 300 of 550,  Cost: 2.4884,  AvgTime: 6.61ms
Step: 19362,  Epoch: 12,  Batch: 400 of 550,  Cost: 2.3533,  AvgTime: 6.80ms
Step: 19641,  Epoch: 12,  Batch: 500 of 550,  Cost: 2.8700,  AvgTime: 6.78ms
Step: 19791,  Epoch: 12,  Batch: 550 of 550,  Cost: 2.6283,  AvgTime: 3.42ms
Step: 20098,  Epoch: 13,  Batch: 100 of 550,  Cost: 2.9138,  AvgTime: 7.73ms
Step: 20391,  Epoch: 13,  Batch: 200 of 550,  Cost: 2.3343,  AvgTime: 6.76ms
Step: 20691,  Epoch: 13,  Batch: 300 of 550,  Cost: 2.4563,  AvgTime: 6.86ms
Step: 20991,  Epoch: 13,  Batch: 400 of 550,  Cost: 2.1555,  AvgTime: 7.01ms
Step: 21280,  Epoch: 13,  Batch: 500 of 550,  Cost: 2.7186,  AvgTime: 6.77ms
Step: 21431,  Epoch: 13,  Batch: 550 of 550,  Cost: 2.9044,  AvgTime: 3.63ms
Step: 21749,  Epoch: 14,  Batch: 100 of 550,  Cost: 2.9610,  AvgTime: 7.94ms
Step: 22057,  Epoch: 14,  Batch: 200 of 550,  Cost: 2.2696,  AvgTime: 7.09ms
Step: 22356,  Epoch: 14,  Batch: 300 of 550,  Cost: 2.2434,  AvgTime: 6.84ms
Step: 22651,  Epoch: 14,  Batch: 400 of 550,  Cost: 2.2135,  AvgTime: 6.75ms
Step: 22939,  Epoch: 14,  Batch: 500 of 550,  Cost: 1.9113,  AvgTime: 6.86ms
Step: 23088,  Epoch: 14,  Batch: 550 of 550,  Cost: 2.4710,  AvgTime: 3.46ms
Step: 23395,  Epoch: 15,  Batch: 100 of 550,  Cost: 2.1838,  AvgTime: 7.75ms
Step: 23694,  Epoch: 15,  Batch: 200 of 550,  Cost: 2.4930,  AvgTime: 6.83ms
Step: 23989,  Epoch: 15,  Batch: 300 of 550,  Cost: 2.2932,  AvgTime: 6.77ms
Step: 24283,  Epoch: 15,  Batch: 400 of 550,  Cost: 2.4008,  AvgTime: 6.76ms
Step: 24580,  Epoch: 15,  Batch: 500 of 550,  Cost: 2.1669,  AvgTime: 6.90ms
Step: 24721,  Epoch: 15,  Batch: 550 of 550,  Cost: 2.2112,  AvgTime: 3.52ms
Step: 25029,  Epoch: 16,  Batch: 100 of 550,  Cost: 2.2468,  AvgTime: 7.81ms
Step: 25328,  Epoch: 16,  Batch: 200 of 550,  Cost: 2.1220,  AvgTime: 6.91ms
Step: 25629,  Epoch: 16,  Batch: 300 of 550,  Cost: 2.7248,  AvgTime: 6.94ms
Step: 25940,  Epoch: 16,  Batch: 400 of 550,  Cost: 2.3142,  AvgTime: 7.10ms
Step: 26239,  Epoch: 16,  Batch: 500 of 550,  Cost: 2.1220,  AvgTime: 7.16ms
Step: 26390,  Epoch: 16,  Batch: 550 of 550,  Cost: 1.6860,  AvgTime: 3.58ms
Step: 26696,  Epoch: 17,  Batch: 100 of 550,  Cost: 2.0388,  AvgTime: 7.74ms
Step: 26995,  Epoch: 17,  Batch: 200 of 550,  Cost: 2.3130,  AvgTime: 6.86ms
Step: 27298,  Epoch: 17,  Batch: 300 of 550,  Cost: 2.5237,  AvgTime: 6.97ms
Step: 27599,  Epoch: 17,  Batch: 400 of 550,  Cost: 2.1731,  AvgTime: 6.94ms
Step: 27892,  Epoch: 17,  Batch: 500 of 550,  Cost: 2.0728,  AvgTime: 7.07ms
Step: 28047,  Epoch: 17,  Batch: 550 of 550,  Cost: 2.0668,  AvgTime: 3.55ms
Step: 28363,  Epoch: 18,  Batch: 100 of 550,  Cost: 2.2246,  AvgTime: 7.89ms
Step: 28663,  Epoch: 18,  Batch: 200 of 550,  Cost: 2.3460,  AvgTime: 6.95ms
Step: 28968,  Epoch: 18,  Batch: 300 of 550,  Cost: 2.1972,  AvgTime: 7.03ms
Step: 29274,  Epoch: 18,  Batch: 400 of 550,  Cost: 1.9391,  AvgTime: 7.00ms
Step: 29555,  Epoch: 18,  Batch: 500 of 550,  Cost: 2.2870,  AvgTime: 6.77ms
Step: 29700,  Epoch: 18,  Batch: 550 of 550,  Cost: 1.3754,  AvgTime: 3.30ms
Step: 30002,  Epoch: 19,  Batch: 100 of 550,  Cost: 2.2759,  AvgTime: 7.62ms
Step: 30305,  Epoch: 19,  Batch: 200 of 550,  Cost: 2.6023,  AvgTime: 6.98ms
Step: 30602,  Epoch: 19,  Batch: 300 of 550,  Cost: 2.1196,  AvgTime: 6.85ms
Step: 30895,  Epoch: 19,  Batch: 400 of 550,  Cost: 2.1535,  AvgTime: 6.78ms
Step: 31179,  Epoch: 19,  Batch: 500 of 550,  Cost: 1.9272,  AvgTime: 6.78ms
Step: 31335,  Epoch: 19,  Batch: 550 of 550,  Cost: 1.8468,  AvgTime: 3.73ms
Step: 31646,  Epoch: 20,  Batch: 100 of 550,  Cost: 2.0427,  AvgTime: 7.85ms
Step: 31946,  Epoch: 20,  Batch: 200 of 550,  Cost: 2.0281,  AvgTime: 6.76ms
Step: 32251,  Epoch: 20,  Batch: 300 of 550,  Cost: 1.4883,  AvgTime: 6.99ms
Step: 32550,  Epoch: 20,  Batch: 400 of 550,  Cost: 1.9323,  AvgTime: 6.87ms
Step: 32837,  Epoch: 20,  Batch: 500 of 550,  Cost: 1.7831,  AvgTime: 7.07ms
Step: 32940,  Epoch: 20,  Batch: 550 of 550,  Cost: 2.1700,  AvgTime: 3.20ms
Test-Accuracy: 0.51
Total Time: 80.68s
Final Cost: 2.1700
done
```
172.17.0.8 worker 1
```bash
root@0b2aa5d32aa3:~/tensorflow-example# python3 isac.py --job_name="worker" --task_index=1 
2017-10-30 13:56:07.592702: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-10-30 13:56:07.593678: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_UNKNOWN
2017-10-30 13:56:07.593733: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:152] no NVIDIA GPU device is present: /dev/nvidia0 does not exist
E1030 13:56:07.593896044   11049 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-10-30 13:56:07.597715: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.6:2222}
2017-10-30 13:56:07.597780: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.7:2222, 1 -> localhost:2222, 2 -> 172.17.0.9:2222}
2017-10-30 13:56:07.598575: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
Variables initialized ...
2017-10-30 13:56:09.456191: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 39fb3686fd7f39b1 with config: 
Step: 129,  Epoch:  1,  Batch: 100 of 550,  Cost: 9.8952,  AvgTime: 6.84ms
Step: 436,  Epoch:  1,  Batch: 200 of 550,  Cost: 9.0960,  AvgTime: 7.06ms
Step: 739,  Epoch:  1,  Batch: 300 of 550,  Cost: 7.3113,  AvgTime: 7.01ms
Step: 1035,  Epoch:  1,  Batch: 400 of 550,  Cost: 6.5938,  AvgTime: 6.75ms
Step: 1335,  Epoch:  1,  Batch: 500 of 550,  Cost: 5.8586,  AvgTime: 6.96ms
Step: 1485,  Epoch:  1,  Batch: 550 of 550,  Cost: 5.7137,  AvgTime: 3.36ms
Step: 1792,  Epoch:  2,  Batch: 100 of 550,  Cost: 5.6149,  AvgTime: 7.91ms
Step: 2087,  Epoch:  2,  Batch: 200 of 550,  Cost: 5.5487,  AvgTime: 6.79ms
Step: 2379,  Epoch:  2,  Batch: 300 of 550,  Cost: 5.1688,  AvgTime: 6.68ms
Step: 2680,  Epoch:  2,  Batch: 400 of 550,  Cost: 5.1250,  AvgTime: 6.88ms
Step: 2968,  Epoch:  2,  Batch: 500 of 550,  Cost: 5.6455,  AvgTime: 6.60ms
Step: 3114,  Epoch:  2,  Batch: 550 of 550,  Cost: 5.5275,  AvgTime: 3.35ms
Step: 3420,  Epoch:  3,  Batch: 100 of 550,  Cost: 4.7275,  AvgTime: 8.03ms
Step: 3722,  Epoch:  3,  Batch: 200 of 550,  Cost: 4.9058,  AvgTime: 6.91ms
Step: 4027,  Epoch:  3,  Batch: 300 of 550,  Cost: 5.1450,  AvgTime: 6.95ms
Step: 4321,  Epoch:  3,  Batch: 400 of 550,  Cost: 4.1691,  AvgTime: 6.67ms
Step: 4615,  Epoch:  3,  Batch: 500 of 550,  Cost: 5.0860,  AvgTime: 6.75ms
Step: 4768,  Epoch:  3,  Batch: 550 of 550,  Cost: 4.2436,  AvgTime: 3.55ms
Step: 5068,  Epoch:  4,  Batch: 100 of 550,  Cost: 4.6336,  AvgTime: 7.76ms
Step: 5369,  Epoch:  4,  Batch: 200 of 550,  Cost: 4.4546,  AvgTime: 6.88ms
Step: 5663,  Epoch:  4,  Batch: 300 of 550,  Cost: 4.4591,  AvgTime: 6.73ms
Step: 5966,  Epoch:  4,  Batch: 400 of 550,  Cost: 4.7443,  AvgTime: 6.92ms
Step: 6265,  Epoch:  4,  Batch: 500 of 550,  Cost: 4.7722,  AvgTime: 6.79ms
Step: 6416,  Epoch:  4,  Batch: 550 of 550,  Cost: 4.7561,  AvgTime: 3.45ms
Step: 6715,  Epoch:  5,  Batch: 100 of 550,  Cost: 4.3239,  AvgTime: 7.78ms
Step: 7011,  Epoch:  5,  Batch: 200 of 550,  Cost: 4.4040,  AvgTime: 6.79ms
Step: 7304,  Epoch:  5,  Batch: 300 of 550,  Cost: 4.3175,  AvgTime: 6.73ms
Step: 7607,  Epoch:  5,  Batch: 400 of 550,  Cost: 3.7616,  AvgTime: 7.00ms
Step: 7900,  Epoch:  5,  Batch: 500 of 550,  Cost: 4.1093,  AvgTime: 6.66ms
Step: 8051,  Epoch:  5,  Batch: 550 of 550,  Cost: 4.0192,  AvgTime: 3.47ms
Step: 8352,  Epoch:  6,  Batch: 100 of 550,  Cost: 3.9199,  AvgTime: 7.75ms
Step: 8659,  Epoch:  6,  Batch: 200 of 550,  Cost: 3.6632,  AvgTime: 7.07ms
Step: 8957,  Epoch:  6,  Batch: 300 of 550,  Cost: 3.9967,  AvgTime: 6.85ms
Step: 9252,  Epoch:  6,  Batch: 400 of 550,  Cost: 3.5982,  AvgTime: 6.77ms
Step: 9558,  Epoch:  6,  Batch: 500 of 550,  Cost: 4.0798,  AvgTime: 7.07ms
Step: 9707,  Epoch:  6,  Batch: 550 of 550,  Cost: 3.5491,  AvgTime: 3.34ms
Step: 10006,  Epoch:  7,  Batch: 100 of 550,  Cost: 3.3762,  AvgTime: 7.91ms
Step: 10302,  Epoch:  7,  Batch: 200 of 550,  Cost: 3.9202,  AvgTime: 6.76ms
Step: 10603,  Epoch:  7,  Batch: 300 of 550,  Cost: 3.4447,  AvgTime: 6.87ms
Step: 10904,  Epoch:  7,  Batch: 400 of 550,  Cost: 3.4446,  AvgTime: 6.86ms
Step: 11199,  Epoch:  7,  Batch: 500 of 550,  Cost: 3.8583,  AvgTime: 6.78ms
Step: 11356,  Epoch:  7,  Batch: 550 of 550,  Cost: 3.1550,  AvgTime: 3.54ms
Step: 11649,  Epoch:  8,  Batch: 100 of 550,  Cost: 3.4440,  AvgTime: 7.68ms
Step: 11954,  Epoch:  8,  Batch: 200 of 550,  Cost: 3.2115,  AvgTime: 7.01ms
Step: 12252,  Epoch:  8,  Batch: 300 of 550,  Cost: 3.3424,  AvgTime: 6.78ms
Step: 12557,  Epoch:  8,  Batch: 400 of 550,  Cost: 3.2863,  AvgTime: 7.05ms
Step: 12855,  Epoch:  8,  Batch: 500 of 550,  Cost: 2.9295,  AvgTime: 6.81ms
Step: 13002,  Epoch:  8,  Batch: 550 of 550,  Cost: 3.8963,  AvgTime: 3.36ms
Step: 13304,  Epoch:  9,  Batch: 100 of 550,  Cost: 2.9014,  AvgTime: 7.93ms
Step: 13615,  Epoch:  9,  Batch: 200 of 550,  Cost: 2.5563,  AvgTime: 7.08ms
Step: 13920,  Epoch:  9,  Batch: 300 of 550,  Cost: 3.2482,  AvgTime: 6.98ms
Step: 14219,  Epoch:  9,  Batch: 400 of 550,  Cost: 3.5561,  AvgTime: 6.92ms
Step: 14511,  Epoch:  9,  Batch: 500 of 550,  Cost: 2.9721,  AvgTime: 6.61ms
Step: 14657,  Epoch:  9,  Batch: 550 of 550,  Cost: 3.2007,  AvgTime: 3.42ms
Step: 14952,  Epoch: 10,  Batch: 100 of 550,  Cost: 3.3554,  AvgTime: 7.66ms
Step: 15249,  Epoch: 10,  Batch: 200 of 550,  Cost: 3.1003,  AvgTime: 6.82ms
Step: 15547,  Epoch: 10,  Batch: 300 of 550,  Cost: 3.1202,  AvgTime: 6.89ms
Step: 15851,  Epoch: 10,  Batch: 400 of 550,  Cost: 2.7711,  AvgTime: 7.00ms
Step: 16145,  Epoch: 10,  Batch: 500 of 550,  Cost: 2.8069,  AvgTime: 6.81ms
Step: 16294,  Epoch: 10,  Batch: 550 of 550,  Cost: 2.4831,  AvgTime: 3.36ms
Step: 16602,  Epoch: 11,  Batch: 100 of 550,  Cost: 2.9385,  AvgTime: 8.04ms
Step: 16893,  Epoch: 11,  Batch: 200 of 550,  Cost: 2.5944,  AvgTime: 6.67ms
Step: 17194,  Epoch: 11,  Batch: 300 of 550,  Cost: 2.8875,  AvgTime: 6.92ms
Step: 17487,  Epoch: 11,  Batch: 400 of 550,  Cost: 2.5286,  AvgTime: 6.70ms
Step: 17788,  Epoch: 11,  Batch: 500 of 550,  Cost: 2.5795,  AvgTime: 6.88ms
Step: 17940,  Epoch: 11,  Batch: 550 of 550,  Cost: 2.7772,  AvgTime: 3.50ms
Step: 18252,  Epoch: 12,  Batch: 100 of 550,  Cost: 2.6592,  AvgTime: 8.16ms
Step: 18546,  Epoch: 12,  Batch: 200 of 550,  Cost: 2.6329,  AvgTime: 6.77ms
Step: 18849,  Epoch: 12,  Batch: 300 of 550,  Cost: 2.7288,  AvgTime: 6.88ms
Step: 19156,  Epoch: 12,  Batch: 400 of 550,  Cost: 2.6357,  AvgTime: 6.95ms
Step: 19458,  Epoch: 12,  Batch: 500 of 550,  Cost: 2.6443,  AvgTime: 6.96ms
Step: 19606,  Epoch: 12,  Batch: 550 of 550,  Cost: 3.2461,  AvgTime: 3.41ms
Step: 19907,  Epoch: 13,  Batch: 100 of 550,  Cost: 2.5474,  AvgTime: 7.94ms
Step: 20214,  Epoch: 13,  Batch: 200 of 550,  Cost: 2.9928,  AvgTime: 7.11ms
Step: 20518,  Epoch: 13,  Batch: 300 of 550,  Cost: 2.1938,  AvgTime: 6.94ms
Step: 20816,  Epoch: 13,  Batch: 400 of 550,  Cost: 2.7750,  AvgTime: 6.83ms
Step: 21116,  Epoch: 13,  Batch: 500 of 550,  Cost: 2.3956,  AvgTime: 6.98ms
Step: 21265,  Epoch: 13,  Batch: 550 of 550,  Cost: 2.7791,  AvgTime: 3.43ms
Step: 21568,  Epoch: 14,  Batch: 100 of 550,  Cost: 2.6660,  AvgTime: 7.91ms
Step: 21870,  Epoch: 14,  Batch: 200 of 550,  Cost: 2.5855,  AvgTime: 6.91ms
Step: 22164,  Epoch: 14,  Batch: 300 of 550,  Cost: 2.3205,  AvgTime: 6.75ms
Step: 22463,  Epoch: 14,  Batch: 400 of 550,  Cost: 2.7497,  AvgTime: 6.86ms
Step: 22758,  Epoch: 14,  Batch: 500 of 550,  Cost: 2.6160,  AvgTime: 6.78ms
Step: 22910,  Epoch: 14,  Batch: 550 of 550,  Cost: 3.0588,  AvgTime: 3.39ms
Step: 23218,  Epoch: 15,  Batch: 100 of 550,  Cost: 2.2879,  AvgTime: 8.15ms
Step: 23518,  Epoch: 15,  Batch: 200 of 550,  Cost: 2.6175,  AvgTime: 6.88ms
Step: 23819,  Epoch: 15,  Batch: 300 of 550,  Cost: 2.5959,  AvgTime: 6.89ms
Step: 24125,  Epoch: 15,  Batch: 400 of 550,  Cost: 2.8026,  AvgTime: 7.07ms
Step: 24429,  Epoch: 15,  Batch: 500 of 550,  Cost: 1.9207,  AvgTime: 6.98ms
Step: 24575,  Epoch: 15,  Batch: 550 of 550,  Cost: 1.6555,  AvgTime: 3.36ms
Step: 24880,  Epoch: 16,  Batch: 100 of 550,  Cost: 1.9533,  AvgTime: 8.05ms
Step: 25187,  Epoch: 16,  Batch: 200 of 550,  Cost: 2.3605,  AvgTime: 7.13ms
Step: 25489,  Epoch: 16,  Batch: 300 of 550,  Cost: 2.2720,  AvgTime: 6.95ms
Step: 25783,  Epoch: 16,  Batch: 400 of 550,  Cost: 2.3449,  AvgTime: 6.74ms
Step: 26076,  Epoch: 16,  Batch: 500 of 550,  Cost: 1.5620,  AvgTime: 6.72ms
Step: 26220,  Epoch: 16,  Batch: 550 of 550,  Cost: 1.9629,  AvgTime: 3.33ms
Step: 26519,  Epoch: 17,  Batch: 100 of 550,  Cost: 1.9532,  AvgTime: 7.96ms
Step: 26818,  Epoch: 17,  Batch: 200 of 550,  Cost: 2.3799,  AvgTime: 6.84ms
Step: 27113,  Epoch: 17,  Batch: 300 of 550,  Cost: 2.6996,  AvgTime: 6.76ms
Step: 27412,  Epoch: 17,  Batch: 400 of 550,  Cost: 2.3061,  AvgTime: 6.96ms
Step: 27712,  Epoch: 17,  Batch: 500 of 550,  Cost: 2.0807,  AvgTime: 6.86ms
Step: 27862,  Epoch: 17,  Batch: 550 of 550,  Cost: 2.1188,  AvgTime: 3.47ms
Step: 28161,  Epoch: 18,  Batch: 100 of 550,  Cost: 2.1082,  AvgTime: 7.84ms
Step: 28459,  Epoch: 18,  Batch: 200 of 550,  Cost: 2.2697,  AvgTime: 6.75ms
Step: 28754,  Epoch: 18,  Batch: 300 of 550,  Cost: 2.0841,  AvgTime: 6.91ms
Step: 29054,  Epoch: 18,  Batch: 400 of 550,  Cost: 2.0052,  AvgTime: 6.89ms
Step: 29348,  Epoch: 18,  Batch: 500 of 550,  Cost: 2.1805,  AvgTime: 6.73ms
Step: 29495,  Epoch: 18,  Batch: 550 of 550,  Cost: 2.9347,  AvgTime: 3.36ms
Step: 29807,  Epoch: 19,  Batch: 100 of 550,  Cost: 1.7471,  AvgTime: 8.11ms
Step: 30098,  Epoch: 19,  Batch: 200 of 550,  Cost: 2.0372,  AvgTime: 6.70ms
Step: 30398,  Epoch: 19,  Batch: 300 of 550,  Cost: 1.9240,  AvgTime: 6.95ms
Step: 30703,  Epoch: 19,  Batch: 400 of 550,  Cost: 2.1627,  AvgTime: 6.98ms
Step: 31008,  Epoch: 19,  Batch: 500 of 550,  Cost: 1.5698,  AvgTime: 7.04ms
Step: 31158,  Epoch: 19,  Batch: 550 of 550,  Cost: 2.0342,  AvgTime: 3.49ms
Step: 31457,  Epoch: 20,  Batch: 100 of 550,  Cost: 1.8542,  AvgTime: 7.93ms
Step: 31747,  Epoch: 20,  Batch: 200 of 550,  Cost: 1.9151,  AvgTime: 6.70ms
Step: 32052,  Epoch: 20,  Batch: 300 of 550,  Cost: 1.8719,  AvgTime: 6.89ms
Step: 32353,  Epoch: 20,  Batch: 400 of 550,  Cost: 1.8238,  AvgTime: 6.84ms
Step: 32652,  Epoch: 20,  Batch: 500 of 550,  Cost: 1.8916,  AvgTime: 6.87ms
Step: 32803,  Epoch: 20,  Batch: 550 of 550,  Cost: 2.0667,  AvgTime: 3.50ms
Test-Accuracy: 0.51
Total Time: 78.60s
Final Cost: 2.0667
done
```

172.17.0.9 worker 2
```bash
root@f5342e7d6059:~/tensorflow-example# python3 isac.py --job_name="worker" --task_index=2 
2017-10-30 13:56:08.814962: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-10-30 13:56:08.816167: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_UNKNOWN
2017-10-30 13:56:08.816216: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:152] no NVIDIA GPU device is present: /dev/nvidia0 does not exist
E1030 13:56:08.816376656   11048 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-10-30 13:56:08.820364: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.6:2222}
2017-10-30 13:56:08.820434: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.7:2222, 1 -> 172.17.0.8:2222, 2 -> localhost:2222}
2017-10-30 13:56:08.820829: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
Variables initialized ...
2017-10-30 13:56:09.705410: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 478830408394c48b with config: 
Step: 279,  Epoch:  1,  Batch: 100 of 550,  Cost: 7.8926,  AvgTime: 7.85ms
Step: 578,  Epoch:  1,  Batch: 200 of 550,  Cost: 7.6162,  AvgTime: 6.84ms
Step: 883,  Epoch:  1,  Batch: 300 of 550,  Cost: 6.7549,  AvgTime: 7.06ms
Step: 1183,  Epoch:  1,  Batch: 400 of 550,  Cost: 6.6968,  AvgTime: 6.85ms
Step: 1488,  Epoch:  1,  Batch: 500 of 550,  Cost: 5.6346,  AvgTime: 7.02ms
Step: 1633,  Epoch:  1,  Batch: 550 of 550,  Cost: 6.6912,  AvgTime: 3.56ms
Step: 1938,  Epoch:  2,  Batch: 100 of 550,  Cost: 6.0191,  AvgTime: 7.62ms
Step: 2241,  Epoch:  2,  Batch: 200 of 550,  Cost: 5.8749,  AvgTime: 6.93ms
Step: 2546,  Epoch:  2,  Batch: 300 of 550,  Cost: 5.3113,  AvgTime: 7.01ms
Step: 2844,  Epoch:  2,  Batch: 400 of 550,  Cost: 5.0104,  AvgTime: 6.80ms
Step: 3133,  Epoch:  2,  Batch: 500 of 550,  Cost: 4.8902,  AvgTime: 6.88ms
Step: 3283,  Epoch:  2,  Batch: 550 of 550,  Cost: 4.4711,  AvgTime: 3.50ms
Step: 3592,  Epoch:  3,  Batch: 100 of 550,  Cost: 5.2375,  AvgTime: 7.78ms
Step: 3889,  Epoch:  3,  Batch: 200 of 550,  Cost: 4.6508,  AvgTime: 6.81ms
Step: 4189,  Epoch:  3,  Batch: 300 of 550,  Cost: 4.6019,  AvgTime: 6.83ms
Step: 4492,  Epoch:  3,  Batch: 400 of 550,  Cost: 4.4033,  AvgTime: 6.88ms
Step: 4787,  Epoch:  3,  Batch: 500 of 550,  Cost: 4.2982,  AvgTime: 7.08ms
Step: 4935,  Epoch:  3,  Batch: 550 of 550,  Cost: 4.1918,  AvgTime: 3.40ms
Step: 5247,  Epoch:  4,  Batch: 100 of 550,  Cost: 4.3241,  AvgTime: 7.72ms
Step: 5550,  Epoch:  4,  Batch: 200 of 550,  Cost: 4.7548,  AvgTime: 6.98ms
Step: 5849,  Epoch:  4,  Batch: 300 of 550,  Cost: 5.1824,  AvgTime: 6.78ms
Step: 6155,  Epoch:  4,  Batch: 400 of 550,  Cost: 3.3165,  AvgTime: 7.01ms
Step: 6444,  Epoch:  4,  Batch: 500 of 550,  Cost: 4.4617,  AvgTime: 6.93ms
Step: 6598,  Epoch:  4,  Batch: 550 of 550,  Cost: 4.2354,  AvgTime: 3.49ms
Step: 6912,  Epoch:  5,  Batch: 100 of 550,  Cost: 4.3680,  AvgTime: 7.82ms
Step: 7206,  Epoch:  5,  Batch: 200 of 550,  Cost: 4.2957,  AvgTime: 6.77ms
Step: 7504,  Epoch:  5,  Batch: 300 of 550,  Cost: 4.1968,  AvgTime: 6.86ms
Step: 7808,  Epoch:  5,  Batch: 400 of 550,  Cost: 3.7637,  AvgTime: 6.93ms
Step: 8100,  Epoch:  5,  Batch: 500 of 550,  Cost: 4.0878,  AvgTime: 6.98ms
Step: 8252,  Epoch:  5,  Batch: 550 of 550,  Cost: 3.9579,  AvgTime: 3.48ms
Step: 8555,  Epoch:  6,  Batch: 100 of 550,  Cost: 3.8508,  AvgTime: 7.58ms
Step: 8857,  Epoch:  6,  Batch: 200 of 550,  Cost: 3.9100,  AvgTime: 6.90ms
Step: 9162,  Epoch:  6,  Batch: 300 of 550,  Cost: 3.9773,  AvgTime: 6.99ms
Step: 9459,  Epoch:  6,  Batch: 400 of 550,  Cost: 3.5823,  AvgTime: 6.86ms
Step: 9744,  Epoch:  6,  Batch: 500 of 550,  Cost: 3.7791,  AvgTime: 6.84ms
Step: 9898,  Epoch:  6,  Batch: 550 of 550,  Cost: 3.8318,  AvgTime: 3.60ms
Step: 10210,  Epoch:  7,  Batch: 100 of 550,  Cost: 3.9888,  AvgTime: 7.76ms
Step: 10519,  Epoch:  7,  Batch: 200 of 550,  Cost: 3.1622,  AvgTime: 7.06ms
Step: 10824,  Epoch:  7,  Batch: 300 of 550,  Cost: 3.6644,  AvgTime: 6.98ms
Step: 11129,  Epoch:  7,  Batch: 400 of 550,  Cost: 3.2285,  AvgTime: 6.97ms
Step: 11419,  Epoch:  7,  Batch: 500 of 550,  Cost: 3.4066,  AvgTime: 6.96ms
Step: 11566,  Epoch:  7,  Batch: 550 of 550,  Cost: 3.5090,  AvgTime: 3.44ms
Step: 11879,  Epoch:  8,  Batch: 100 of 550,  Cost: 3.2229,  AvgTime: 7.72ms
Step: 12171,  Epoch:  8,  Batch: 200 of 550,  Cost: 3.2181,  AvgTime: 6.66ms
Step: 12465,  Epoch:  8,  Batch: 300 of 550,  Cost: 3.0988,  AvgTime: 6.75ms
Step: 12768,  Epoch:  8,  Batch: 400 of 550,  Cost: 2.5438,  AvgTime: 6.90ms
Step: 13058,  Epoch:  8,  Batch: 500 of 550,  Cost: 3.6056,  AvgTime: 7.04ms
Step: 13208,  Epoch:  8,  Batch: 550 of 550,  Cost: 3.0779,  AvgTime: 3.42ms
Step: 13518,  Epoch:  9,  Batch: 100 of 550,  Cost: 3.3530,  AvgTime: 7.76ms
Step: 13819,  Epoch:  9,  Batch: 200 of 550,  Cost: 2.9899,  AvgTime: 6.89ms
Step: 14116,  Epoch:  9,  Batch: 300 of 550,  Cost: 2.9030,  AvgTime: 6.85ms
Step: 14419,  Epoch:  9,  Batch: 400 of 550,  Cost: 3.3404,  AvgTime: 6.90ms
Step: 14718,  Epoch:  9,  Batch: 500 of 550,  Cost: 3.2744,  AvgTime: 7.22ms
Step: 14864,  Epoch:  9,  Batch: 550 of 550,  Cost: 3.4393,  AvgTime: 3.50ms
Step: 15182,  Epoch: 10,  Batch: 100 of 550,  Cost: 2.6632,  AvgTime: 7.78ms
Step: 15482,  Epoch: 10,  Batch: 200 of 550,  Cost: 2.4883,  AvgTime: 6.89ms
Step: 15779,  Epoch: 10,  Batch: 300 of 550,  Cost: 3.1522,  AvgTime: 6.81ms
Step: 16077,  Epoch: 10,  Batch: 400 of 550,  Cost: 3.1801,  AvgTime: 6.88ms
Step: 16373,  Epoch: 10,  Batch: 500 of 550,  Cost: 3.0289,  AvgTime: 7.04ms
Step: 16517,  Epoch: 10,  Batch: 550 of 550,  Cost: 2.8193,  AvgTime: 3.50ms
Step: 16831,  Epoch: 11,  Batch: 100 of 550,  Cost: 3.1621,  AvgTime: 7.71ms
Step: 17130,  Epoch: 11,  Batch: 200 of 550,  Cost: 2.3402,  AvgTime: 6.84ms
Step: 17423,  Epoch: 11,  Batch: 300 of 550,  Cost: 3.0913,  AvgTime: 6.71ms
Step: 17722,  Epoch: 11,  Batch: 400 of 550,  Cost: 2.7888,  AvgTime: 6.85ms
Step: 18005,  Epoch: 11,  Batch: 500 of 550,  Cost: 3.3510,  AvgTime: 6.86ms
Step: 18156,  Epoch: 11,  Batch: 550 of 550,  Cost: 2.7159,  AvgTime: 3.50ms
Step: 18473,  Epoch: 12,  Batch: 100 of 550,  Cost: 2.6567,  AvgTime: 7.89ms
Step: 18771,  Epoch: 12,  Batch: 200 of 550,  Cost: 2.9303,  AvgTime: 6.79ms
Step: 19074,  Epoch: 12,  Batch: 300 of 550,  Cost: 2.4405,  AvgTime: 6.91ms
Step: 19374,  Epoch: 12,  Batch: 400 of 550,  Cost: 2.6849,  AvgTime: 6.86ms
Step: 19672,  Epoch: 12,  Batch: 500 of 550,  Cost: 2.2152,  AvgTime: 7.22ms
Step: 19815,  Epoch: 12,  Batch: 550 of 550,  Cost: 2.4587,  AvgTime: 3.50ms
Step: 20129,  Epoch: 13,  Batch: 100 of 550,  Cost: 2.1176,  AvgTime: 7.67ms
Step: 20438,  Epoch: 13,  Batch: 200 of 550,  Cost: 2.3039,  AvgTime: 7.10ms
Step: 20731,  Epoch: 13,  Batch: 300 of 550,  Cost: 2.7820,  AvgTime: 6.69ms
Step: 21037,  Epoch: 13,  Batch: 400 of 550,  Cost: 2.4182,  AvgTime: 7.11ms
Step: 21326,  Epoch: 13,  Batch: 500 of 550,  Cost: 1.7647,  AvgTime: 6.92ms
Step: 21460,  Epoch: 13,  Batch: 550 of 550,  Cost: 2.5968,  AvgTime: 3.45ms
Step: 21775,  Epoch: 14,  Batch: 100 of 550,  Cost: 2.5712,  AvgTime: 7.55ms
Step: 22069,  Epoch: 14,  Batch: 200 of 550,  Cost: 2.2087,  AvgTime: 6.76ms
Step: 22371,  Epoch: 14,  Batch: 300 of 550,  Cost: 2.6150,  AvgTime: 6.97ms
Step: 22683,  Epoch: 14,  Batch: 400 of 550,  Cost: 1.8943,  AvgTime: 7.10ms
Step: 22969,  Epoch: 14,  Batch: 500 of 550,  Cost: 2.6193,  AvgTime: 6.81ms
Step: 23109,  Epoch: 14,  Batch: 550 of 550,  Cost: 2.7155,  AvgTime: 3.54ms
Step: 23426,  Epoch: 15,  Batch: 100 of 550,  Cost: 2.3266,  AvgTime: 7.67ms
Step: 23730,  Epoch: 15,  Batch: 200 of 550,  Cost: 1.9543,  AvgTime: 6.93ms
Step: 24027,  Epoch: 15,  Batch: 300 of 550,  Cost: 2.2945,  AvgTime: 6.88ms
Step: 24333,  Epoch: 15,  Batch: 400 of 550,  Cost: 2.3747,  AvgTime: 7.00ms
Step: 24626,  Epoch: 15,  Batch: 500 of 550,  Cost: 2.3737,  AvgTime: 7.07ms
Step: 24763,  Epoch: 15,  Batch: 550 of 550,  Cost: 1.9715,  AvgTime: 3.53ms
Step: 25072,  Epoch: 16,  Batch: 100 of 550,  Cost: 1.8765,  AvgTime: 7.51ms
Step: 25370,  Epoch: 16,  Batch: 200 of 550,  Cost: 2.1541,  AvgTime: 6.82ms
Step: 25668,  Epoch: 16,  Batch: 300 of 550,  Cost: 2.3879,  AvgTime: 6.91ms
Step: 25968,  Epoch: 16,  Batch: 400 of 550,  Cost: 2.1221,  AvgTime: 6.85ms
Step: 26261,  Epoch: 16,  Batch: 500 of 550,  Cost: 2.4611,  AvgTime: 7.10ms
Step: 26407,  Epoch: 16,  Batch: 550 of 550,  Cost: 2.1920,  AvgTime: 3.58ms
Step: 26725,  Epoch: 17,  Batch: 100 of 550,  Cost: 2.6185,  AvgTime: 7.84ms
Step: 27030,  Epoch: 17,  Batch: 200 of 550,  Cost: 1.9193,  AvgTime: 6.96ms
Step: 27327,  Epoch: 17,  Batch: 300 of 550,  Cost: 2.1718,  AvgTime: 6.85ms
Step: 27626,  Epoch: 17,  Batch: 400 of 550,  Cost: 2.5772,  AvgTime: 6.89ms
Step: 27911,  Epoch: 17,  Batch: 500 of 550,  Cost: 2.0193,  AvgTime: 6.89ms
Step: 28058,  Epoch: 17,  Batch: 550 of 550,  Cost: 2.2215,  AvgTime: 3.45ms
Step: 28366,  Epoch: 18,  Batch: 100 of 550,  Cost: 2.0564,  AvgTime: 7.63ms
Step: 28666,  Epoch: 18,  Batch: 200 of 550,  Cost: 2.1255,  AvgTime: 6.98ms
Step: 28963,  Epoch: 18,  Batch: 300 of 550,  Cost: 2.3852,  AvgTime: 6.83ms
Step: 29266,  Epoch: 18,  Batch: 400 of 550,  Cost: 2.0940,  AvgTime: 6.91ms
Step: 29564,  Epoch: 18,  Batch: 500 of 550,  Cost: 2.0937,  AvgTime: 7.17ms
Step: 29711,  Epoch: 18,  Batch: 550 of 550,  Cost: 1.8059,  AvgTime: 3.52ms
Step: 30036,  Epoch: 19,  Batch: 100 of 550,  Cost: 2.1789,  AvgTime: 7.96ms
Step: 30334,  Epoch: 19,  Batch: 200 of 550,  Cost: 2.1041,  AvgTime: 6.89ms
Step: 30641,  Epoch: 19,  Batch: 300 of 550,  Cost: 2.2974,  AvgTime: 7.03ms
Step: 30937,  Epoch: 19,  Batch: 400 of 550,  Cost: 2.4051,  AvgTime: 6.86ms
Step: 31228,  Epoch: 19,  Batch: 500 of 550,  Cost: 2.2501,  AvgTime: 7.06ms
Step: 31367,  Epoch: 19,  Batch: 550 of 550,  Cost: 1.8499,  AvgTime: 3.51ms
Step: 31694,  Epoch: 20,  Batch: 100 of 550,  Cost: 2.1828,  AvgTime: 7.90ms
Step: 31987,  Epoch: 20,  Batch: 200 of 550,  Cost: 2.0387,  AvgTime: 6.62ms
Step: 32284,  Epoch: 20,  Batch: 300 of 550,  Cost: 2.0869,  AvgTime: 6.76ms
Step: 32583,  Epoch: 20,  Batch: 400 of 550,  Cost: 2.0963,  AvgTime: 6.88ms
Step: 32856,  Epoch: 20,  Batch: 500 of 550,  Cost: 1.5775,  AvgTime: 7.03ms
Step: 32948,  Epoch: 20,  Batch: 550 of 550,  Cost: 1.8096,  AvgTime: 3.03ms
Test-Accuracy: 0.51
Total Time: 77.84s
Final Cost: 1.8096
done
```