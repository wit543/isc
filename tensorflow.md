
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
