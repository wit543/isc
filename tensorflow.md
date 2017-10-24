
```sh
# install git
apt update & apt install git vim curl

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