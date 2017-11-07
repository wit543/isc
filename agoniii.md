

## run
```bash
python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
```

## Result
worker 1
```bash
root@a22e6717d336:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name ps --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 04:04:22.283882: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 04:04:22.289574: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 04:04:22.289675: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: a22e6717d336
2017-11-07 04:04:22.289717: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: a22e6717d336
2017-11-07 04:04:22.289792: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 04:04:22.289826: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
"""
2017-11-07 04:04:22.289866: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 04:04:22.289886: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 04:04:22.290046827     615 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 04:04:22.294265: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> localhost:2222}
2017-11-07 04:04:22.294327: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-07 04:04:22.295133: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
```
worker 2
```bash
root@98154222840c:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 04:07:42.100149: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 04:07:42.200732: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-07 04:07:42.201216: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-07 04:07:42.201262: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1107 04:07:42.259149940    1043 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-07 04:07:42.263184: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 04:07:42.263310: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-07 04:07:42.263706: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 04:07:47.465870: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session f392cec2bf182302 with config: 
2017-11-07 04:07:52.127522: step 0, duration = 0.224
2017-11-07 04:07:54.409408: step 10, duration = 0.235
2017-11-07 04:07:56.748736: step 20, duration = 0.250
2017-11-07 04:07:59.064053: step 30, duration = 0.230
2017-11-07 04:08:01.426743: step 40, duration = 0.240
2017-11-07 04:08:03.765635: step 50, duration = 0.228
2017-11-07 04:08:06.067220: step 60, duration = 0.234
2017-11-07 04:08:08.376084: step 70, duration = 0.225
2017-11-07 04:08:10.667997: step 80, duration = 0.226
2017-11-07 04:08:12.989066: step 90, duration = 0.223
2017-11-07 04:08:15.319912: step 100, duration = 0.240
2017-11-07 04:08:17.601850: step 110, duration = 0.225
2017-11-07 04:08:20.984854: step 120, duration = 0.354
2017-11-07 04:08:25.004294: step 130, duration = 0.388
2017-11-07 04:08:28.625820: step 140, duration = 0.321
2017-11-07 04:08:32.369990: step 150, duration = 0.370
2017-11-07 04:08:36.150448: step 160, duration = 0.386
2017-11-07 04:08:39.889587: step 170, duration = 0.345
2017-11-07 04:08:43.703735: step 180, duration = 0.411
2017-11-07 04:08:47.569074: step 190, duration = 0.375
2017-11-07 04:08:51.341627: step 200, duration = 0.398
2017-11-07 04:08:55.175825: step 210, duration = 0.351
2017-11-07 04:08:58.958531: step 220, duration = 0.396
2017-11-07 04:09:02.798729: step 230, duration = 0.364
2017-11-07 04:09:06.493835: step 240, duration = 0.334
2017-11-07 04:09:10.338620: step 250, duration = 0.382
2017-11-07 04:09:14.132868: step 260, duration = 0.356
2017-11-07 04:09:17.987356: step 270, duration = 0.412
2017-11-07 04:09:21.866413: step 280, duration = 0.416
2017-11-07 04:09:25.625774: step 290, duration = 0.396
2017-11-07 04:09:29.449082: step 300, duration = 0.359
2017-11-07 04:09:33.377607: step 310, duration = 0.396
2017-11-07 04:09:37.296977: step 320, duration = 0.416
2017-11-07 04:09:41.092367: step 330, duration = 0.455
2017-11-07 04:09:44.771121: step 340, duration = 0.317
2017-11-07 04:09:48.638317: step 350, duration = 0.414
2017-11-07 04:09:52.416588: step 360, duration = 0.427
2017-11-07 04:09:56.138539: step 370, duration = 0.435
2017-11-07 04:10:00.015432: step 380, duration = 0.424
2017-11-07 04:10:03.919414: step 390, duration = 0.390
2017-11-07 04:10:07.481140: step 400, duration = 0.322
2017-11-07 04:10:11.367878: step 410, duration = 0.416
2017-11-07 04:10:15.274732: step 420, duration = 0.344
2017-11-07 04:10:19.028557: step 430, duration = 0.324
2017-11-07 04:10:23.079439: step 440, duration = 0.464
2017-11-07 04:10:26.860924: step 450, duration = 0.388
2017-11-07 04:10:30.766645: step 460, duration = 0.369
2017-11-07 04:10:34.612688: step 470, duration = 0.409
2017-11-07 04:10:38.308485: step 480, duration = 0.410
2017-11-07 04:10:42.089170: step 490, duration = 0.418
2017-11-07 04:10:45.747540: step 500, duration = 0.363
2017-11-07 04:10:49.590439: step 510, duration = 0.338
2017-11-07 04:10:53.293681: step 520, duration = 0.352
2017-11-07 04:10:57.114182: step 530, duration = 0.360
2017-11-07 04:11:00.951802: step 540, duration = 0.372
2017-11-07 04:11:04.877085: step 550, duration = 0.413
2017-11-07 04:11:08.606345: step 560, duration = 0.367
2017-11-07 04:11:12.399592: step 570, duration = 0.383
2017-11-07 04:11:16.144636: step 580, duration = 0.347
2017-11-07 04:11:19.953541: step 590, duration = 0.364
2017-11-07 04:11:23.672574: step 600, duration = 0.369
2017-11-07 04:11:27.520677: step 610, duration = 0.346
2017-11-07 04:11:31.246989: step 620, duration = 0.373
2017-11-07 04:11:34.952294: step 630, duration = 0.374
2017-11-07 04:11:38.755479: step 640, duration = 0.443
2017-11-07 04:11:42.612494: step 650, duration = 0.410
2017-11-07 04:11:46.430717: step 660, duration = 0.339
2017-11-07 04:11:50.214479: step 670, duration = 0.432
2017-11-07 04:11:54.068509: step 680, duration = 0.318
2017-11-07 04:11:57.958503: step 690, duration = 0.383
2017-11-07 04:12:01.764915: step 700, duration = 0.355
2017-11-07 04:12:05.710486: step 710, duration = 0.392
2017-11-07 04:12:09.658750: step 720, duration = 0.418
2017-11-07 04:12:13.544640: step 730, duration = 0.449
2017-11-07 04:12:17.353321: step 740, duration = 0.323
2017-11-07 04:12:21.070290: step 750, duration = 0.379
2017-11-07 04:12:24.831523: step 760, duration = 0.432
2017-11-07 04:12:28.654754: step 770, duration = 0.388
2017-11-07 04:12:32.479685: step 780, duration = 0.400
2017-11-07 04:12:36.196192: step 790, duration = 0.352
2017-11-07 04:12:40.038621: step 800, duration = 0.396
2017-11-07 04:12:43.741641: step 810, duration = 0.366
2017-11-07 04:12:47.478210: step 820, duration = 0.451
2017-11-07 04:12:51.240888: step 830, duration = 0.357
2017-11-07 04:12:55.007916: step 840, duration = 0.361
2017-11-07 04:12:58.872937: step 850, duration = 0.405
2017-11-07 04:13:02.601309: step 860, duration = 0.341
2017-11-07 04:13:06.487385: step 870, duration = 0.449
2017-11-07 04:13:10.241470: step 880, duration = 0.322
2017-11-07 04:13:14.016986: step 890, duration = 0.385
2017-11-07 04:13:17.896705: step 900, duration = 0.383
2017-11-07 04:13:21.550148: step 910, duration = 0.368
2017-11-07 04:13:25.461869: step 920, duration = 0.352
2017-11-07 04:13:29.342573: step 930, duration = 0.439
2017-11-07 04:13:33.484055: step 940, duration = 0.390
2017-11-07 04:13:37.331942: step 950, duration = 0.414
2017-11-07 04:13:41.157494: step 960, duration = 0.368
2017-11-07 04:13:45.012643: step 970, duration = 0.367
2017-11-07 04:13:48.790129: step 980, duration = 0.376
2017-11-07 04:13:52.493782: step 990, duration = 0.399
2017-11-07 04:13:55.962819: across 1000 steps, 0.368 +/- 0.060 sec / batch
```
worker 3
```bash
root@610546c83414:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 2 --batch_size 10 --num_batches 1000
2017-11-07 04:07:44.579479: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 04:07:44.582440: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 04:07:44.582501: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 610546c83414
2017-11-07 04:07:44.582537: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 610546c83414
2017-11-07 04:07:44.582600: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 04:07:44.582641: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
"""
2017-11-07 04:07:44.582678: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 04:07:44.582697: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 04:07:44.582853145     213 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 04:07:44.586670: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 04:07:44.586734: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> localhost:2222, 2 -> 172.17.0.5:2222}
2017-11-07 04:07:44.587451: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 04:07:47.773868: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 86265ce89540b7b6 with config:
2017-11-07 04:08:18.042457: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session af57b12ddeb32f24 with config:
2017-11-07 04:08:28.332300: step 0, duration = 0.898
2017-11-07 04:08:37.657402: step 10, duration = 0.951
2017-11-07 04:08:46.536331: step 20, duration = 0.910
2017-11-07 04:08:55.332068: step 30, duration = 0.870
2017-11-07 04:09:04.007145: step 40, duration = 0.828
2017-11-07 04:09:13.083301: step 50, duration = 0.890
2017-11-07 04:09:22.189385: step 60, duration = 0.946
2017-11-07 04:09:30.951890: step 70, duration = 0.885
2017-11-07 04:09:39.588266: step 80, duration = 0.856
2017-11-07 04:09:48.706204: step 90, duration = 0.895
2017-11-07 04:09:57.767799: step 100, duration = 0.880
2017-11-07 04:10:06.529283: step 110, duration = 0.928
2017-11-07 04:10:15.615323: step 120, duration = 0.933
2017-11-07 04:10:24.583716: step 130, duration = 0.918
2017-11-07 04:10:33.413319: step 140, duration = 0.892
2017-11-07 04:10:42.573027: step 150, duration = 0.913
2017-11-07 04:10:51.643484: step 160, duration = 1.043
2017-11-07 04:11:00.687513: step 170, duration = 0.892
2017-11-07 04:11:09.920941: step 180, duration = 0.877
2017-11-07 04:11:18.932451: step 190, duration = 0.926
2017-11-07 04:11:28.275307: step 200, duration = 1.070
2017-11-07 04:11:37.384701: step 210, duration = 0.907
2017-11-07 04:11:46.203330: step 220, duration = 0.914
2017-11-07 04:11:55.139370: step 230, duration = 0.860
2017-11-07 04:12:03.931422: step 240, duration = 0.809
2017-11-07 04:12:12.965502: step 250, duration = 0.892
2017-11-07 04:12:21.878421: step 260, duration = 0.912
2017-11-07 04:12:30.837275: step 270, duration = 0.911
2017-11-07 04:12:39.514312: step 280, duration = 0.829
2017-11-07 04:12:48.496454: step 290, duration = 0.944
2017-11-07 04:12:57.400930: step 300, duration = 0.861
2017-11-07 04:13:07.277960: step 310, duration = 0.851
2017-11-07 04:13:16.190382: step 320, duration = 0.912
2017-11-07 04:13:25.090407: step 330, duration = 0.995
2017-11-07 04:13:35.807852: step 340, duration = 0.899
2017-11-07 04:13:44.685702: step 350, duration = 0.913
2017-11-07 04:13:53.875000: step 360, duration = 1.021
2017-11-07 04:14:00.622646: step 370, duration = 0.611
2017-11-07 04:14:06.706954: step 380, duration = 0.608
2017-11-07 04:14:12.652273: step 390, duration = 0.592
2017-11-07 04:14:18.766703: step 400, duration = 0.631
2017-11-07 04:14:25.593451: step 410, duration = 0.723
2017-11-07 04:14:31.652537: step 420, duration = 0.577
2017-11-07 04:14:37.663894: step 430, duration = 0.615
2017-11-07 04:14:43.691750: step 440, duration = 0.574
2017-11-07 04:14:49.929493: step 450, duration = 0.547
2017-11-07 04:14:55.942405: step 460, duration = 0.505
2017-11-07 04:15:02.108311: step 470, duration = 0.576
2017-11-07 04:15:08.143198: step 480, duration = 0.594
2017-11-07 04:15:14.290015: step 490, duration = 0.591
2017-11-07 04:15:20.300943: step 500, duration = 0.591
2017-11-07 04:15:26.563439: step 510, duration = 0.660
2017-11-07 04:15:32.565130: step 520, duration = 0.648
2017-11-07 04:15:38.760036: step 530, duration = 0.610
2017-11-07 04:15:44.651235: step 540, duration = 0.561
2017-11-07 04:15:50.943676: step 550, duration = 0.630
2017-11-07 04:15:56.877401: step 560, duration = 0.589
2017-11-07 04:16:02.887674: step 570, duration = 0.636
2017-11-07 04:16:08.713385: step 580, duration = 0.592
2017-11-07 04:16:14.838170: step 590, duration = 0.598
2017-11-07 04:16:20.702568: step 600, duration = 0.550
2017-11-07 04:16:26.659432: step 610, duration = 0.642
2017-11-07 04:16:32.779084: step 620, duration = 0.596
2017-11-07 04:16:38.760416: step 630, duration = 0.563
2017-11-07 04:16:44.786447: step 640, duration = 0.611
2017-11-07 04:16:50.766085: step 650, duration = 0.649
2017-11-07 04:16:56.750941: step 660, duration = 0.632
2017-11-07 04:17:02.589914: step 670, duration = 0.576
2017-11-07 04:17:08.697758: step 680, duration = 0.660
2017-11-07 04:17:14.792697: step 690, duration = 0.580
2017-11-07 04:17:20.783504: step 700, duration = 0.576
2017-11-07 04:17:26.834200: step 710, duration = 0.559
2017-11-07 04:17:32.850365: step 720, duration = 0.597
2017-11-07 04:17:39.078357: step 730, duration = 0.601
2017-11-07 04:17:44.951963: step 740, duration = 0.572
2017-11-07 04:17:51.111675: step 750, duration = 0.614
2017-11-07 04:17:57.225556: step 760, duration = 0.560
2017-11-07 04:18:03.283287: step 770, duration = 0.614
2017-11-07 04:18:09.284402: step 780, duration = 0.572
2017-11-07 04:18:15.489919: step 790, duration = 0.611
2017-11-07 04:18:21.544461: step 800, duration = 0.565
2017-11-07 04:18:27.522564: step 810, duration = 0.542
2017-11-07 04:18:33.358538: step 820, duration = 0.560
2017-11-07 04:18:39.197982: step 830, duration = 0.620
2017-11-07 04:18:45.202238: step 840, duration = 0.599
2017-11-07 04:18:51.328629: step 850, duration = 0.628
2017-11-07 04:18:57.330473: step 860, duration = 0.544
2017-11-07 04:19:03.221539: step 870, duration = 0.543
2017-11-07 04:19:09.256634: step 880, duration = 0.642
2017-11-07 04:19:15.245133: step 890, duration = 0.596
2017-11-07 04:19:21.262314: step 900, duration = 0.604
2017-11-07 04:19:27.453523: step 910, duration = 0.642
2017-11-07 04:19:33.320442: step 920, duration = 0.578
2017-11-07 04:19:39.457519: step 930, duration = 0.604
2017-11-07 04:19:45.535880: step 940, duration = 0.559
2017-11-07 04:19:51.675944: step 950, duration = 0.602
2017-11-07 04:19:57.875246: step 960, duration = 0.567
2017-11-07 04:20:03.914381: step 970, duration = 0.600
2017-11-07 04:20:09.933632: step 980, duration = 0.567
2017-11-07 04:20:15.880286: step 990, duration = 0.646
2017-11-07 04:20:19.500514: across 1000 steps, 0.721 +/- 0.139 sec / batch
```

worker 4
```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 2 --batch_size 10 --num_batches 1000
2017-11-07 04:07:47.240153: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 04:07:47.243772: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 04:07:47.243855: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-07 04:07:47.243897: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-07 04:07:47.243957: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 04:07:47.243992: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 04:07:47.244033: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 04:07:47.244050: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 04:07:47.244276441     226 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 04:07:47.249597: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 04:07:47.249681: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> localhost:2222}
2017-11-07 04:07:47.250261: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 04:07:47.465854: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 9310b9664402626a with config: 
2017-11-07 04:08:18.019039: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 9afc8eb65a8c4515 with config: 
2017-11-07 04:08:27.663005: step 0, duration = 0.961
2017-11-07 04:08:36.407922: step 10, duration = 0.984
2017-11-07 04:08:45.436208: step 20, duration = 0.843
2017-11-07 04:08:54.663979: step 30, duration = 0.945
2017-11-07 04:09:03.725756: step 40, duration = 0.905
2017-11-07 04:09:12.835376: step 50, duration = 0.905
2017-11-07 04:09:21.483071: step 60, duration = 0.900
2017-11-07 04:09:30.534492: step 70, duration = 0.964
2017-11-07 04:09:39.530173: step 80, duration = 0.930
2017-11-07 04:09:48.405794: step 90, duration = 0.899
2017-11-07 04:09:57.423317: step 100, duration = 0.906
2017-11-07 04:10:06.683267: step 110, duration = 0.971
2017-11-07 04:10:15.476265: step 120, duration = 0.841
2017-11-07 04:10:24.353303: step 130, duration = 0.944
2017-11-07 04:10:33.551819: step 140, duration = 0.901
2017-11-07 04:10:42.439647: step 150, duration = 0.824
2017-11-07 04:10:51.446357: step 160, duration = 0.849
2017-11-07 04:11:00.177033: step 170, duration = 1.017
2017-11-07 04:11:08.790199: step 180, duration = 0.805
2017-11-07 04:11:17.570193: step 190, duration = 0.927
2017-11-07 04:11:26.230664: step 200, duration = 0.895
2017-11-07 04:11:34.985543: step 210, duration = 0.878
2017-11-07 04:11:43.805487: step 220, duration = 0.786
2017-11-07 04:11:52.436658: step 230, duration = 0.873
2017-11-07 04:12:01.571511: step 240, duration = 0.931
2017-11-07 04:12:10.159633: step 250, duration = 0.850
2017-11-07 04:12:19.133940: step 260, duration = 0.856
2017-11-07 04:12:28.180898: step 270, duration = 0.882
2017-11-07 04:12:37.038446: step 280, duration = 0.800
2017-11-07 04:12:46.173813: step 290, duration = 0.951
2017-11-07 04:12:54.929032: step 300, duration = 0.858
2017-11-07 04:13:04.438395: step 310, duration = 0.857
2017-11-07 04:13:13.182696: step 320, duration = 0.923
2017-11-07 04:13:22.051938: step 330, duration = 0.870
2017-11-07 04:13:32.293042: step 340, duration = 1.165
2017-11-07 04:13:41.196617: step 350, duration = 0.865
2017-11-07 04:13:50.210356: step 360, duration = 0.879
2017-11-07 04:13:58.079408: step 370, duration = 0.590
2017-11-07 04:14:04.104237: step 380, duration = 0.592
2017-11-07 04:14:10.067443: step 390, duration = 0.630
2017-11-07 04:14:16.223558: step 400, duration = 0.598
2017-11-07 04:14:22.301146: step 410, duration = 0.720
2017-11-07 04:14:29.117975: step 420, duration = 0.612
2017-11-07 04:14:35.249261: step 430, duration = 0.658
2017-11-07 04:14:41.259168: step 440, duration = 0.592
2017-11-07 04:14:47.466063: step 450, duration = 0.599
2017-11-07 04:14:53.356481: step 460, duration = 0.589
2017-11-07 04:14:59.312470: step 470, duration = 0.639
2017-11-07 04:15:05.195961: step 480, duration = 0.616
2017-11-07 04:15:11.255408: step 490, duration = 0.615
2017-11-07 04:15:17.326477: step 500, duration = 0.545
2017-11-07 04:15:23.366827: step 510, duration = 0.612
2017-11-07 04:15:29.301149: step 520, duration = 0.646
2017-11-07 04:15:35.082037: step 530, duration = 0.544
2017-11-07 04:15:41.171223: step 540, duration = 0.601
2017-11-07 04:15:47.255202: step 550, duration = 0.615
2017-11-07 04:15:53.110912: step 560, duration = 0.624
2017-11-07 04:15:59.200356: step 570, duration = 0.581
2017-11-07 04:16:05.397943: step 580, duration = 0.566
2017-11-07 04:16:11.380087: step 590, duration = 0.557
2017-11-07 04:16:17.361035: step 600, duration = 0.611
2017-11-07 04:16:23.416502: step 610, duration = 0.621
2017-11-07 04:16:29.335227: step 620, duration = 0.551
2017-11-07 04:16:35.265730: step 630, duration = 0.589
2017-11-07 04:16:41.301919: step 640, duration = 0.556
2017-11-07 04:16:47.354570: step 650, duration = 0.579
2017-11-07 04:16:53.256050: step 660, duration = 0.615
2017-11-07 04:16:59.320513: step 670, duration = 0.573
2017-11-07 04:17:05.411208: step 680, duration = 0.605
2017-11-07 04:17:11.195042: step 690, duration = 0.612
2017-11-07 04:17:17.290054: step 700, duration = 0.560
2017-11-07 04:17:23.318291: step 710, duration = 0.592
2017-11-07 04:17:29.453499: step 720, duration = 0.621
2017-11-07 04:17:35.317806: step 730, duration = 0.571
2017-11-07 04:17:41.302365: step 740, duration = 0.626
2017-11-07 04:17:47.435681: step 750, duration = 0.599
2017-11-07 04:17:53.478418: step 760, duration = 0.596
2017-11-07 04:17:59.417195: step 770, duration = 0.570
2017-11-07 04:18:05.288241: step 780, duration = 0.566
2017-11-07 04:18:11.212013: step 790, duration = 0.522
2017-11-07 04:18:17.073636: step 800, duration = 0.576
2017-11-07 04:18:22.996272: step 810, duration = 0.571
2017-11-07 04:18:28.934703: step 820, duration = 0.568
2017-11-07 04:18:35.294390: step 830, duration = 0.590
2017-11-07 04:18:41.448528: step 840, duration = 0.610
2017-11-07 04:18:47.612299: step 850, duration = 0.662
2017-11-07 04:18:53.518869: step 860, duration = 0.572
2017-11-07 04:18:59.358391: step 870, duration = 0.504
2017-11-07 04:19:05.519042: step 880, duration = 0.598
2017-11-07 04:19:11.516397: step 890, duration = 0.597
2017-11-07 04:19:17.655033: step 900, duration = 0.605
2017-11-07 04:19:23.741745: step 910, duration = 0.565
2017-11-07 04:19:29.758327: step 920, duration = 0.623
2017-11-07 04:19:35.864581: step 930, duration = 0.584
2017-11-07 04:19:41.842941: step 940, duration = 0.558
2017-11-07 04:19:47.989433: step 950, duration = 0.612
2017-11-07 04:19:54.123026: step 960, duration = 0.597
2017-11-07 04:20:00.000211: step 970, duration = 0.558
2017-11-07 04:20:05.951254: step 980, duration = 0.545
2017-11-07 04:20:12.052685: step 990, duration = 0.610
2017-11-07 04:20:17.479215: across 1000 steps, 0.719 +/- 0.131 sec / batch
```

## local

GPU k40

```bash
root@98154222840c:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_ba
tches 1000
2017-11-07 04:32:03.865376: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 04:32:03.986051: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-07 04:32:03.986587: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-07 04:32:03.986646: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1107 04:32:04.044290272    2250 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-07 04:32:04.048666: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-07 04:32:04.049052: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 04:32:04.227997: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 9d571d1009e06f24 with config: 
2017-11-07 04:32:05.554331: step 0, duration = 0.013
2017-11-07 04:32:05.687378: step 10, duration = 0.013
2017-11-07 04:32:05.820868: step 20, duration = 0.013
2017-11-07 04:32:05.954514: step 30, duration = 0.013
2017-11-07 04:32:06.087871: step 40, duration = 0.013
2017-11-07 04:32:06.221059: step 50, duration = 0.013
2017-11-07 04:32:06.354694: step 60, duration = 0.013
2017-11-07 04:32:06.488333: step 70, duration = 0.013
2017-11-07 04:32:06.621810: step 80, duration = 0.013
2017-11-07 04:32:06.755650: step 90, duration = 0.013
2017-11-07 04:32:06.889183: step 100, duration = 0.013
2017-11-07 04:32:07.022518: step 110, duration = 0.014
2017-11-07 04:32:07.155891: step 120, duration = 0.013
2017-11-07 04:32:07.289471: step 130, duration = 0.013
2017-11-07 04:32:07.423116: step 140, duration = 0.013
2017-11-07 04:32:07.556822: step 150, duration = 0.013
2017-11-07 04:32:07.690277: step 160, duration = 0.013
2017-11-07 04:32:07.823740: step 170, duration = 0.013
2017-11-07 04:32:07.957500: step 180, duration = 0.013
2017-11-07 04:32:08.090508: step 190, duration = 0.013
2017-11-07 04:32:08.223435: step 200, duration = 0.013
2017-11-07 04:32:08.357114: step 210, duration = 0.013
2017-11-07 04:32:08.490296: step 220, duration = 0.013
2017-11-07 04:32:08.623346: step 230, duration = 0.013
2017-11-07 04:32:08.755642: step 240, duration = 0.013
2017-11-07 04:32:08.888275: step 250, duration = 0.013
2017-11-07 04:32:09.021637: step 260, duration = 0.013
2017-11-07 04:32:09.155345: step 270, duration = 0.013
2017-11-07 04:32:09.288882: step 280, duration = 0.013
2017-11-07 04:32:09.422310: step 290, duration = 0.013
2017-11-07 04:32:09.555411: step 300, duration = 0.013
2017-11-07 04:32:09.688421: step 310, duration = 0.013
2017-11-07 04:32:09.821588: step 320, duration = 0.013
2017-11-07 04:32:09.954670: step 330, duration = 0.013
2017-11-07 04:32:10.087225: step 340, duration = 0.013
2017-11-07 04:32:10.219922: step 350, duration = 0.013
2017-11-07 04:32:10.353133: step 360, duration = 0.013
2017-11-07 04:32:10.487327: step 370, duration = 0.013
2017-11-07 04:32:10.621064: step 380, duration = 0.013
2017-11-07 04:32:10.754521: step 390, duration = 0.013
2017-11-07 04:32:10.887419: step 400, duration = 0.013
2017-11-07 04:32:11.020950: step 410, duration = 0.013
2017-11-07 04:32:11.154586: step 420, duration = 0.014
2017-11-07 04:32:11.288457: step 430, duration = 0.013
2017-11-07 04:32:11.421150: step 440, duration = 0.013
2017-11-07 04:32:11.554795: step 450, duration = 0.013
2017-11-07 04:32:11.688156: step 460, duration = 0.013
2017-11-07 04:32:11.821933: step 470, duration = 0.013
2017-11-07 04:32:11.955319: step 480, duration = 0.013
2017-11-07 04:32:12.088927: step 490, duration = 0.013
2017-11-07 04:32:12.222031: step 500, duration = 0.013
2017-11-07 04:32:12.355408: step 510, duration = 0.013
2017-11-07 04:32:12.488494: step 520, duration = 0.013
2017-11-07 04:32:12.621140: step 530, duration = 0.013
2017-11-07 04:32:12.754130: step 540, duration = 0.013
2017-11-07 04:32:12.887073: step 550, duration = 0.013
2017-11-07 04:32:13.020478: step 560, duration = 0.013
2017-11-07 04:32:13.153687: step 570, duration = 0.013
2017-11-07 04:32:13.286622: step 580, duration = 0.013
2017-11-07 04:32:13.419503: step 590, duration = 0.013
2017-11-07 04:32:13.553049: step 600, duration = 0.013
2017-11-07 04:32:13.686503: step 610, duration = 0.013
2017-11-07 04:32:13.819891: step 620, duration = 0.013
2017-11-07 04:32:13.953298: step 630, duration = 0.013
2017-11-07 04:32:14.086875: step 640, duration = 0.013
2017-11-07 04:32:14.220012: step 650, duration = 0.013
2017-11-07 04:32:14.353748: step 660, duration = 0.013
2017-11-07 04:32:14.487445: step 670, duration = 0.013
2017-11-07 04:32:14.620748: step 680, duration = 0.013
2017-11-07 04:32:14.753528: step 690, duration = 0.013
2017-11-07 04:32:14.886841: step 700, duration = 0.013
2017-11-07 04:32:15.020509: step 710, duration = 0.013
2017-11-07 04:32:15.154013: step 720, duration = 0.013
2017-11-07 04:32:15.287466: step 730, duration = 0.013
2017-11-07 04:32:15.421133: step 740, duration = 0.013
2017-11-07 04:32:15.554333: step 750, duration = 0.013
2017-11-07 04:32:15.687999: step 760, duration = 0.013
2017-11-07 04:32:15.820955: step 770, duration = 0.013
2017-11-07 04:32:15.954073: step 780, duration = 0.013
2017-11-07 04:32:16.087377: step 790, duration = 0.013
2017-11-07 04:32:16.220658: step 800, duration = 0.014
2017-11-07 04:32:16.353821: step 810, duration = 0.013
2017-11-07 04:32:16.486708: step 820, duration = 0.013
2017-11-07 04:32:16.620180: step 830, duration = 0.013
2017-11-07 04:32:16.753794: step 840, duration = 0.013
2017-11-07 04:32:16.887331: step 850, duration = 0.013
2017-11-07 04:32:17.021053: step 860, duration = 0.013
2017-11-07 04:32:17.154357: step 870, duration = 0.013
2017-11-07 04:32:17.287154: step 880, duration = 0.013
2017-11-07 04:32:17.420628: step 890, duration = 0.013
2017-11-07 04:32:17.553977: step 900, duration = 0.013
2017-11-07 04:32:17.686485: step 910, duration = 0.013
2017-11-07 04:32:17.818688: step 920, duration = 0.013
2017-11-07 04:32:17.951951: step 930, duration = 0.013
2017-11-07 04:32:18.085283: step 940, duration = 0.013
2017-11-07 04:32:18.217990: step 950, duration = 0.013
2017-11-07 04:32:18.350692: step 960, duration = 0.013
2017-11-07 04:32:18.483865: step 970, duration = 0.013
2017-11-07 04:32:18.616793: step 980, duration = 0.013
2017-11-07 04:32:18.750207: step 990, duration = 0.013
2017-11-07 04:32:18.869919: across 1000 steps, 0.014 +/- 0.022 sec / batch
```

cpu

```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 04:52:57.994018: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 04:52:57.997383: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 04:52:57.997434: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-07 04:52:57.997455: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-07 04:52:57.997514: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 04:52:57.997550: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 04:52:57.997582: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 04:52:57.997599: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 04:52:57.997761049    3451 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 04:52:58.004274: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-07 04:52:58.004994: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 04:52:58.176803: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session fdc0102301d16575 with config: 
2017-11-07 04:53:01.057863: step 0, duration = 0.229
2017-11-07 04:53:03.368278: step 10, duration = 0.231
2017-11-07 04:53:05.683764: step 20, duration = 0.230
2017-11-07 04:53:07.993614: step 30, duration = 0.229
2017-11-07 04:53:10.309447: step 40, duration = 0.231
2017-11-07 04:53:12.619554: step 50, duration = 0.231
2017-11-07 04:53:14.932440: step 60, duration = 0.234
2017-11-07 04:53:17.240671: step 70, duration = 0.229
2017-11-07 04:53:19.549506: step 80, duration = 0.233
2017-11-07 04:53:21.860989: step 90, duration = 0.230
2017-11-07 04:53:24.165134: step 100, duration = 0.231
2017-11-07 04:53:26.480401: step 110, duration = 0.233
2017-11-07 04:53:28.792189: step 120, duration = 0.232
2017-11-07 04:53:31.100868: step 130, duration = 0.233
2017-11-07 04:53:33.415900: step 140, duration = 0.231
2017-11-07 04:53:35.725554: step 150, duration = 0.232
2017-11-07 04:53:38.040406: step 160, duration = 0.230
2017-11-07 04:53:40.343990: step 170, duration = 0.230
2017-11-07 04:53:42.657549: step 180, duration = 0.231
2017-11-07 04:53:44.969175: step 190, duration = 0.231
2017-11-07 04:53:47.279383: step 200, duration = 0.231
2017-11-07 04:53:49.584017: step 210, duration = 0.230
2017-11-07 04:53:51.896824: step 220, duration = 0.231
2017-11-07 04:53:54.205763: step 230, duration = 0.232
2017-11-07 04:53:56.517517: step 240, duration = 0.231
2017-11-07 04:53:58.830153: step 250, duration = 0.230
2017-11-07 04:54:01.140880: step 260, duration = 0.233
2017-11-07 04:54:03.456560: step 270, duration = 0.231
2017-11-07 04:54:05.761890: step 280, duration = 0.231
2017-11-07 04:54:08.069719: step 290, duration = 0.230
2017-11-07 04:54:10.377854: step 300, duration = 0.231
2017-11-07 04:54:12.688907: step 310, duration = 0.231
2017-11-07 04:54:14.997972: step 320, duration = 0.232
2017-11-07 04:54:17.311397: step 330, duration = 0.231
2017-11-07 04:54:19.622197: step 340, duration = 0.232
2017-11-07 04:54:21.932936: step 350, duration = 0.232
2017-11-07 04:54:24.236975: step 360, duration = 0.229
2017-11-07 04:54:26.538939: step 370, duration = 0.229
2017-11-07 04:54:28.851678: step 380, duration = 0.230
2017-11-07 04:54:31.169165: step 390, duration = 0.234
2017-11-07 04:54:33.472172: step 400, duration = 0.229
2017-11-07 04:54:35.780634: step 410, duration = 0.232
2017-11-07 04:54:38.090846: step 420, duration = 0.231
2017-11-07 04:54:40.404703: step 430, duration = 0.233
2017-11-07 04:54:42.714001: step 440, duration = 0.231
2017-11-07 04:54:45.022848: step 450, duration = 0.231
2017-11-07 04:54:47.333164: step 460, duration = 0.232
2017-11-07 04:54:49.643806: step 470, duration = 0.230
2017-11-07 04:54:51.951782: step 480, duration = 0.228
2017-11-07 04:54:54.258638: step 490, duration = 0.231
2017-11-07 04:54:56.570334: step 500, duration = 0.230
2017-11-07 04:54:58.884206: step 510, duration = 0.231
2017-11-07 04:55:01.194131: step 520, duration = 0.233
2017-11-07 04:55:03.504499: step 530, duration = 0.231
2017-11-07 04:55:05.811512: step 540, duration = 0.230
2017-11-07 04:55:08.128606: step 550, duration = 0.231
2017-11-07 04:55:10.436843: step 560, duration = 0.230
2017-11-07 04:55:12.743864: step 570, duration = 0.230
2017-11-07 04:55:15.049771: step 580, duration = 0.231
2017-11-07 04:55:17.358562: step 590, duration = 0.229
2017-11-07 04:55:19.662322: step 600, duration = 0.231
2017-11-07 04:55:21.979553: step 610, duration = 0.235
2017-11-07 04:55:24.296803: step 620, duration = 0.231
2017-11-07 04:55:26.606118: step 630, duration = 0.230
2017-11-07 04:55:28.912557: step 640, duration = 0.231
2017-11-07 04:55:31.213536: step 650, duration = 0.230
2017-11-07 04:55:33.527643: step 660, duration = 0.230
2017-11-07 04:55:35.835072: step 670, duration = 0.229
2017-11-07 04:55:38.150472: step 680, duration = 0.231
2017-11-07 04:55:40.455907: step 690, duration = 0.229
2017-11-07 04:55:42.770928: step 700, duration = 0.232
2017-11-07 04:55:45.083567: step 710, duration = 0.229
2017-11-07 04:55:47.396040: step 720, duration = 0.231
2017-11-07 04:55:49.709834: step 730, duration = 0.231
2017-11-07 04:55:52.021784: step 740, duration = 0.231
2017-11-07 04:55:54.331822: step 750, duration = 0.231
2017-11-07 04:55:56.637201: step 760, duration = 0.231
2017-11-07 04:55:58.947429: step 770, duration = 0.232
2017-11-07 04:56:01.254812: step 780, duration = 0.230
2017-11-07 04:56:03.565204: step 790, duration = 0.231
2017-11-07 04:56:05.881522: step 800, duration = 0.231
2017-11-07 04:56:08.195088: step 810, duration = 0.231
2017-11-07 04:56:10.501504: step 820, duration = 0.230
2017-11-07 04:56:12.810206: step 830, duration = 0.230
2017-11-07 04:56:15.111418: step 840, duration = 0.231
2017-11-07 04:56:17.421087: step 850, duration = 0.230
2017-11-07 04:56:19.732178: step 860, duration = 0.230
2017-11-07 04:56:22.046498: step 870, duration = 0.234
2017-11-07 04:56:24.354785: step 880, duration = 0.230
2017-11-07 04:56:26.664910: step 890, duration = 0.230
2017-11-07 04:56:28.977560: step 900, duration = 0.232
2017-11-07 04:56:31.284272: step 910, duration = 0.231
2017-11-07 04:56:33.601530: step 920, duration = 0.229
2017-11-07 04:56:35.908495: step 930, duration = 0.229
2017-11-07 04:56:38.222251: step 940, duration = 0.230
2017-11-07 04:56:40.533434: step 950, duration = 0.231
2017-11-07 04:56:42.838038: step 960, duration = 0.230
2017-11-07 04:56:45.149286: step 970, duration = 0.231
2017-11-07 04:56:47.460731: step 980, duration = 0.230
2017-11-07 04:56:49.768924: step 990, duration = 0.230
2017-11-07 04:56:51.858250: across 1000 steps, 0.233 +/- 0.023 sec / batch
```
## Modified (add 10 layer)

layer
```bash
            net = slim.max_pool2d(net, [3, 3], 2, scope='pool1')
            net = slim.conv2d(net, 192, [5, 5], scope='conv2')
            net = slim.max_pool2d(net, [3, 3], 2, scope='pool2')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.1')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.2')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.3')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.4')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.5')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.6')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.7')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.8')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.9')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4')
            net = slim.conv2d(net, 256, [3, 3], scope='conv5')
            net = slim.max_pool2d(net, [3, 3], 2, scope='pool5')
```
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

### single

gpu
```bash
root@98154222840c:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_ba
tches 1000
2017-11-07 08:46:58.448282: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 08:46:58.549822: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-07 08:46:58.550342: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-07 08:46:58.550388: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1107 08:46:58.607474828    6866 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-07 08:46:58.611821: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-07 08:46:58.612401: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 08:46:58.958851: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 88bb5b143aec61bc with config: 
2017-11-07 08:47:00.686836: step 0, duration = 0.032
2017-11-07 08:47:01.013154: step 10, duration = 0.033
2017-11-07 08:47:01.339807: step 20, duration = 0.033
2017-11-07 08:47:01.666918: step 30, duration = 0.033
2017-11-07 08:47:01.994395: step 40, duration = 0.033
2017-11-07 08:47:02.321113: step 50, duration = 0.033
2017-11-07 08:47:02.648910: step 60, duration = 0.033
2017-11-07 08:47:02.976099: step 70, duration = 0.032
2017-11-07 08:47:03.303667: step 80, duration = 0.033
2017-11-07 08:47:03.631013: step 90, duration = 0.033
2017-11-07 08:47:03.958404: step 100, duration = 0.033
2017-11-07 08:47:04.285543: step 110, duration = 0.033
2017-11-07 08:47:04.612419: step 120, duration = 0.033
2017-11-07 08:47:04.939122: step 130, duration = 0.033
2017-11-07 08:47:05.267171: step 140, duration = 0.033
2017-11-07 08:47:05.593972: step 150, duration = 0.033
2017-11-07 08:47:05.920550: step 160, duration = 0.032
2017-11-07 08:47:06.247025: step 170, duration = 0.033
2017-11-07 08:47:06.573760: step 180, duration = 0.033
2017-11-07 08:47:06.900394: step 190, duration = 0.033
2017-11-07 08:47:07.227302: step 200, duration = 0.032
2017-11-07 08:47:07.554941: step 210, duration = 0.033
2017-11-07 08:47:07.882367: step 220, duration = 0.033
2017-11-07 08:47:08.209591: step 230, duration = 0.033
2017-11-07 08:47:08.536155: step 240, duration = 0.033
2017-11-07 08:47:08.862230: step 250, duration = 0.033
2017-11-07 08:47:09.188720: step 260, duration = 0.033
2017-11-07 08:47:09.514663: step 270, duration = 0.033
2017-11-07 08:47:09.842219: step 280, duration = 0.033
2017-11-07 08:47:10.168983: step 290, duration = 0.032
2017-11-07 08:47:10.495644: step 300, duration = 0.032
2017-11-07 08:47:10.823373: step 310, duration = 0.033
2017-11-07 08:47:11.150414: step 320, duration = 0.033
2017-11-07 08:47:11.477363: step 330, duration = 0.033
2017-11-07 08:47:11.803956: step 340, duration = 0.033
2017-11-07 08:47:12.131406: step 350, duration = 0.033
2017-11-07 08:47:12.458240: step 360, duration = 0.033
2017-11-07 08:47:12.784046: step 370, duration = 0.032
2017-11-07 08:47:13.111546: step 380, duration = 0.033
2017-11-07 08:47:13.438743: step 390, duration = 0.033
2017-11-07 08:47:13.765708: step 400, duration = 0.033
2017-11-07 08:47:14.092436: step 410, duration = 0.033
2017-11-07 08:47:14.419274: step 420, duration = 0.033
2017-11-07 08:47:14.746758: step 430, duration = 0.033
2017-11-07 08:47:15.074150: step 440, duration = 0.033
2017-11-07 08:47:15.401080: step 450, duration = 0.033
2017-11-07 08:47:15.728716: step 460, duration = 0.033
2017-11-07 08:47:16.055623: step 470, duration = 0.033
2017-11-07 08:47:16.383414: step 480, duration = 0.032
2017-11-07 08:47:16.709913: step 490, duration = 0.033
2017-11-07 08:47:17.037348: step 500, duration = 0.033
2017-11-07 08:47:17.364510: step 510, duration = 0.033
2017-11-07 08:47:17.691865: step 520, duration = 0.033
2017-11-07 08:47:18.019190: step 530, duration = 0.033
2017-11-07 08:47:18.345615: step 540, duration = 0.033
2017-11-07 08:47:18.673035: step 550, duration = 0.033
2017-11-07 08:47:18.999361: step 560, duration = 0.032
2017-11-07 08:47:19.325885: step 570, duration = 0.033
2017-11-07 08:47:19.653877: step 580, duration = 0.033
2017-11-07 08:47:19.981048: step 590, duration = 0.032
2017-11-07 08:47:20.308723: step 600, duration = 0.033
2017-11-07 08:47:20.635276: step 610, duration = 0.033
2017-11-07 08:47:20.963632: step 620, duration = 0.033
2017-11-07 08:47:21.290955: step 630, duration = 0.033
2017-11-07 08:47:21.618732: step 640, duration = 0.033
2017-11-07 08:47:21.945712: step 650, duration = 0.033
2017-11-07 08:47:22.273057: step 660, duration = 0.033
2017-11-07 08:47:22.600032: step 670, duration = 0.033
2017-11-07 08:47:22.927695: step 680, duration = 0.032
2017-11-07 08:47:23.254017: step 690, duration = 0.033
2017-11-07 08:47:23.581574: step 700, duration = 0.033
2017-11-07 08:47:23.909060: step 710, duration = 0.032
2017-11-07 08:47:24.235830: step 720, duration = 0.033
2017-11-07 08:47:24.562181: step 730, duration = 0.032
2017-11-07 08:47:24.889424: step 740, duration = 0.033
2017-11-07 08:47:25.216762: step 750, duration = 0.033
2017-11-07 08:47:25.545193: step 760, duration = 0.033
2017-11-07 08:47:25.873016: step 770, duration = 0.033
2017-11-07 08:47:26.199978: step 780, duration = 0.033
2017-11-07 08:47:26.527018: step 790, duration = 0.033
2017-11-07 08:47:26.853674: step 800, duration = 0.032
2017-11-07 08:47:27.180842: step 810, duration = 0.033
2017-11-07 08:47:27.507527: step 820, duration = 0.033
2017-11-07 08:47:27.834832: step 830, duration = 0.033
2017-11-07 08:47:28.163236: step 840, duration = 0.033
2017-11-07 08:47:28.491373: step 850, duration = 0.033
2017-11-07 08:47:28.817720: step 860, duration = 0.033
2017-11-07 08:47:29.145436: step 870, duration = 0.033
2017-11-07 08:47:29.471639: step 880, duration = 0.032
2017-11-07 08:47:29.798828: step 890, duration = 0.033
2017-11-07 08:47:30.126120: step 900, duration = 0.033
2017-11-07 08:47:30.453441: step 910, duration = 0.033
2017-11-07 08:47:30.780234: step 920, duration = 0.032
2017-11-07 08:47:31.106826: step 930, duration = 0.033
2017-11-07 08:47:31.433728: step 940, duration = 0.033
2017-11-07 08:47:31.761314: step 950, duration = 0.033
2017-11-07 08:47:32.088316: step 960, duration = 0.033
2017-11-07 08:47:32.415697: step 970, duration = 0.033
2017-11-07 08:47:32.743036: step 980, duration = 0.033
2017-11-07 08:47:33.070072: step 990, duration = 0.033
2017-11-07 08:47:33.366015: across 1000 steps, 0.034 +/- 0.023 sec / batch
```


layer

```bash
            net = slim.conv2d(inputs, 64, [11, 11], 4, padding='VALID',
                              scope='conv1')
            net = slim.max_pool2d(net, [3, 3], 2, scope='pool1')
            net = slim.conv2d(net, 192, [5, 5], scope='conv2')
            net = slim.max_pool2d(net, [3, 3], 2, scope='pool2')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.1')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.2')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.3')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.4')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.5')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.6')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.7')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.8')
            net = slim.conv2d(net, 384, [3, 3], scope='conv3.9')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.1')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.2')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.3')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.4')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.5')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.6')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.7')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.8')
            net = slim.conv2d(net, 384, [3, 3], scope='conv4.9')
            net = slim.conv2d(net, 256, [3, 3], scope='conv5')
            net = slim.max_pool2d(net, [3, 3], 2, scope='pool5')
```
ps 1
```bash
root@a22e6717d336:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name ps --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 13:04:12.440354: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 13:04:12.445034: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 13:04:12.445147: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: a22e6717d336
2017-11-07 13:04:12.445192: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: a22e6717d336
2017-11-07 13:04:12.445276: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 13:04:12.445337: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 13:04:12.445373: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 13:04:12.445391: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 13:04:12.445698457     800 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 13:04:12.452421: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> localhost:2222}
2017-11-07 13:04:12.452505: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-07 13:04:12.453196: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
```
worker 1

```bash
root@98154222840c:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-07 13:04:47.700030: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 13:04:47.801975: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-07 13:04:47.802473: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-07 13:04:47.802519: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1107 13:04:47.858900058    8291 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-07 13:04:47.865615: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 13:04:47.865721: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-07 13:04:47.866481: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 13:04:58.438432: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:2
2017-11-07 13:05:03.454152: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 2feaff26548834a9 with config: 
2017-11-07 13:05:08.958645: step 0, duration = 0.292
2017-11-07 13:05:11.971562: step 10, duration = 0.309
2017-11-07 13:05:14.951934: step 20, duration = 0.297
2017-11-07 13:05:17.941937: step 30, duration = 0.307
2017-11-07 13:05:20.934862: step 40, duration = 0.314
2017-11-07 13:05:23.984735: step 50, duration = 0.310
2017-11-07 13:05:26.989820: step 60, duration = 0.303
2017-11-07 13:05:29.952667: step 70, duration = 0.302
2017-11-07 13:05:32.965805: step 80, duration = 0.290
2017-11-07 13:05:36.864096: step 90, duration = 0.462
2017-11-07 13:05:41.441015: step 100, duration = 0.500
2017-11-07 13:05:46.001447: step 110, duration = 0.453
2017-11-07 13:05:50.435335: step 120, duration = 0.420
2017-11-07 13:05:54.980404: step 130, duration = 0.497
2017-11-07 13:05:59.547468: step 140, duration = 0.428
2017-11-07 13:06:04.083728: step 150, duration = 0.462
2017-11-07 13:06:08.703175: step 160, duration = 0.464
2017-11-07 13:06:13.246629: step 170, duration = 0.407
2017-11-07 13:06:17.724530: step 180, duration = 0.480
2017-11-07 13:06:22.442785: step 190, duration = 0.511
2017-11-07 13:06:26.772952: step 200, duration = 0.392
2017-11-07 13:06:31.431380: step 210, duration = 0.454
2017-11-07 13:06:35.921232: step 220, duration = 0.490
2017-11-07 13:06:40.535504: step 230, duration = 0.431
2017-11-07 13:06:45.265232: step 240, duration = 0.552
2017-11-07 13:06:49.711251: step 250, duration = 0.413
2017-11-07 13:06:54.420100: step 260, duration = 0.470
2017-11-07 13:06:58.846439: step 270, duration = 0.478
2017-11-07 13:07:03.346875: step 280, duration = 0.462
2017-11-07 13:07:07.903425: step 290, duration = 0.377
2017-11-07 13:07:12.548440: step 300, duration = 0.439
2017-11-07 13:07:17.050298: step 310, duration = 0.479
2017-11-07 13:07:21.628406: step 320, duration = 0.414
2017-11-07 13:07:26.273203: step 330, duration = 0.453
2017-11-07 13:07:30.874200: step 340, duration = 0.430
2017-11-07 13:07:35.371185: step 350, duration = 0.522
2017-11-07 13:07:39.805255: step 360, duration = 0.431
2017-11-07 13:07:44.310039: step 370, duration = 0.433
2017-11-07 13:07:49.041209: step 380, duration = 0.486
2017-11-07 13:07:53.523348: step 390, duration = 0.451
2017-11-07 13:07:58.143084: step 400, duration = 0.437
2017-11-07 13:08:02.671833: step 410, duration = 0.415
2017-11-07 13:08:07.132410: step 420, duration = 0.436
2017-11-07 13:08:11.629845: step 430, duration = 0.493
2017-11-07 13:08:16.076457: step 440, duration = 0.406
2017-11-07 13:08:20.631470: step 450, duration = 0.530
2017-11-07 13:08:25.241028: step 460, duration = 0.480
2017-11-07 13:08:29.679406: step 470, duration = 0.464
2017-11-07 13:08:34.035209: step 480, duration = 0.516
2017-11-07 13:08:38.660659: step 490, duration = 0.509
2017-11-07 13:08:43.262597: step 500, duration = 0.498
2017-11-07 13:08:47.873485: step 510, duration = 0.476
2017-11-07 13:08:52.383652: step 520, duration = 0.405
2017-11-07 13:08:56.823490: step 530, duration = 0.441
2017-11-07 13:09:01.585517: step 540, duration = 0.531
2017-11-07 13:09:05.962647: step 550, duration = 0.413
2017-11-07 13:09:10.524571: step 560, duration = 0.530
2017-11-07 13:09:14.965630: step 570, duration = 0.487
2017-11-07 13:09:19.415829: step 580, duration = 0.453
2017-11-07 13:09:23.952850: step 590, duration = 0.460
2017-11-07 13:09:28.559258: step 600, duration = 0.453
2017-11-07 13:09:32.999964: step 610, duration = 0.420
2017-11-07 13:09:37.392519: step 620, duration = 0.474
2017-11-07 13:09:41.906558: step 630, duration = 0.431
2017-11-07 13:09:46.391129: step 640, duration = 0.420
2017-11-07 13:09:51.229430: step 650, duration = 0.548
2017-11-07 13:09:55.836671: step 660, duration = 0.431
2017-11-07 13:10:00.485367: step 670, duration = 0.461
2017-11-07 13:10:05.090507: step 680, duration = 0.438
2017-11-07 13:10:09.708710: step 690, duration = 0.453
2017-11-07 13:10:14.334629: step 700, duration = 0.506
2017-11-07 13:10:18.744600: step 710, duration = 0.415
2017-11-07 13:10:23.227688: step 720, duration = 0.456
2017-11-07 13:10:27.764486: step 730, duration = 0.450
2017-11-07 13:10:32.345194: step 740, duration = 0.428
2017-11-07 13:10:36.881633: step 750, duration = 0.424
2017-11-07 13:10:41.188419: step 760, duration = 0.419
2017-11-07 13:10:45.678870: step 770, duration = 0.459
2017-11-07 13:10:50.153654: step 780, duration = 0.516
2017-11-07 13:10:54.563115: step 790, duration = 0.387
2017-11-07 13:10:58.957012: step 800, duration = 0.435
2017-11-07 13:11:03.461893: step 810, duration = 0.475
2017-11-07 13:11:08.366778: step 820, duration = 0.505
2017-11-07 13:11:12.811543: step 830, duration = 0.455
2017-11-07 13:11:17.420042: step 840, duration = 0.468
2017-11-07 13:11:21.860694: step 850, duration = 0.423
2017-11-07 13:11:26.167627: step 860, duration = 0.409
2017-11-07 13:11:30.821184: step 870, duration = 0.539
2017-11-07 13:11:35.250039: step 880, duration = 0.438
2017-11-07 13:11:39.640401: step 890, duration = 0.390
2017-11-07 13:11:44.009820: step 900, duration = 0.405
2017-11-07 13:11:48.575353: step 910, duration = 0.396
2017-11-07 13:11:53.154516: step 920, duration = 0.443
2017-11-07 13:11:57.825286: step 930, duration = 0.513
2017-11-07 13:12:02.431169: step 940, duration = 0.394
2017-11-07 13:12:07.161598: step 950, duration = 0.468
2017-11-07 13:12:11.752685: step 960, duration = 0.419
2017-11-07 13:12:16.278030: step 970, duration = 0.500
2017-11-07 13:12:20.755332: step 980, duration = 0.426
2017-11-07 13:12:25.336761: step 990, duration = 0.422
2017-11-07 13:12:29.353180: across 1000 steps, 0.445 +/- 0.049 sec / batch
```

worker 2
```bash

root@610546c83414:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 1 --batch_size 10 --num_batches 1000
2017-11-07 13:04:19.101113: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 13:04:19.105215: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 13:04:19.105276: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 610546c83414
2017-11-07 13:04:19.105300: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 610546c83414
2017-11-07 13:04:19.105356: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 13:04:19.105394: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 13:04:19.105434: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 13:04:19.105459: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 13:04:19.105617809    3474 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 13:04:19.111887: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 13:04:19.111978: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> localhost:2222, 2 -> 172.17.0.5:2222}
2017-11-07 13:04:19.112734: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 13:04:21.680791: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 34bc1dbe415cf1ff with config: 
2017-11-07 13:05:03.879880: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 303869706eebf146 with config: 
2017-11-07 13:05:34.178231: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session d8a4b1db5b8cd3d7 with config: 
2017-11-07 13:06:10.643410: step 0, duration = 3.291
2017-11-07 13:06:43.809373: step 10, duration = 3.216
2017-11-07 13:07:16.816275: step 20, duration = 3.388
2017-11-07 13:07:50.280413: step 30, duration = 3.363
2017-11-07 13:08:23.685942: step 40, duration = 3.490
2017-11-07 13:08:56.652708: step 50, duration = 3.391
2017-11-07 13:09:29.859608: step 60, duration = 3.301
2017-11-07 13:10:02.879244: step 70, duration = 3.311
2017-11-07 13:10:35.989501: step 80, duration = 3.309
2017-11-07 13:11:09.625512: step 90, duration = 3.266
2017-11-07 13:11:43.113206: step 100, duration = 3.291
2017-11-07 13:12:15.984319: step 110, duration = 3.214
2017-11-07 13:12:42.459390: step 120, duration = 2.138
2017-11-07 13:13:04.522672: step 130, duration = 2.251
2017-11-07 13:13:26.477251: step 140, duration = 2.208
2017-11-07 13:13:48.721204: step 150, duration = 2.240
2017-11-07 13:14:10.562729: step 160, duration = 2.252
2017-11-07 13:14:32.848344: step 170, duration = 2.193
2017-11-07 13:14:55.100585: step 180, duration = 2.196
2017-11-07 13:15:17.338481: step 190, duration = 2.230
2017-11-07 13:15:39.944028: step 200, duration = 2.224
2017-11-07 13:16:02.387938: step 210, duration = 2.236
2017-11-07 13:16:24.817251: step 220, duration = 2.127
2017-11-07 13:16:47.197201: step 230, duration = 2.256
2017-11-07 13:17:09.148537: step 240, duration = 2.143
2017-11-07 13:17:31.443129: step 250, duration = 2.207
2017-11-07 13:17:53.396520: step 260, duration = 2.223
2017-11-07 13:18:15.350206: step 270, duration = 2.161
2017-11-07 13:18:37.409207: step 280, duration = 2.201
2017-11-07 13:18:59.326472: step 290, duration = 2.187
2017-11-07 13:19:21.563534: step 300, duration = 2.272
2017-11-07 13:19:43.508769: step 310, duration = 2.155
2017-11-07 13:20:05.455659: step 320, duration = 2.204
2017-11-07 13:20:27.435233: step 330, duration = 2.217
2017-11-07 13:20:49.669457: step 340, duration = 2.183
2017-11-07 13:21:11.771047: step 350, duration = 2.269
2017-11-07 13:34:27.078142: step 710, duration = 2.203
2017-11-07 13:34:49.069209: step 720, duration = 2.183
2017-11-07 13:35:11.188495: step 730, duration = 2.240
2017-11-07 13:35:33.270411: step 740, duration = 2.269
2017-11-07 13:35:55.506482: step 750, duration = 2.285
2017-11-07 13:36:17.457306: step 760, duration = 2.228
2017-11-07 13:36:39.242434: step 770, duration = 2.183
2017-11-07 13:37:01.390280: step 780, duration = 2.156
2017-11-07 13:37:23.498206: step 790, duration = 2.195
2017-11-07 13:37:45.398894: step 800, duration = 2.186
2017-11-07 13:38:07.427238: step 810, duration = 2.171
2017-11-07 13:38:29.467431: step 820, duration = 2.225
2017-11-07 13:38:51.585473: step 830, duration = 2.240
2017-11-07 13:39:13.943460: step 840, duration = 2.248
2017-11-07 13:39:36.373390: step 850, duration = 2.288
2017-11-07 13:39:58.693976: step 860, duration = 2.245
2017-11-07 13:40:21.217409: step 870, duration = 2.218
2017-11-07 13:40:43.268235: step 880, duration = 2.226
2017-11-07 13:41:05.565240: step 890, duration = 2.316
2017-11-07 13:41:27.794407: step 900, duration = 2.247
2017-11-07 13:41:49.824199: step 910, duration = 2.108
2017-11-07 13:42:12.083469: step 920, duration = 2.187
2017-11-07 13:42:34.162209: step 930, duration = 2.210
2017-11-07 13:42:56.187279: step 940, duration = 2.207
2017-11-07 13:43:18.526441: step 950, duration = 2.231
2017-11-07 13:43:40.636574: step 960, duration = 2.224
2017-11-07 13:44:02.645654: step 970, duration = 2.213
2017-11-07 13:44:24.279209: step 980, duration = 2.168
2017-11-07 13:44:46.299059: step 990, duration = 2.218
2017-11-07 13:45:04.660371: across 1000 steps, 2.370 +/- 0.290 sec / batch
```

worker 3

```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 2 --batch_size 10 --num_batches 1000
2017-11-07 13:05:03.237415: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-07 13:05:03.240412: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-07 13:05:03.240478: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-07 13:05:03.240501: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-07 13:05:03.240553: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-07 13:05:03.240590: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-07 13:05:03.240629: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-07 13:05:03.240648: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1107 13:05:03.240814051    9118 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-07 13:05:03.244620: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-07 13:05:03.244686: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> localhost:2222}
2017-11-07 13:05:03.245374: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-07 13:05:03.880205: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 1684ffbec1f0586f with config: 
2017-11-07 13:05:34.221434: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session c87f4207b6002f39 with config: 
2017-11-07 13:06:11.687356: step 0, duration = 3.210
2017-11-07 13:06:44.964436: step 10, duration = 3.189
2017-11-07 13:07:18.488493: step 20, duration = 3.420
2017-11-07 13:07:51.544850: step 30, duration = 3.333
2017-11-07 13:08:24.741022: step 40, duration = 3.253
2017-11-07 13:08:57.975076: step 50, duration = 3.296
2017-11-07 13:09:31.092049: step 60, duration = 3.310
2017-11-07 13:10:04.014383: step 70, duration = 3.375
2017-11-07 13:10:36.906415: step 80, duration = 3.262
2017-11-07 13:11:10.203384: step 90, duration = 3.398
2017-11-07 13:11:44.186188: step 100, duration = 3.535
2017-11-07 13:12:17.316380: step 110, duration = 3.464
2017-11-07 13:12:43.664519: step 120, duration = 2.226
2017-11-07 13:13:05.653203: step 130, duration = 2.154
2017-11-07 13:13:27.845517: step 140, duration = 2.153
2017-11-07 13:13:49.713598: step 150, duration = 2.189
2017-11-07 13:14:11.967421: step 160, duration = 2.141
2017-11-07 13:14:33.790035: step 170, duration = 2.229
2017-11-07 13:14:55.569306: step 180, duration = 2.155
2017-11-07 13:15:17.776407: step 190, duration = 2.180
2017-11-07 13:15:39.924502: step 200, duration = 2.312
2017-11-07 13:16:02.376864: step 210, duration = 2.250
2017-11-07 13:16:24.615669: step 220, duration = 2.234
2017-11-07 13:16:46.760596: step 230, duration = 2.237
2017-11-07 13:17:08.964042: step 240, duration = 2.279
2017-11-07 13:17:31.462444: step 250, duration = 2.264
2017-11-07 13:17:53.951004: step 260, duration = 2.247
2017-11-07 13:18:16.000208: step 270, duration = 2.253
2017-11-07 13:18:38.019205: step 280, duration = 2.261
2017-11-07 13:19:00.170630: step 290, duration = 2.238
2017-11-07 13:19:22.057922: step 300, duration = 2.156
2017-11-07 13:19:44.193203: step 310, duration = 2.249
2017-11-07 13:20:06.250441: step 320, duration = 2.198
2017-11-07 13:20:28.256212: step 330, duration = 2.125
2017-11-07 13:20:50.150861: step 340, duration = 2.202
2017-11-07 13:21:12.111147: step 350, duration = 2.199
2017-11-07 13:21:34.203245: step 360, duration = 2.183
2017-11-07 13:34:26.172435: step 710, duration = 2.192
2017-11-07 13:34:48.226531: step 720, duration = 2.255
2017-11-07 13:35:10.105787: step 730, duration = 2.180
2017-11-07 13:35:32.046201: step 740, duration = 2.185
2017-11-07 13:35:53.813321: step 750, duration = 2.133
2017-11-07 13:36:15.773510: step 760, duration = 2.206
2017-11-07 13:36:37.903485: step 770, duration = 2.242
2017-11-07 13:36:59.713707: step 780, duration = 2.190
2017-11-07 13:37:21.711217: step 790, duration = 2.212
2017-11-07 13:37:43.752855: step 800, duration = 2.159
2017-11-07 13:38:05.767513: step 810, duration = 2.158
2017-11-07 13:38:27.796440: step 820, duration = 2.199
2017-11-07 13:38:49.803644: step 830, duration = 2.170
2017-11-07 13:39:11.686650: step 840, duration = 2.194
2017-11-07 13:39:34.061398: step 850, duration = 2.309
2017-11-07 13:39:56.422142: step 860, duration = 2.233
2017-11-07 13:40:18.598503: step 870, duration = 2.158
2017-11-07 13:40:40.779406: step 880, duration = 2.252
2017-11-07 13:41:03.005514: step 890, duration = 2.177
2017-11-07 13:41:25.161202: step 900, duration = 2.192
2017-11-07 13:41:46.954195: step 910, duration = 2.170
2017-11-07 13:42:08.765368: step 920, duration = 2.137
2017-11-07 13:42:30.730545: step 930, duration = 2.257
2017-11-07 13:42:52.753088: step 940, duration = 2.161
2017-11-07 13:43:14.574337: step 950, duration = 2.254
2017-11-07 13:43:36.623851: step 960, duration = 2.216
2017-11-07 13:43:58.786179: step 970, duration = 2.271
2017-11-07 13:44:21.202194: step 980, duration = 2.221
2017-11-07 13:44:43.230783: step 990, duration = 2.190
2017-11-07 13:45:02.985217: across 1000 steps, 2.369 +/- 0.292 sec / batch
```