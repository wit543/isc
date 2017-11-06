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


## fail attempt

worker 1

``` bash
root@98154222840c:~/isc# python3 alexnet.py  --job_name worker --task_index 0
2017-11-06 10:42:27.046752: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-06 10:42:27.147486: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-06 10:42:27.148203: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-06 10:42:27.148259: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1106 10:42:27.211565165     810 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-06 10:42:27.216556: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-06 10:42:27.216688: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-06 10:42:27.218341: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
conv1   [128, 56, 56, 64]
pool1   [128, 27, 27, 64]
conv2   [128, 27, 27, 192]
pool2   [128, 13, 13, 192]
conv3   [128, 13, 13, 384]
conv4   [128, 13, 13, 256]
conv5   [128, 13, 13, 256]
pool5   [128, 6, 6, 256]
2017-11-06 10:42:27.290413: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
2017-11-06 10:42:29.862750: step 0, duration = 0.124
2017-11-06 10:42:31.107390: step 10, duration = 0.126
2017-11-06 10:42:32.358143: step 20, duration = 0.124
2017-11-06 10:42:33.594976: step 30, duration = 0.124
2017-11-06 10:42:34.833029: step 40, duration = 0.124
2017-11-06 10:42:36.079618: step 50, duration = 0.124
2017-11-06 10:42:37.316667: step 60, duration = 0.124
2017-11-06 10:42:38.553960: step 70, duration = 0.123
2017-11-06 10:42:39.805954: step 80, duration = 0.124
2017-11-06 10:42:41.052326: step 90, duration = 0.124
2017-11-06 10:42:42.174312: Forward across 100 steps, 0.124 +/- 0.002 sec / batch
2017-11-06 10:42:46.787516: step 0, duration = 0.328
2017-11-06 10:42:50.080465: step 10, duration = 0.329
2017-11-06 10:42:53.367886: step 20, duration = 0.328
2017-11-06 10:42:56.656992: step 30, duration = 0.329
2017-11-06 10:42:59.962360: step 40, duration = 0.331
2017-11-06 10:43:03.250028: step 50, duration = 0.327
2017-11-06 10:43:06.550873: step 60, duration = 0.331
2017-11-06 10:43:09.850876: step 70, duration = 0.329
2017-11-06 10:43:13.160265: step 80, duration = 0.329
2017-11-06 10:43:16.448525: step 90, duration = 0.329
2017-11-06 10:43:19.403795: Forward-backward across 100 steps, 0.329 +/- 0.002 sec / batch
```

worker 2

``` bash
root@610546c83414:~/isc# python3 alexnet.py  --job_name worker --task_index 1
2017-11-06 10:38:38.223773: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-06 10:38:38.234296: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-06 10:38:38.234386: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 610546c83414
2017-11-06 10:38:38.234409: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 610546c83414
2017-11-06 10:38:38.234468: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-06 10:38:38.234560: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-06 10:38:38.234775: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-06 10:38:38.234799: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1106 10:38:38.235132724     147 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-06 10:38:38.242295: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-06 10:38:38.242378: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> localhost:2222, 2 -> 172.17.0.5:2222}
2017-11-06 10:38:38.243118: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
conv1   [128, 56, 56, 64]
pool1   [128, 27, 27, 64]
conv2   [128, 27, 27, 192]
pool2   [128, 13, 13, 192]
conv3   [128, 13, 13, 384]
conv4   [128, 13, 13, 256]
conv5   [128, 13, 13, 256]
pool5   [128, 6, 6, 256]
2017-11-06 10:39:45.286059: step 0, duration = 6.670
2017-11-06 10:40:34.765937: step 10, duration = 4.867
2017-11-06 10:41:23.546300: step 20, duration = 4.937
2017-11-06 10:42:12.266843: step 30, duration = 4.914
2017-11-06 10:43:12.944367: step 40, duration = 6.763
2017-11-06 10:44:03.629214: step 50, duration = 4.881
2017-11-06 10:44:52.494687: step 60, duration = 4.881
2017-11-06 10:45:41.545709: step 70, duration = 4.835
2017-11-06 10:46:30.215225: step 80, duration = 4.883
2017-11-06 10:47:19.106870: step 90, duration = 4.845
2017-11-06 10:48:01.780605: Forward across 100 steps, 5.032 +/- 0.495 sec / batch
2017-11-06 10:51:10.243874: step 0, duration = 17.139
2017-11-06 10:54:01.544378: step 10, duration = 17.248
2017-11-06 10:56:53.155274: step 20, duration = 17.055
2017-11-06 10:59:44.149839: step 30, duration = 17.250
2017-11-06 11:02:35.318911: step 40, duration = 17.105
2017-11-06 11:05:26.299299: step 50, duration = 17.066
2017-11-06 11:08:17.537378: step 60, duration = 17.107
2017-11-06 11:11:08.630783: step 70, duration = 17.264
2017-11-06 11:14:00.081247: step 80, duration = 17.211
2017-11-06 11:16:51.271194: step 90, duration = 17.173
2017-11-06 11:19:04.358045: Forward-backward across 100 steps, 16.912 +/- 1.248 sec / batch
```

worker 3

```bash
root@5dee89c483b9:~/isc# python3 alexnet.py  --job_name worker --task_index 2
2017-11-06 10:38:11.834879: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-06 10:38:11.837553: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-06 10:38:11.837607: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-06 10:38:11.837629: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-06 10:38:11.837713: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-06 10:38:11.837750: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-06 10:38:11.837785: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-06 10:38:11.837803: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1106 10:38:11.838121902     160 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-06 10:38:11.841916: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-06 10:38:11.841991: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> localhost:2222}
2017-11-06 10:38:11.842668: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
conv1   [128, 56, 56, 64]
pool1   [128, 27, 27, 64]
conv2   [128, 27, 27, 192]
pool2   [128, 13, 13, 192]
conv3   [128, 13, 13, 384]
conv4   [128, 13, 13, 256]
conv5   [128, 13, 13, 256]
pool5   [128, 6, 6, 256]
2017-11-06 10:38:49.368638: step 0, duration = 4.887
2017-11-06 10:39:51.681805: step 10, duration = 5.491
2017-11-06 10:40:40.260026: step 20, duration = 4.870
2017-11-06 10:41:28.784906: step 30, duration = 4.862
2017-11-06 10:42:17.431733: step 40, duration = 4.854
2017-11-06 10:43:19.903277: step 50, duration = 6.611
2017-11-06 10:44:08.622313: step 60, duration = 4.849
2017-11-06 10:44:57.422237: step 70, duration = 4.841
2017-11-06 10:45:46.151667: step 80, duration = 4.951
2017-11-06 10:46:34.998216: step 90, duration = 4.859
2017-11-06 10:47:18.803225: Forward across 100 steps, 5.143 +/- 0.604 sec / batch
2017-11-06 10:50:28.177920: step 0, duration = 17.043
2017-11-06 10:53:19.353503: step 10, duration = 17.116
2017-11-06 10:56:10.273737: step 20, duration = 16.949
2017-11-06 10:59:02.295929: step 30, duration = 17.211
2017-11-06 11:01:53.203285: step 40, duration = 17.084
2017-11-06 11:04:44.439765: step 50, duration = 17.105
2017-11-06 11:07:35.339967: step 60, duration = 16.996
2017-11-06 11:10:26.589104: step 70, duration = 17.259
2017-11-06 11:13:17.443790: step 80, duration = 17.128
2017-11-06 11:16:08.739137: step 90, duration = 17.250
2017-11-06 11:18:42.778283: Forward-backward across 100 steps, 17.116 +/- 0.106 sec / batch
```