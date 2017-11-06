# Alex Net

## normal

```bash
root@a22e6717d336:~/models/tutorials/image/alexnet# python3 alexnet_benchmark.py
conv1   [128, 56, 56, 64]
pool1   [128, 27, 27, 64]
conv2   [128, 27, 27, 192]
pool2   [128, 13, 13, 192]
conv3   [128, 13, 13, 384]
conv4   [128, 13, 13, 256]
conv5   [128, 13, 13, 256]
pool5   [128, 6, 6, 256]
2017-11-05 08:52:05.258856: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-05 08:52:05.404808: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-05 08:52:05.405287: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties:
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-05 08:52:05.405372: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
2017-11-05 08:52:12.880742: step 0, duration = 0.123
2017-11-05 08:52:14.109850: step 10, duration = 0.123
2017-11-05 08:52:15.338491: step 20, duration = 0.123
2017-11-05 08:52:16.567150: step 30, duration = 0.123
2017-11-05 08:52:17.795845: step 40, duration = 0.123
2017-11-05 08:52:19.024539: step 50, duration = 0.123
2017-11-05 08:52:20.252829: step 60, duration = 0.123
2017-11-05 08:52:21.481728: step 70, duration = 0.123
2017-11-05 08:52:22.710379: step 80, duration = 0.123
2017-11-05 08:52:23.938908: step 90, duration = 0.123
2017-11-05 08:52:25.044883: Forward across 100 steps, 0.123 +/- 0.000 sec / batch
.2017-11-05 08:52:29.671687: step 0, duration = 0.329
2017-11-05 08:52:32.960443: step 10, duration = 0.329
2017-11-05 08:52:36.250040: step 20, duration = 0.329
2017-11-05 08:52:39.542388: step 30, duration = 0.329
2017-11-05 08:52:42.832023: step 40, duration = 0.329
2017-11-05 08:52:46.121084: step 50, duration = 0.329
2017-11-05 08:52:49.413365: step 60, duration = 0.332
2017-11-05 08:52:52.702879: step 70, duration = 0.329
2017-11-05 08:52:55.992488: step 80, duration = 0.329
2017-11-05 08:52:59.281984: step 90, duration = 0.329
2017-11-05 08:53:02.249144: Forward-backward across 100 steps, 0.329 +/- 0.001 sec / batch
```

## Distributed

distributed 1 worker
```bash
root@a22e6717d336:~/isc# python3 alexnet.py  --job_name worker --task_index 0
2017-11-06 03:54:00.292475: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-06 03:54:00.390069: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-06 03:54:00.390603: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-06 03:54:00.390666: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1106 03:54:00.446725740     150 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-06 03:54:00.450657: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.6:2222}
2017-11-06 03:54:00.450721: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.8:2222, 2 -> 172.17.0.9:2222}
2017-11-06 03:54:00.451284: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
conv1   [128, 56, 56, 64]
pool1   [128, 27, 27, 64]
conv2   [128, 27, 27, 192]
pool2   [128, 13, 13, 192]
conv3   [128, 13, 13, 384]
conv4   [128, 13, 13, 256]
conv5   [128, 13, 13, 256]
pool5   [128, 6, 6, 256]
2017-11-06 03:54:00.510380: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
2017-11-06 03:54:03.003803: step 0, duration = 0.124
2017-11-06 03:54:04.236782: step 10, duration = 0.123
2017-11-06 03:54:05.469337: step 20, duration = 0.123
2017-11-06 03:54:06.703473: step 30, duration = 0.123
2017-11-06 03:54:07.937722: step 40, duration = 0.124
2017-11-06 03:54:09.171046: step 50, duration = 0.123
2017-11-06 03:54:10.404547: step 60, duration = 0.123
2017-11-06 03:54:11.638039: step 70, duration = 0.123
2017-11-06 03:54:12.870970: step 80, duration = 0.123
2017-11-06 03:54:14.104983: step 90, duration = 0.123
2017-11-06 03:54:15.215377: Forward across 100 steps, 0.123 +/- 0.000 sec / batch
2017-11-06 03:54:19.776567: step 0, duration = 0.330
2017-11-06 03:54:23.066635: step 10, duration = 0.330
2017-11-06 03:54:26.365174: step 20, duration = 0.330
2017-11-06 03:54:29.659569: step 30, duration = 0.328
2017-11-06 03:54:32.952178: step 40, duration = 0.328
2017-11-06 03:54:36.248447: step 50, duration = 0.331
2017-11-06 03:54:39.538702: step 60, duration = 0.329
2017-11-06 03:54:42.832680: step 70, duration = 0.327
2017-11-06 03:54:46.129948: step 80, duration = 0.331
2017-11-06 03:54:49.422665: step 90, duration = 0.330
2017-11-06 03:54:52.387350: Forward-backward across 100 steps, 0.329 +/- 0.001 sec / batch
```