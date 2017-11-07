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

## Modified (add 10 layer)

### distributed
ps 1
```bash
root@a22e6717d336:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name ps --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 08:00:38.376894: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 08:00:38.380281: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 08:00:38.380339: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: a22e6717d336
2017-11-07 08:00:38.380361: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: a22e6717d336
2017-11-07 08:00:38.380411: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 08:00:38.380445: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 08:00:38.380480: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 08:00:38.380500: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 08:00:38.380680470     723 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 08:00:38.387311: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> localhost:2222}
2017-11-07 08:00:38.387406: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-07 08:00:38.388113: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
```
worker 2
```bash
root@98154222840c:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 08:01:13.267100: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 08:01:13.367423: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-07 08:01:13.368034: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-07 08:01:13.368086: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1107 08:01:13.424578050    5782 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-07 08:01:13.428718: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 08:01:13.428783: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-07 08:01:13.429245: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 08:01:21.796339: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session b9ab6ca287d4efda with config: 
2017-11-07 08:01:26.466640: step 0, duration = 0.268
2017-11-07 08:01:29.061035: step 10, duration = 0.260
2017-11-07 08:01:31.716837: step 20, duration = 0.270
2017-11-07 08:01:34.328573: step 30, duration = 0.256
2017-11-07 08:01:36.956684: step 40, duration = 0.268
2017-11-07 08:01:39.608582: step 50, duration = 0.281
2017-11-07 08:01:42.265741: step 60, duration = 0.265
2017-11-07 08:01:44.904771: step 70, duration = 0.261
2017-11-07 08:01:47.517005: step 80, duration = 0.262
2017-11-07 08:01:50.147625: step 90, duration = 0.266
2017-11-07 08:01:53.355868: step 100, duration = 0.329
2017-11-07 08:01:57.437052: step 110, duration = 0.403
2017-11-07 08:02:01.411663: step 120, duration = 0.340
2017-11-07 08:02:05.477249: step 130, duration = 0.337
2017-11-07 08:02:09.613592: step 140, duration = 0.435
2017-11-07 08:02:13.580859: step 150, duration = 0.483
2017-11-07 08:02:17.350593: step 160, duration = 0.380
2017-11-07 08:02:21.424617: step 170, duration = 0.391
2017-11-07 08:02:25.460048: step 180, duration = 0.375
2017-11-07 08:02:29.549703: step 190, duration = 0.378
2017-11-07 08:02:33.657501: step 200, duration = 0.368
2017-11-07 08:02:37.591534: step 210, duration = 0.373
2017-11-07 08:02:41.460636: step 220, duration = 0.422
2017-11-07 08:02:45.388579: step 230, duration = 0.341
2017-11-07 08:02:49.398539: step 240, duration = 0.409
2017-11-07 08:02:53.375933: step 250, duration = 0.439
2017-11-07 08:02:57.506597: step 260, duration = 0.405
2017-11-07 08:03:01.577474: step 270, duration = 0.399
2017-11-07 08:03:05.520587: step 280, duration = 0.356
2017-11-07 08:03:09.415685: step 290, duration = 0.380
2017-11-07 08:03:13.462281: step 300, duration = 0.372
2017-11-07 08:03:17.573550: step 310, duration = 0.402
2017-11-07 08:03:21.702446: step 320, duration = 0.398
2017-11-07 08:03:25.720829: step 330, duration = 0.488
2017-11-07 08:03:29.771293: step 340, duration = 0.471
2017-11-07 08:03:33.711245: step 350, duration = 0.417
2017-11-07 08:03:37.634874: step 360, duration = 0.364
2017-11-07 08:03:41.648673: step 370, duration = 0.396
2017-11-07 08:03:45.631524: step 380, duration = 0.372
2017-11-07 08:03:49.564926: step 390, duration = 0.380
2017-11-07 08:03:53.572620: step 400, duration = 0.416
2017-11-07 08:03:57.516518: step 410, duration = 0.453
2017-11-07 08:04:01.426167: step 420, duration = 0.428
2017-11-07 08:04:05.515114: step 430, duration = 0.422
2017-11-07 08:04:09.599428: step 440, duration = 0.394
2017-11-07 08:04:13.508962: step 450, duration = 0.407
2017-11-07 08:04:17.524479: step 460, duration = 0.430
2017-11-07 08:04:21.406160: step 470, duration = 0.383
2017-11-07 08:04:25.317664: step 480, duration = 0.423
2017-11-07 08:04:29.206394: step 490, duration = 0.369
2017-11-07 08:04:33.203333: step 500, duration = 0.414
2017-11-07 08:04:37.333129: step 510, duration = 0.461
2017-11-07 08:04:41.254888: step 520, duration = 0.475
2017-11-07 08:04:45.342721: step 530, duration = 0.444
2017-11-07 08:04:49.264637: step 540, duration = 0.332
2017-11-07 08:04:53.253582: step 550, duration = 0.360
2017-11-07 08:04:57.204069: step 560, duration = 0.351
2017-11-07 08:05:01.057030: step 570, duration = 0.485
2017-11-07 08:05:04.883472: step 580, duration = 0.387
2017-11-07 08:05:08.689769: step 590, duration = 0.342
2017-11-07 08:05:12.701530: step 600, duration = 0.370
2017-11-07 08:05:16.609550: step 610, duration = 0.361
2017-11-07 08:05:20.623641: step 620, duration = 0.469
2017-11-07 08:05:24.537474: step 630, duration = 0.476
2017-11-07 08:05:28.575123: step 640, duration = 0.484
2017-11-07 08:05:32.456874: step 650, duration = 0.351
2017-11-07 08:05:36.535521: step 660, duration = 0.344
2017-11-07 08:05:40.455006: step 670, duration = 0.382
2017-11-07 08:05:44.417921: step 680, duration = 0.354
2017-11-07 08:05:48.456286: step 690, duration = 0.353
2017-11-07 08:05:52.386967: step 700, duration = 0.463
2017-11-07 08:05:56.305462: step 710, duration = 0.473
2017-11-07 08:06:00.367321: step 720, duration = 0.429
2017-11-07 08:06:04.452045: step 730, duration = 0.433
2017-11-07 08:06:08.475082: step 740, duration = 0.403
2017-11-07 08:06:12.465778: step 750, duration = 0.384
2017-11-07 08:06:16.453837: step 760, duration = 0.366
2017-11-07 08:06:20.464461: step 770, duration = 0.344
2017-11-07 08:06:24.401473: step 780, duration = 0.411
2017-11-07 08:06:28.482559: step 790, duration = 0.429
2017-11-07 08:06:32.482521: step 800, duration = 0.505
2017-11-07 08:06:36.469930: step 810, duration = 0.473
2017-11-07 08:06:40.322729: step 820, duration = 0.387
2017-11-07 08:06:44.331577: step 830, duration = 0.369
2017-11-07 08:06:48.344251: step 840, duration = 0.376
2017-11-07 08:06:52.633856: step 850, duration = 0.353
2017-11-07 08:06:56.522374: step 860, duration = 0.416
2017-11-07 08:07:00.388668: step 870, duration = 0.404
2017-11-07 08:07:04.388214: step 880, duration = 0.400
2017-11-07 08:07:08.400756: step 890, duration = 0.436
2017-11-07 08:07:12.359187: step 900, duration = 0.431
2017-11-07 08:07:16.507648: step 910, duration = 0.435
2017-11-07 08:07:20.447912: step 920, duration = 0.330
2017-11-07 08:07:24.431861: step 930, duration = 0.405
2017-11-07 08:07:28.625374: step 940, duration = 0.376
2017-11-07 08:07:32.920434: step 950, duration = 0.389
2017-11-07 08:07:36.964523: step 960, duration = 0.393
2017-11-07 08:07:41.041346: step 970, duration = 0.440
2017-11-07 08:07:44.991569: step 980, duration = 0.389
2017-11-07 08:07:48.924164: step 990, duration = 0.454
2017-11-07 08:07:52.529902: across 1000 steps, 0.390 +/- 0.054 sec / batch
```
worker 3
```bash
root@610546c83414:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 1 --batch_size 10 --num_batches 1000
2017-11-07 08:01:17.177566: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 08:01:17.180514: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 08:01:17.180569: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 610546c83414
2017-11-07 08:01:17.180591: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 610546c83414
2017-11-07 08:01:17.180646: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 08:01:17.180682: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 08:01:17.180718: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 08:01:17.180745: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 08:01:17.180899932    2383 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 08:01:17.184756: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 08:01:17.184816: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> localhost:2222, 2 -> 172.17.0.5:2222}
2017-11-07 08:01:17.185365: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 08:01:21.542553: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session b7c7f585971a0468 with config: 
2017-11-07 08:01:51.641509: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 1ba4095ab88393a4 with config: 
2017-11-07 08:02:15.203976: step 0, duration = 2.200
2017-11-07 08:02:36.854956: step 10, duration = 2.217
2017-11-07 08:02:57.873400: step 20, duration = 2.074
2017-11-07 08:03:18.650311: step 30, duration = 1.979
2017-11-07 08:03:40.083528: step 40, duration = 2.078
2017-11-07 08:04:01.542252: step 50, duration = 2.136
2017-11-07 08:04:22.688063: step 60, duration = 2.043
2017-11-07 08:04:43.103431: step 70, duration = 2.105
2017-11-07 08:05:04.838328: step 80, duration = 2.181
2017-11-07 08:05:26.176280: step 90, duration = 2.094
2017-11-07 08:05:47.315519: step 100, duration = 2.153
2017-11-07 08:06:08.896217: step 110, duration = 2.116
2017-11-07 08:06:29.868458: step 120, duration = 2.067
2017-11-07 08:06:51.486159: step 130, duration = 2.041
2017-11-07 08:07:12.745956: step 140, duration = 2.121
2017-11-07 08:07:33.990237: step 150, duration = 2.269
2017-11-07 08:07:54.402699: step 160, duration = 1.483
2017-11-07 08:08:08.475535: step 170, duration = 1.421
2017-11-07 08:08:22.806430: step 180, duration = 1.419
2017-11-07 08:08:36.963441: step 190, duration = 1.371
2017-11-07 08:08:50.864387: step 200, duration = 1.334
2017-11-07 08:09:06.072211: step 210, duration = 1.348
2017-11-07 08:09:20.118159: step 220, duration = 1.386
2017-11-07 08:09:33.960193: step 230, duration = 1.403
2017-11-07 08:09:48.179882: step 240, duration = 1.466
2017-11-07 08:10:02.537209: step 250, duration = 1.462
2017-11-07 08:10:16.894470: step 260, duration = 1.424
2017-11-07 08:10:31.172525: step 270, duration = 1.525
2017-11-07 08:10:46.243797: step 280, duration = 1.870
2017-11-07 08:11:00.390573: step 290, duration = 1.424
2017-11-07 08:11:14.573537: step 300, duration = 1.493
2017-11-07 08:11:29.011215: step 310, duration = 1.573
2017-11-07 08:11:45.486306: step 320, duration = 1.554
2017-11-07 08:12:00.825307: step 330, duration = 1.760
2017-11-07 08:12:17.002339: step 340, duration = 1.765
2017-11-07 08:12:33.835494: step 350, duration = 1.928
2017-11-07 08:12:50.884330: step 360, duration = 1.766
2017-11-07 08:13:08.925314: step 370, duration = 1.710
2017-11-07 08:13:25.965658: step 380, duration = 1.683
2017-11-07 08:13:43.418228: step 390, duration = 1.721
2017-11-07 08:14:01.472781: step 400, duration = 1.847
2017-11-07 08:14:18.099201: step 410, duration = 1.425
2017-11-07 08:14:32.053482: step 420, duration = 1.407
2017-11-07 08:14:46.078702: step 430, duration = 1.397
2017-11-07 08:15:00.702427: step 440, duration = 1.363
2017-11-07 08:15:14.884845: step 450, duration = 1.390
2017-11-07 08:15:29.058687: step 460, duration = 1.502
2017-11-07 08:15:43.329477: step 470, duration = 1.461
2017-11-07 08:15:57.337395: step 480, duration = 1.386
2017-11-07 08:16:11.746286: step 490, duration = 1.483
2017-11-07 08:16:26.004010: step 500, duration = 1.474
2017-11-07 08:16:40.376276: step 510, duration = 1.478
2017-11-07 08:16:54.664543: step 520, duration = 1.404
2017-11-07 08:17:08.942820: step 530, duration = 1.504
2017-11-07 08:17:22.926122: step 540, duration = 1.390
2017-11-07 08:17:36.776220: step 550, duration = 1.355
2017-11-07 08:17:50.728203: step 560, duration = 1.387
2017-11-07 08:18:04.698417: step 570, duration = 1.439
2017-11-07 08:18:18.716388: step 580, duration = 1.445
2017-11-07 08:18:32.577620: step 590, duration = 1.402
2017-11-07 08:18:46.599908: step 600, duration = 1.464
2017-11-07 08:19:00.557216: step 610, duration = 1.411
2017-11-07 08:19:14.493403: step 620, duration = 1.430
2017-11-07 08:19:28.458598: step 630, duration = 1.376
2017-11-07 08:19:42.435479: step 640, duration = 1.439
2017-11-07 08:19:56.345857: step 650, duration = 1.366
2017-11-07 08:20:10.195178: step 660, duration = 1.454
2017-11-07 08:20:24.305406: step 670, duration = 1.458
2017-11-07 08:20:38.067814: step 680, duration = 1.427
2017-11-07 08:20:52.087256: step 690, duration = 1.328
2017-11-07 08:21:05.970503: step 700, duration = 1.470
2017-11-07 08:21:20.390967: step 710, duration = 1.483
2017-11-07 08:21:34.571235: step 720, duration = 1.375
2017-11-07 08:21:48.596532: step 730, duration = 1.458
2017-11-07 08:22:02.424066: step 740, duration = 1.361
2017-11-07 08:22:16.438439: step 750, duration = 1.427
2017-11-07 08:22:30.494765: step 760, duration = 1.382
2017-11-07 08:22:44.915366: step 770, duration = 1.449
2017-11-07 08:22:58.801642: step 780, duration = 1.394
2017-11-07 08:23:13.080014: step 790, duration = 1.392
2017-11-07 08:23:27.460148: step 800, duration = 1.398
2017-11-07 08:23:41.599142: step 810, duration = 1.379
2017-11-07 08:23:55.673033: step 820, duration = 1.412
2017-11-07 08:24:09.741195: step 830, duration = 1.382
2017-11-07 08:24:23.474462: step 840, duration = 1.456
2017-11-07 08:24:37.506297: step 850, duration = 1.438
2017-11-07 08:24:51.510365: step 860, duration = 1.444
2017-11-07 08:25:05.431724: step 870, duration = 1.401
2017-11-07 08:25:19.324209: step 880, duration = 1.403
2017-11-07 08:25:33.221008: step 890, duration = 1.347
2017-11-07 08:25:47.172427: step 900, duration = 1.366
2017-11-07 08:26:01.281409: step 910, duration = 1.391
2017-11-07 08:26:15.306561: step 920, duration = 1.321
2017-11-07 08:26:29.288442: step 930, duration = 1.384
2017-11-07 08:26:42.995792: step 940, duration = 1.353
2017-11-07 08:26:56.972439: step 950, duration = 1.398
2017-11-07 08:27:10.939389: step 960, duration = 1.380
2017-11-07 08:27:25.121295: step 970, duration = 1.405
2017-11-07 08:27:39.219198: step 980, duration = 1.440
2017-11-07 08:27:53.356846: step 990, duration = 1.434
2017-11-07 08:28:05.887216: across 1000 steps, 1.574 +/- 0.232 sec / batch
```
worker 4
```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 2 --batch_size 10 --num_batches 1000
2017-11-07 08:01:20.988895: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 08:01:20.992626: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 08:01:20.992727: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-07 08:01:20.992749: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-07 08:01:20.992802: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 08:01:20.992836: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 08:01:20.992873: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 08:01:20.992892: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 08:01:20.993115167    5727 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 08:01:20.999439: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 08:01:20.999531: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> localhost:2222}
2017-11-07 08:01:21.000178: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 08:01:21.363430: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session bf76272a5590bf2c with config: 
2017-11-07 08:01:51.449759: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 777460b3b8cfb87d with config: 
2017-11-07 08:02:15.302165: step 0, duration = 2.239
2017-11-07 08:02:36.302157: step 10, duration = 1.977
2017-11-07 08:02:57.286623: step 20, duration = 2.158
2017-11-07 08:03:18.584222: step 30, duration = 2.118
2017-11-07 08:03:39.856234: step 40, duration = 2.138
2017-11-07 08:04:00.886313: step 50, duration = 2.116
2017-11-07 08:04:21.461655: step 60, duration = 2.144
2017-11-07 08:04:43.103455: step 70, duration = 2.186
2017-11-07 08:05:04.837765: step 80, duration = 2.172
2017-11-07 08:05:26.226845: step 90, duration = 2.022
2017-11-07 08:05:47.520060: step 100, duration = 1.957
2017-11-07 08:06:08.405652: step 110, duration = 1.987
2017-11-07 08:06:29.670588: step 120, duration = 2.125
2017-11-07 08:06:50.866790: step 130, duration = 2.114
2017-11-07 08:07:12.157797: step 140, duration = 2.139
2017-11-07 08:07:33.735192: step 150, duration = 1.977
2017-11-07 08:07:54.169550: step 160, duration = 1.463
2017-11-07 08:08:08.246424: step 170, duration = 1.412
2017-11-07 08:08:22.369451: step 180, duration = 1.335
2017-11-07 08:08:36.019772: step 190, duration = 1.437
2017-11-07 08:08:50.065294: step 200, duration = 1.438
2017-11-07 08:09:05.403118: step 210, duration = 1.460
2017-11-07 08:09:19.272563: step 220, duration = 1.382
2017-11-07 08:09:33.341509: step 230, duration = 1.421
2017-11-07 08:09:47.047544: step 240, duration = 1.390
2017-11-07 08:10:01.118814: step 250, duration = 1.458
2017-11-07 08:10:15.281226: step 260, duration = 1.404
2017-11-07 08:10:29.588596: step 270, duration = 1.382
2017-11-07 08:10:44.107829: step 280, duration = 1.793
2017-11-07 08:10:58.653234: step 290, duration = 1.408
2017-11-07 08:11:12.556453: step 300, duration = 1.378
2017-11-07 08:11:26.299533: step 310, duration = 1.363
2017-11-07 08:11:43.088783: step 320, duration = 1.734
2017-11-07 08:11:59.093914: step 330, duration = 1.691
2017-11-07 08:12:15.093560: step 340, duration = 1.825
2017-11-07 08:12:32.285656: step 350, duration = 1.572
2017-11-07 08:12:49.642524: step 360, duration = 1.828
2017-11-07 08:13:07.778274: step 370, duration = 1.794
2017-11-07 08:13:25.630188: step 380, duration = 1.700
2017-11-07 08:13:42.799703: step 390, duration = 1.856
2017-11-07 08:14:01.027510: step 400, duration = 1.851
2017-11-07 08:14:17.480578: step 410, duration = 1.327
2017-11-07 08:14:31.618232: step 420, duration = 1.464
2017-11-07 08:14:45.641630: step 430, duration = 1.435
2017-11-07 08:15:00.469207: step 440, duration = 1.444
2017-11-07 08:15:14.506502: step 450, duration = 1.423
2017-11-07 08:15:28.831061: step 460, duration = 1.448
2017-11-07 08:15:43.338866: step 470, duration = 1.436
2017-11-07 08:15:57.618097: step 480, duration = 1.489
2017-11-07 08:16:11.754189: step 490, duration = 1.405
2017-11-07 08:16:26.023268: step 500, duration = 1.382
2017-11-07 08:16:40.398304: step 510, duration = 1.457
2017-11-07 08:16:54.722546: step 520, duration = 1.456
2017-11-07 08:17:08.960114: step 530, duration = 1.339
2017-11-07 08:17:23.468199: step 540, duration = 1.432
2017-11-07 08:17:37.481665: step 550, duration = 1.437
2017-11-07 08:17:51.498198: step 560, duration = 1.477
2017-11-07 08:18:05.472217: step 570, duration = 1.339
2017-11-07 08:18:19.523792: step 580, duration = 1.409
2017-11-07 08:18:33.630701: step 590, duration = 1.420
2017-11-07 08:18:48.093227: step 600, duration = 1.474
2017-11-07 08:19:02.288449: step 610, duration = 1.385
2017-11-07 08:19:16.329563: step 620, duration = 1.402
2017-11-07 08:19:30.417272: step 630, duration = 1.431
2017-11-07 08:19:44.330352: step 640, duration = 1.359
2017-11-07 08:19:58.310922: step 650, duration = 1.424
2017-11-07 08:20:12.383331: step 660, duration = 1.383
2017-11-07 08:20:26.268790: step 670, duration = 1.396
2017-11-07 08:20:40.417038: step 680, duration = 1.377
2017-11-07 08:20:54.470967: step 690, duration = 1.494
2017-11-07 08:21:08.753280: step 700, duration = 1.442
2017-11-07 08:21:22.827348: step 710, duration = 1.386
2017-11-07 08:21:36.544382: step 720, duration = 1.352
2017-11-07 08:21:50.414461: step 730, duration = 1.391
2017-11-07 08:22:04.449464: step 740, duration = 1.356
2017-11-07 08:22:18.382286: step 750, duration = 1.410
2017-11-07 08:22:32.198310: step 760, duration = 1.352
2017-11-07 08:22:46.382333: step 770, duration = 1.443
2017-11-07 08:23:00.648199: step 780, duration = 1.418
2017-11-07 08:23:14.616338: step 790, duration = 1.354
2017-11-07 08:23:28.610018: step 800, duration = 1.348
2017-11-07 08:23:42.646331: step 810, duration = 1.418
2017-11-07 08:23:56.504398: step 820, duration = 1.378
2017-11-07 08:24:10.230201: step 830, duration = 1.376
2017-11-07 08:24:24.427207: step 840, duration = 1.326
2017-11-07 08:24:38.263989: step 850, duration = 1.332
2017-11-07 08:24:52.111643: step 860, duration = 1.308
2017-11-07 08:25:06.106206: step 870, duration = 1.413
2017-11-07 08:25:20.109674: step 880, duration = 1.400
2017-11-07 08:25:34.029207: step 890, duration = 1.396
2017-11-07 08:25:47.949332: step 900, duration = 1.396
2017-11-07 08:26:01.742593: step 910, duration = 1.447
2017-11-07 08:26:15.773394: step 920, duration = 1.480
2017-11-07 08:26:29.664202: step 930, duration = 1.418
2017-11-07 08:26:43.848384: step 940, duration = 1.355
2017-11-07 08:26:58.116819: step 950, duration = 1.386
2017-11-07 08:27:12.354803: step 960, duration = 1.513
2017-11-07 08:27:26.621456: step 970, duration = 1.419
2017-11-07 08:27:40.818307: step 980, duration = 1.393
2017-11-07 08:27:54.957066: step 990, duration = 1.457
2017-11-07 08:28:06.933635: across 1000 steps, 1.575 +/- 0.235 sec / batch
```