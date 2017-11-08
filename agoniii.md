

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

gpu

```bash
root@98154222840c:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts localhost:2222 --job_name worker --task_index 
0 --batch_size 10 --num_batches 1000
2017-11-08 04:12:53.434425: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 04:12:53.540688: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-08 04:12:53.541149: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-08 04:12:53.541196: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1108 04:12:53.597451028    9386 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-08 04:12:53.601806: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 04:12:53.602471: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 04:12:54.152074: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 51ff1864a361b77c with config: 
2017-11-08 04:12:56.288853: step 0, duration = 0.052
2017-11-08 04:12:56.812456: step 10, duration = 0.052
2017-11-08 04:12:57.335897: step 20, duration = 0.052
2017-11-08 04:12:57.859478: step 30, duration = 0.052
2017-11-08 04:12:58.380929: step 40, duration = 0.052
2017-11-08 04:12:58.903513: step 50, duration = 0.052
2017-11-08 04:12:59.427304: step 60, duration = 0.053
2017-11-08 04:12:59.949832: step 70, duration = 0.052
2017-11-08 04:13:00.473843: step 80, duration = 0.052
2017-11-08 04:13:00.997325: step 90, duration = 0.052
2017-11-08 04:13:01.521073: step 100, duration = 0.052
2017-11-08 04:13:02.044274: step 110, duration = 0.052
2017-11-08 04:13:02.568991: step 120, duration = 0.053
2017-11-08 04:13:03.091371: step 130, duration = 0.052
2017-11-08 04:13:03.613663: step 140, duration = 0.052
2017-11-08 04:13:04.136631: step 150, duration = 0.053
2017-11-08 04:13:04.660123: step 160, duration = 0.053
2017-11-08 04:13:05.184153: step 170, duration = 0.052
2017-11-08 04:13:05.706240: step 180, duration = 0.052
2017-11-08 04:13:06.229650: step 190, duration = 0.052
2017-11-08 04:13:06.752622: step 200, duration = 0.052
2017-11-08 04:13:07.275796: step 210, duration = 0.052
2017-11-08 04:13:07.797992: step 220, duration = 0.052
2017-11-08 04:13:08.321842: step 230, duration = 0.053
2017-11-08 04:13:08.844614: step 240, duration = 0.052
2017-11-08 04:13:09.367390: step 250, duration = 0.052
2017-11-08 04:13:09.890346: step 260, duration = 0.052
2017-11-08 04:13:10.412018: step 270, duration = 0.052
2017-11-08 04:13:10.935822: step 280, duration = 0.053
2017-11-08 04:13:11.460270: step 290, duration = 0.053
2017-11-08 04:13:11.984503: step 300, duration = 0.053
2017-11-08 04:13:12.506810: step 310, duration = 0.052
2017-11-08 04:13:13.030829: step 320, duration = 0.052
2017-11-08 04:13:13.556145: step 330, duration = 0.053
2017-11-08 04:13:14.080456: step 340, duration = 0.053
2017-11-08 04:13:14.602711: step 350, duration = 0.052
2017-11-08 04:13:15.125049: step 360, duration = 0.052
2017-11-08 04:13:15.649230: step 370, duration = 0.053
2017-11-08 04:13:16.173518: step 380, duration = 0.053
2017-11-08 04:13:16.696638: step 390, duration = 0.052
2017-11-08 04:13:17.220102: step 400, duration = 0.053
2017-11-08 04:13:17.744044: step 410, duration = 0.052
2017-11-08 04:13:18.269144: step 420, duration = 0.052
2017-11-08 04:13:18.792227: step 430, duration = 0.052
2017-11-08 04:13:19.315463: step 440, duration = 0.053
2017-11-08 04:13:19.840663: step 450, duration = 0.052
2017-11-08 04:13:20.362502: step 460, duration = 0.052
2017-11-08 04:13:20.886364: step 470, duration = 0.052
2017-11-08 04:13:21.409362: step 480, duration = 0.052
2017-11-08 04:13:21.932437: step 490, duration = 0.052
2017-11-08 04:13:22.455374: step 500, duration = 0.052
2017-11-08 04:13:22.979469: step 510, duration = 0.052
2017-11-08 04:13:23.502904: step 520, duration = 0.052
2017-11-08 04:13:24.026253: step 530, duration = 0.052
2017-11-08 04:13:24.550219: step 540, duration = 0.052
2017-11-08 04:13:25.073146: step 550, duration = 0.052
2017-11-08 04:13:25.596747: step 560, duration = 0.053
2017-11-08 04:13:26.119778: step 570, duration = 0.052
2017-11-08 04:13:26.643893: step 580, duration = 0.052
2017-11-08 04:13:27.166873: step 590, duration = 0.052
2017-11-08 04:13:27.689563: step 600, duration = 0.052
2017-11-08 04:13:28.213803: step 610, duration = 0.052
2017-11-08 04:13:28.737151: step 620, duration = 0.052
2017-11-08 04:13:29.260854: step 630, duration = 0.052
2017-11-08 04:13:29.784023: step 640, duration = 0.052
2017-11-08 04:13:30.308939: step 650, duration = 0.053
2017-11-08 04:13:30.832810: step 660, duration = 0.052
2017-11-08 04:13:31.356278: step 670, duration = 0.052
2017-11-08 04:13:31.879915: step 680, duration = 0.052
2017-11-08 04:13:32.402917: step 690, duration = 0.052
2017-11-08 04:13:32.926124: step 700, duration = 0.052
2017-11-08 04:13:33.449979: step 710, duration = 0.052
2017-11-08 04:13:33.973748: step 720, duration = 0.052
2017-11-08 04:13:34.496020: step 730, duration = 0.052
2017-11-08 04:13:35.018801: step 740, duration = 0.052
2017-11-08 04:13:35.541658: step 750, duration = 0.053
2017-11-08 04:13:36.065037: step 760, duration = 0.052
2017-11-08 04:13:36.588744: step 770, duration = 0.052
2017-11-08 04:13:37.111470: step 780, duration = 0.052
2017-11-08 04:13:37.634837: step 790, duration = 0.052
2017-11-08 04:13:38.157128: step 800, duration = 0.052
2017-11-08 04:13:38.681277: step 810, duration = 0.052
2017-11-08 04:13:39.204777: step 820, duration = 0.052
2017-11-08 04:13:39.729503: step 830, duration = 0.053
2017-11-08 04:13:40.252932: step 840, duration = 0.052
2017-11-08 04:13:40.776199: step 850, duration = 0.052
2017-11-08 04:13:41.300605: step 860, duration = 0.053
2017-11-08 04:13:41.822902: step 870, duration = 0.053
2017-11-08 04:13:42.347057: step 880, duration = 0.052
2017-11-08 04:13:42.870296: step 890, duration = 0.052
2017-11-08 04:13:43.393534: step 900, duration = 0.052
2017-11-08 04:13:43.917992: step 910, duration = 0.052
2017-11-08 04:13:44.440571: step 920, duration = 0.053
2017-11-08 04:13:44.965160: step 930, duration = 0.053
2017-11-08 04:13:45.489360: step 940, duration = 0.052
2017-11-08 04:13:46.012428: step 950, duration = 0.052
2017-11-08 04:13:46.535587: step 960, duration = 0.052
2017-11-08 04:13:47.059056: step 970, duration = 0.052
2017-11-08 04:13:47.582748: step 980, duration = 0.052
2017-11-08 04:13:48.106042: step 990, duration = 0.052
2017-11-08 04:13:48.575917: across 1000 steps, 0.054 +/- 0.023 sec / batch```

cpu

```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-08 04:19:31.903930: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 04:19:31.907383: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 04:19:31.907444: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-08 04:19:31.907484: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-08 04:19:31.907536: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 04:19:31.907572: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 04:19:31.907608: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 04:19:31.907627: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 04:19:31.907782013   11203 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 04:19:31.911666: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 04:19:31.912240: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 04:19:32.456810: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session eaf154aba1810242 with config: 
2017-11-08 04:19:44.424364: step 0, duration = 1.017
2017-11-08 04:19:54.590559: step 10, duration = 1.011
2017-11-08 04:20:04.823123: step 20, duration = 1.027
2017-11-08 04:20:14.995392: step 30, duration = 1.018
2017-11-08 04:20:25.190196: step 40, duration = 1.016
2017-11-08 04:20:35.359608: step 50, duration = 1.019
2017-11-08 04:20:45.569548: step 60, duration = 1.019
2017-11-08 04:20:55.740034: step 70, duration = 1.020
2017-11-08 04:21:05.929144: step 80, duration = 1.012
2017-11-08 04:21:16.092978: step 90, duration = 1.015
2017-11-08 04:21:26.280406: step 100, duration = 1.017
2017-11-08 04:21:36.448517: step 110, duration = 1.015
2017-11-08 04:21:46.653188: step 120, duration = 1.018
2017-11-08 04:21:56.814338: step 130, duration = 1.012
2017-11-08 04:22:07.023900: step 140, duration = 1.015
2017-11-08 04:22:17.179755: step 150, duration = 1.015
2017-11-08 04:22:27.373098: step 160, duration = 1.013
2017-11-08 04:22:37.547826: step 170, duration = 1.018
2017-11-08 04:22:47.731428: step 180, duration = 1.016
2017-11-08 04:22:57.902864: step 190, duration = 1.018
2017-11-08 04:23:08.100004: step 200, duration = 1.016
2017-11-08 04:23:18.276312: step 210, duration = 1.017
2017-11-08 04:23:28.480388: step 220, duration = 1.025
2017-11-08 04:23:38.655546: step 230, duration = 1.014
2017-11-08 04:23:48.842169: step 240, duration = 1.019
2017-11-08 04:23:59.015643: step 250, duration = 1.020
2017-11-08 04:24:09.242298: step 260, duration = 1.021
2017-11-08 04:24:19.458618: step 270, duration = 1.051
2017-11-08 04:24:29.642380: step 280, duration = 1.016
2017-11-08 04:24:39.832484: step 290, duration = 1.043
2017-11-08 04:24:49.992572: step 300, duration = 1.018
2017-11-08 04:25:00.191355: step 310, duration = 1.042
2017-11-08 04:25:10.358458: step 320, duration = 1.016
2017-11-08 04:25:20.565067: step 330, duration = 1.015
2017-11-08 04:25:30.740941: step 340, duration = 1.016
2017-11-08 04:25:40.949635: step 350, duration = 1.021
2017-11-08 04:25:51.127435: step 360, duration = 1.021
2017-11-08 04:26:01.335499: step 370, duration = 1.020
2017-11-08 04:26:11.512449: step 380, duration = 1.013
2017-11-08 04:26:21.715173: step 390, duration = 1.020
2017-11-08 04:26:31.884844: step 400, duration = 1.019
2017-11-08 04:26:42.076367: step 410, duration = 1.016
2017-11-08 04:26:52.266140: step 420, duration = 1.023
2017-11-08 04:27:02.494483: step 430, duration = 1.023
2017-11-08 04:27:12.672331: step 440, duration = 1.020
2017-11-08 04:27:22.901692: step 450, duration = 1.015
2017-11-08 04:27:33.104663: step 460, duration = 1.019
2017-11-08 04:27:43.300349: step 470, duration = 1.015
2017-11-08 04:27:53.476079: step 480, duration = 1.018
2017-11-08 04:28:03.696237: step 490, duration = 1.017
2017-11-08 04:28:13.861601: step 500, duration = 1.017
2017-11-08 04:28:24.059471: step 510, duration = 1.018
2017-11-08 04:28:34.264496: step 520, duration = 1.020
2017-11-08 04:28:44.463996: step 530, duration = 1.018
2017-11-08 04:28:54.639650: step 540, duration = 1.016
2017-11-08 04:29:04.842477: step 550, duration = 1.019
2017-11-08 04:29:15.027962: step 560, duration = 1.016
2017-11-08 04:29:25.245321: step 570, duration = 1.022
2017-11-08 04:29:35.526044: step 580, duration = 1.012
2017-11-08 04:29:45.742080: step 590, duration = 1.020
2017-11-08 04:29:55.912300: step 600, duration = 1.018
2017-11-08 04:30:06.149321: step 610, duration = 1.020
2017-11-08 04:30:16.325901: step 620, duration = 1.015
2017-11-08 04:30:26.522136: step 630, duration = 1.015
2017-11-08 04:30:36.693453: step 640, duration = 1.022
2017-11-08 04:30:46.892822: step 650, duration = 1.019
2017-11-08 04:30:57.058012: step 660, duration = 1.021
2017-11-08 04:31:07.239485: step 670, duration = 1.015
2017-11-08 04:31:17.416409: step 680, duration = 1.017
2017-11-08 04:31:27.633349: step 690, duration = 1.013
2017-11-08 04:31:37.816241: step 700, duration = 1.019
2017-11-08 04:31:48.019421: step 710, duration = 1.016
2017-11-08 04:31:58.188844: step 720, duration = 1.012
2017-11-08 04:32:08.395210: step 730, duration = 1.016
2017-11-08 04:32:18.559312: step 740, duration = 1.022
2017-11-08 04:32:28.763187: step 750, duration = 1.014
2017-11-08 04:32:38.935473: step 760, duration = 1.022
2017-11-08 04:32:49.125491: step 770, duration = 1.018
2017-11-08 04:32:59.319009: step 780, duration = 1.023
2017-11-08 04:33:09.491148: step 790, duration = 1.018
2017-11-08 04:33:19.702766: step 800, duration = 1.049
2017-11-08 04:33:29.862855: step 810, duration = 1.009
2017-11-08 04:33:40.071069: step 820, duration = 1.041
2017-11-08 04:33:50.254686: step 830, duration = 1.024
2017-11-08 04:34:00.435658: step 840, duration = 1.015
2017-11-08 04:34:10.605682: step 850, duration = 1.013
2017-11-08 04:34:20.800330: step 860, duration = 1.016
2017-11-08 04:34:30.969580: step 870, duration = 1.012
2017-11-08 04:34:41.172800: step 880, duration = 1.017
2017-11-08 04:34:51.371956: step 890, duration = 1.021
2017-11-08 04:35:01.587890: step 900, duration = 1.019
2017-11-08 04:35:11.775858: step 910, duration = 1.021
2017-11-08 04:35:21.974603: step 920, duration = 1.018
2017-11-08 04:35:32.157532: step 930, duration = 1.015
2017-11-08 04:35:42.357386: step 940, duration = 1.020
2017-11-08 04:35:52.524428: step 950, duration = 1.015
2017-11-08 04:36:02.744841: step 960, duration = 1.019
2017-11-08 04:36:12.928623: step 970, duration = 1.017
2017-11-08 04:36:23.131238: step 980, duration = 1.016
2017-11-08 04:36:33.303945: step 990, duration = 1.020
2017-11-08 04:36:42.498238: across 1000 steps, 1.029 +/- 0.102 sec / batch
```
cpu

```bash

root@5dee89c483b9:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-08 04:56:20.647397: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 04:56:20.651905: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 04:56:20.651999: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-08 04:56:20.652042: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-08 04:56:20.652156: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 04:56:20.652191: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 04:56:20.652228: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 04:56:20.652246: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 04:56:20.652408491   12722 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 04:56:20.658495: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 04:56:20.659151: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 04:56:20.992032: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 24f46ec6456bfadc with config: 
2017-11-08 04:56:28.445341: step 0, duration = 0.632
2017-11-08 04:56:34.681718: step 10, duration = 0.628
2017-11-08 04:56:40.966012: step 20, duration = 0.623
2017-11-08 04:56:47.224785: step 30, duration = 0.628
2017-11-08 04:56:53.483258: step 40, duration = 0.625
2017-11-08 04:56:59.781509: step 50, duration = 0.652
2017-11-08 04:57:06.025185: step 60, duration = 0.622
2017-11-08 04:57:12.276845: step 70, duration = 0.625
2017-11-08 04:57:18.530378: step 80, duration = 0.624
2017-11-08 04:57:24.812771: step 90, duration = 0.622
2017-11-08 04:57:31.074127: step 100, duration = 0.623
2017-11-08 04:57:37.320760: step 110, duration = 0.621
2017-11-08 04:57:43.582844: step 120, duration = 0.623
2017-11-08 04:57:49.817503: step 130, duration = 0.628
2017-11-08 04:57:56.067000: step 140, duration = 0.625
2017-11-08 04:58:02.336954: step 150, duration = 0.630
2017-11-08 04:58:08.596307: step 160, duration = 0.624
2017-11-08 04:58:14.840223: step 170, duration = 0.622
2017-11-08 04:58:21.118566: step 180, duration = 0.624
2017-11-08 04:58:27.362862: step 190, duration = 0.621
2017-11-08 04:58:33.623598: step 200, duration = 0.626
2017-11-08 04:58:39.902143: step 210, duration = 0.648
2017-11-08 04:58:46.139999: step 220, duration = 0.626
2017-11-08 04:58:52.403343: step 230, duration = 0.624
2017-11-08 04:58:58.668950: step 240, duration = 0.626
2017-11-08 04:59:04.947387: step 250, duration = 0.622
2017-11-08 04:59:11.187716: step 260, duration = 0.624
2017-11-08 04:59:17.436893: step 270, duration = 0.626
2017-11-08 04:59:23.723334: step 280, duration = 0.630
2017-11-08 04:59:29.978294: step 290, duration = 0.627
2017-11-08 04:59:36.225820: step 300, duration = 0.623
2017-11-08 04:59:42.513328: step 310, duration = 0.626
2017-11-08 04:59:48.767606: step 320, duration = 0.625
2017-11-08 04:59:55.032640: step 330, duration = 0.623
2017-11-08 05:00:01.334937: step 340, duration = 0.651
2017-11-08 05:00:07.589184: step 350, duration = 0.630
2017-11-08 05:00:13.828363: step 360, duration = 0.624
2017-11-08 05:00:20.115513: step 370, duration = 0.624
2017-11-08 05:00:26.358845: step 380, duration = 0.622
2017-11-08 05:00:32.620887: step 390, duration = 0.627
2017-11-08 05:00:38.866763: step 400, duration = 0.621
2017-11-08 05:00:45.144548: step 410, duration = 0.626
2017-11-08 05:00:51.394449: step 420, duration = 0.626
2017-11-08 05:00:57.653414: step 430, duration = 0.627
2017-11-08 05:01:03.940437: step 440, duration = 0.622
2017-11-08 05:01:10.202802: step 450, duration = 0.623
2017-11-08 05:01:16.458491: step 460, duration = 0.624
2017-11-08 05:01:22.742343: step 470, duration = 0.623
2017-11-08 05:01:29.000450: step 480, duration = 0.629
2017-11-08 05:01:35.260929: step 490, duration = 0.625
2017-11-08 05:01:41.538123: step 500, duration = 0.631
2017-11-08 05:01:47.790096: step 510, duration = 0.623
2017-11-08 05:01:54.036917: step 520, duration = 0.623
2017-11-08 05:02:00.304677: step 530, duration = 0.623
2017-11-08 05:02:06.556361: step 540, duration = 0.625
2017-11-08 05:02:12.813331: step 550, duration = 0.622
2017-11-08 05:02:19.076299: step 560, duration = 0.626
2017-11-08 05:02:25.345473: step 570, duration = 0.628
2017-11-08 05:02:31.604475: step 580, duration = 0.626
2017-11-08 05:02:37.846084: step 590, duration = 0.625
2017-11-08 05:02:44.123450: step 600, duration = 0.625
2017-11-08 05:02:50.378692: step 610, duration = 0.623
2017-11-08 05:02:56.618201: step 620, duration = 0.621
2017-11-08 05:03:02.896440: step 630, duration = 0.624
2017-11-08 05:03:09.145595: step 640, duration = 0.625
2017-11-08 05:03:15.401032: step 650, duration = 0.627
2017-11-08 05:03:21.677424: step 660, duration = 0.623
2017-11-08 05:03:27.926664: step 670, duration = 0.624
2017-11-08 05:03:34.161837: step 680, duration = 0.623
2017-11-08 05:03:40.437444: step 690, duration = 0.623
2017-11-08 05:03:46.701427: step 700, duration = 0.626
2017-11-08 05:03:52.957895: step 710, duration = 0.625
2017-11-08 05:03:59.205796: step 720, duration = 0.629
2017-11-08 05:04:05.501935: step 730, duration = 0.626
2017-11-08 05:04:11.752466: step 740, duration = 0.623
2017-11-08 05:04:18.009826: step 750, duration = 0.622
2017-11-08 05:04:24.278934: step 760, duration = 0.623
2017-11-08 05:04:30.541433: step 770, duration = 0.626
2017-11-08 05:04:36.794119: step 780, duration = 0.629
2017-11-08 05:04:43.077683: step 790, duration = 0.628
2017-11-08 05:04:49.327790: step 800, duration = 0.620
2017-11-08 05:04:55.578353: step 810, duration = 0.621
2017-11-08 05:05:01.846803: step 820, duration = 0.621
2017-11-08 05:05:08.085409: step 830, duration = 0.620
2017-11-08 05:05:14.336388: step 840, duration = 0.630
2017-11-08 05:05:20.616730: step 850, duration = 0.624
2017-11-08 05:05:26.871305: step 860, duration = 0.628
2017-11-08 05:05:33.136749: step 870, duration = 0.624
2017-11-08 05:05:39.424405: step 880, duration = 0.655
2017-11-08 05:05:45.671616: step 890, duration = 0.620
2017-11-08 05:05:51.915767: step 900, duration = 0.621
2017-11-08 05:05:58.171065: step 910, duration = 0.628
2017-11-08 05:06:04.458720: step 920, duration = 0.627
2017-11-08 05:06:10.699536: step 930, duration = 0.628
2017-11-08 05:06:16.949597: step 940, duration = 0.626
2017-11-08 05:06:23.298291: step 950, duration = 0.623
2017-11-08 05:06:29.550959: step 960, duration = 0.627
2017-11-08 05:06:35.808689: step 970, duration = 0.622
2017-11-08 05:06:42.091140: step 980, duration = 0.628
2017-11-08 05:06:48.343217: step 990, duration = 0.626
2017-11-08 05:06:53.981966: across 1000 steps, 0.633 +/- 0.063 sec / batch
```

## 20 layer + 3 fully

distributed

worker 1 gpu
```bash
root@98154222840c:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-08 05:41:20.845480: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 05:41:20.947424: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-08 05:41:20.947944: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-08 05:41:20.947990: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1108 05:41:21.004203723   10877 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-08 05:41:21.008167: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-08 05:41:21.008233: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-08 05:41:21.008772: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 05:41:21.714847: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session d5d0fba7154068d2 with config: 
2017-11-08 05:41:26.404894: step 0, duration = 0.286
2017-11-08 05:41:28.974837: step 10, duration = 0.253
2017-11-08 05:41:31.515500: step 20, duration = 0.248
2017-11-08 05:41:34.000043: step 30, duration = 0.244
2017-11-08 05:41:36.497187: step 40, duration = 0.258
2017-11-08 05:41:39.019646: step 50, duration = 0.245
2017-11-08 05:41:41.509075: step 60, duration = 0.273
2017-11-08 05:41:44.056080: step 70, duration = 0.237
2017-11-08 05:41:46.612570: step 80, duration = 0.270
2017-11-08 05:41:49.110138: step 90, duration = 0.239
2017-11-08 05:41:51.620623: step 100, duration = 0.272
2017-11-08 05:41:55.346532: step 110, duration = 0.468
2017-11-08 05:41:59.170939: step 120, duration = 0.418
2017-11-08 05:42:02.947768: step 130, duration = 0.320
2017-11-08 05:42:06.765406: step 140, duration = 0.347
2017-11-08 05:42:10.481036: step 150, duration = 0.336
2017-11-08 05:42:14.403188: step 160, duration = 0.415
2017-11-08 05:42:18.388425: step 170, duration = 0.467
2017-11-08 05:42:22.089075: step 180, duration = 0.374
2017-11-08 05:42:25.971962: step 190, duration = 0.341
2017-11-08 05:42:29.722370: step 200, duration = 0.370
2017-11-08 05:42:33.636702: step 210, duration = 0.395
2017-11-08 05:42:37.511283: step 220, duration = 0.407
2017-11-08 05:42:41.219153: step 230, duration = 0.371
2017-11-08 05:42:44.875485: step 240, duration = 0.389
2017-11-08 05:42:48.504782: step 250, duration = 0.350
2017-11-08 05:42:52.237782: step 260, duration = 0.387
2017-11-08 05:42:56.076154: step 270, duration = 0.422
2017-11-08 05:42:59.841676: step 280, duration = 0.397
2017-11-08 05:43:03.550529: step 290, duration = 0.453
2017-11-08 05:43:07.216428: step 300, duration = 0.354
2017-11-08 05:43:10.931343: step 310, duration = 0.349
2017-11-08 05:43:14.612676: step 320, duration = 0.330
2017-11-08 05:43:18.420157: step 330, duration = 0.405
2017-11-08 05:43:22.163655: step 340, duration = 0.371
2017-11-08 05:43:26.129535: step 350, duration = 0.431
2017-11-08 05:43:29.949973: step 360, duration = 0.315
2017-11-08 05:43:33.675134: step 370, duration = 0.372
2017-11-08 05:43:37.457332: step 380, duration = 0.388
2017-11-08 05:43:41.277413: step 390, duration = 0.406
2017-11-08 05:43:44.973334: step 400, duration = 0.362
2017-11-08 05:43:48.872610: step 410, duration = 0.343
2017-11-08 05:43:52.588641: step 420, duration = 0.372
2017-11-08 05:43:56.273130: step 430, duration = 0.356
2017-11-08 05:43:59.881595: step 440, duration = 0.340
2017-11-08 05:44:03.819504: step 450, duration = 0.435
2017-11-08 05:44:07.734300: step 460, duration = 0.388
2017-11-08 05:44:11.517790: step 470, duration = 0.347
2017-11-08 05:44:15.424735: step 480, duration = 0.401
2017-11-08 05:44:19.193707: step 490, duration = 0.354
2017-11-08 05:44:23.078690: step 500, duration = 0.438
2017-11-08 05:44:26.846256: step 510, duration = 0.471
2017-11-08 05:44:30.636912: step 520, duration = 0.340
2017-11-08 05:44:34.506461: step 530, duration = 0.368
2017-11-08 05:44:38.271794: step 540, duration = 0.360
2017-11-08 05:44:42.016839: step 550, duration = 0.371
2017-11-08 05:44:45.808461: step 560, duration = 0.362
2017-11-08 05:44:49.611154: step 570, duration = 0.386
2017-11-08 05:44:53.388280: step 580, duration = 0.379
2017-11-08 05:44:57.242930: step 590, duration = 0.426
2017-11-08 05:45:01.031144: step 600, duration = 0.375
2017-11-08 05:45:04.968597: step 610, duration = 0.403
2017-11-08 05:45:08.898797: step 620, duration = 0.413
2017-11-08 05:45:12.706742: step 630, duration = 0.349
2017-11-08 05:45:16.440175: step 640, duration = 0.378
2017-11-08 05:45:20.247892: step 650, duration = 0.407
2017-11-08 05:45:24.016034: step 660, duration = 0.453
2017-11-08 05:45:27.826106: step 670, duration = 0.370
2017-11-08 05:45:31.512442: step 680, duration = 0.342
2017-11-08 05:45:35.242957: step 690, duration = 0.374
2017-11-08 05:45:39.048664: step 700, duration = 0.338
2017-11-08 05:45:42.904484: step 710, duration = 0.344
2017-11-08 05:45:46.908720: step 720, duration = 0.476
2017-11-08 05:45:50.733700: step 730, duration = 0.335
2017-11-08 05:45:54.522383: step 740, duration = 0.312
2017-11-08 05:45:58.300232: step 750, duration = 0.345
2017-11-08 05:46:02.066339: step 760, duration = 0.358
2017-11-08 05:46:05.955309: step 770, duration = 0.451
2017-11-08 05:46:09.880205: step 780, duration = 0.412
2017-11-08 05:46:13.707834: step 790, duration = 0.386
2017-11-08 05:46:17.506492: step 800, duration = 0.347
2017-11-08 05:46:21.353550: step 810, duration = 0.369
2017-11-08 05:46:25.168219: step 820, duration = 0.344
2017-11-08 05:46:29.104145: step 830, duration = 0.509
2017-11-08 05:46:32.802826: step 840, duration = 0.357
2017-11-08 05:46:36.443346: step 850, duration = 0.316
2017-11-08 05:46:40.333483: step 860, duration = 0.392
2017-11-08 05:46:44.089920: step 870, duration = 0.366
2017-11-08 05:46:47.971625: step 880, duration = 0.419
2017-11-08 05:46:51.750744: step 890, duration = 0.358
2017-11-08 05:46:55.470228: step 900, duration = 0.408
2017-11-08 05:46:59.434530: step 910, duration = 0.415
2017-11-08 05:47:03.200643: step 920, duration = 0.393
2017-11-08 05:47:07.026560: step 930, duration = 0.401
2017-11-08 05:47:10.803823: step 940, duration = 0.343
2017-11-08 05:47:14.624214: step 950, duration = 0.357
2017-11-08 05:47:18.413635: step 960, duration = 0.337
2017-11-08 05:47:22.296622: step 970, duration = 0.367
2017-11-08 05:47:26.060354: step 980, duration = 0.389
2017-11-08 05:47:30.044273: step 990, duration = 0.424
2017-11-08 05:47:33.516307: across 1000 steps, 0.371 +/- 0.045 sec / batch
```

worker 2 cpu

```bash
root@610546c83414:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 1 --batch_size 10 --num_batches 1000
2017-11-08 05:40:04.751529: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 05:40:04.754351: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 05:40:04.754408: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 610546c83414
2017-11-08 05:40:04.754435: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 610546c83414
2017-11-08 05:40:04.754492: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 05:40:04.754527: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 05:40:04.754559: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 05:40:04.754576: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 05:40:04.754725441    4553 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 05:40:04.758563: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-08 05:40:04.758628: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> localhost:2222, 2 -> 172.17.0.5:2222}
2017-11-08 05:40:04.759177: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 05:40:12.433014: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 99c32058d2c38326 with config: 
2017-11-08 05:40:52.571638: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:41:02.571797: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:41:12.571951: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:41:21.610635: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session d325dfee59e5fde2 with config: 
2017-11-08 05:41:51.716564: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session ee6313306f5f39bf with config: 
2017-11-08 05:42:26.756544: step 0, duration = 3.168
2017-11-08 05:42:58.982621: step 10, duration = 3.146
2017-11-08 05:43:31.204024: step 20, duration = 3.460
2017-11-08 05:44:03.321456: step 30, duration = 3.274
2017-11-08 05:44:35.262975: step 40, duration = 3.072
2017-11-08 05:45:07.272621: step 50, duration = 3.114
2017-11-08 05:45:39.939896: step 60, duration = 3.273
2017-11-08 05:46:12.472555: step 70, duration = 3.167
2017-11-08 05:46:45.210768: step 80, duration = 3.336
2017-11-08 05:47:17.226209: step 90, duration = 3.109
2017-11-08 05:47:44.384343: step 100, duration = 2.190
2017-11-08 05:48:06.001518: step 110, duration = 2.122
2017-11-08 05:48:27.540640: step 120, duration = 2.119
2017-11-08 05:48:49.020745: step 130, duration = 2.179
2017-11-08 05:49:10.459444: step 140, duration = 2.130
2017-11-08 05:49:31.971594: step 150, duration = 2.194
2017-11-08 05:49:53.384710: step 160, duration = 2.126
2017-11-08 05:50:14.988727: step 170, duration = 2.148
2017-11-08 05:50:36.985451: step 180, duration = 2.168
2017-11-08 05:50:58.461209: step 190, duration = 2.153
2017-11-08 05:51:19.911728: step 200, duration = 2.164
2017-11-08 05:51:41.418206: step 210, duration = 2.140
2017-11-08 05:52:02.880737: step 220, duration = 2.185
2017-11-08 05:52:24.387291: step 230, duration = 2.210
2017-11-08 05:52:46.227413: step 240, duration = 2.226
2017-11-08 05:53:08.227199: step 250, duration = 2.199
2017-11-08 05:53:30.043109: step 260, duration = 2.188
2017-11-08 05:53:51.562211: step 270, duration = 2.211
2017-11-08 05:54:13.543255: step 280, duration = 2.189
2017-11-08 05:54:35.005954: step 290, duration = 2.098
2017-11-08 05:54:56.756869: step 300, duration = 2.176
2017-11-08 05:55:18.557210: step 310, duration = 2.086
2017-11-08 05:55:40.153526: step 320, duration = 2.205
2017-11-08 05:56:01.574199: step 330, duration = 2.177
2017-11-08 05:56:23.036830: step 340, duration = 2.162
2017-11-08 05:56:44.811429: step 350, duration = 2.208
2017-11-08 05:57:06.446747: step 360, duration = 2.268
2017-11-08 05:57:28.341596: step 370, duration = 2.166
2017-11-08 05:57:49.961413: step 380, duration = 2.242
2017-11-08 05:58:11.640422: step 390, duration = 2.144
2017-11-08 05:58:33.381962: step 400, duration = 2.106
2017-11-08 05:58:54.980841: step 410, duration = 2.098
2017-11-08 05:59:16.518159: step 420, duration = 2.125
2017-11-08 05:59:37.922450: step 430, duration = 2.180
2017-11-08 05:59:59.378012: step 440, duration = 2.107
2017-11-08 06:00:20.767224: step 450, duration = 2.122
2017-11-08 06:00:42.351400: step 460, duration = 2.152
2017-11-08 06:01:03.988032: step 470, duration = 2.231
2017-11-08 06:01:25.561678: step 480, duration = 2.280
2017-11-08 06:01:46.979396: step 490, duration = 2.116
2017-11-08 06:02:08.289377: step 500, duration = 2.049
2017-11-08 06:02:30.139224: step 510, duration = 2.127
2017-11-08 06:02:51.777810: step 520, duration = 2.149
2017-11-08 06:03:13.338136: step 530, duration = 2.167
2017-11-08 06:03:35.085321: step 540, duration = 2.177
2017-11-08 06:03:56.585772: step 550, duration = 2.097
2017-11-08 06:04:18.587920: step 560, duration = 2.174
2017-11-08 06:04:40.432106: step 570, duration = 2.196
2017-11-08 06:05:01.866480: step 580, duration = 2.204
2017-11-08 06:05:23.362384: step 590, duration = 2.132
2017-11-08 06:05:44.717368: step 600, duration = 2.156
2017-11-08 06:06:06.292209: step 610, duration = 2.117
2017-11-08 06:06:27.878612: step 620, duration = 2.091
2017-11-08 06:06:49.534677: step 630, duration = 2.213
2017-11-08 06:07:10.955208: step 640, duration = 2.135
2017-11-08 06:07:32.388378: step 650, duration = 2.095
2017-11-08 06:07:53.838106: step 660, duration = 2.160
2017-11-08 06:08:15.195192: step 670, duration = 2.129
2017-11-08 06:08:36.666313: step 680, duration = 2.155
2017-11-08 06:08:58.136201: step 690, duration = 2.151
2017-11-08 06:09:19.766124: step 700, duration = 2.115
2017-11-08 06:09:41.180502: step 710, duration = 2.117
2017-11-08 06:10:02.980137: step 720, duration = 2.230
2017-11-08 06:10:24.729536: step 730, duration = 2.193
2017-11-08 06:10:46.251400: step 740, duration = 2.160
2017-11-08 06:11:07.658229: step 750, duration = 2.098
2017-11-08 06:11:29.122258: step 760, duration = 2.156
2017-11-08 06:11:50.415498: step 770, duration = 2.118
2017-11-08 06:12:12.005468: step 780, duration = 2.142
2017-11-08 06:12:33.567211: step 790, duration = 2.157
2017-11-08 06:12:54.958831: step 800, duration = 2.096
2017-11-08 06:13:16.376908: step 810, duration = 2.255
2017-11-08 06:13:37.808425: step 820, duration = 2.050
2017-11-08 06:13:59.149212: step 830, duration = 2.171
2017-11-08 06:14:20.628363: step 840, duration = 2.268
2017-11-08 06:14:42.204204: step 850, duration = 2.095
2017-11-08 06:15:03.819040: step 860, duration = 2.109
2017-11-08 06:15:25.082572: step 870, duration = 2.101
2017-11-08 06:15:46.863694: step 880, duration = 2.167
2017-11-08 06:16:08.413808: step 890, duration = 2.192
2017-11-08 06:16:30.203013: step 900, duration = 2.152
2017-11-08 06:16:51.432592: step 910, duration = 2.152
2017-11-08 06:17:12.959162: step 920, duration = 2.189
2017-11-08 06:17:34.478484: step 930, duration = 2.138
2017-11-08 06:17:55.965123: step 940, duration = 2.038
2017-11-08 06:18:17.420449: step 950, duration = 2.141
2017-11-08 06:18:38.975964: step 960, duration = 2.204
2017-11-08 06:19:00.564424: step 970, duration = 2.249
2017-11-08 06:19:21.989429: step 980, duration = 2.174
2017-11-08 06:19:43.542284: step 990, duration = 2.208
2017-11-08 06:20:03.003159: across 1000 steps, 2.291 +/- 0.243 sec / batch
```

worker 3 cpu

```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 2 --batch_size 10 --num_batches 1000
2017-11-08 05:40:12.124160: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 05:40:12.127018: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 05:40:12.127074: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-08 05:40:12.127103: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-08 05:40:12.127156: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 05:40:12.127193: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 05:40:12.127226: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 05:40:12.127245: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 05:40:12.127392636   14043 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 05:40:12.131325: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-08 05:40:12.131387: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> localhost:2222}
2017-11-08 05:40:12.131964: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 05:40:22.867998: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:40:32.868180: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:40:42.868347: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:40:52.868527: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:41:02.868712: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:41:12.868889: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 05:41:21.941604: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session f46d14aadfb48734 with config: 
2017-11-08 05:41:52.244113: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session c18c2453823d3b32 with config: 
2017-11-08 05:42:27.606184: step 0, duration = 3.190
2017-11-08 05:42:59.640658: step 10, duration = 3.209
2017-11-08 05:43:31.730879: step 20, duration = 3.035
2017-11-08 05:44:03.939863: step 30, duration = 3.011
2017-11-08 05:44:36.211078: step 40, duration = 3.150
2017-11-08 05:45:08.115498: step 50, duration = 3.222
2017-11-08 05:45:40.005980: step 60, duration = 3.193
2017-11-08 05:46:12.264328: step 70, duration = 3.242
2017-11-08 05:46:44.614067: step 80, duration = 3.251
2017-11-08 05:47:16.450406: step 90, duration = 3.268
2017-11-08 05:47:43.650306: step 100, duration = 2.149
2017-11-08 05:48:05.107493: step 110, duration = 2.152
2017-11-08 05:48:26.680204: step 120, duration = 2.214
2017-11-08 05:48:48.258444: step 130, duration = 2.116
2017-11-08 05:49:09.888150: step 140, duration = 2.157
2017-11-08 05:49:31.403597: step 150, duration = 2.174
2017-11-08 05:49:53.099417: step 160, duration = 2.180
2017-11-08 05:50:15.113533: step 170, duration = 2.205
2017-11-08 05:50:36.863453: step 180, duration = 2.145
2017-11-08 05:50:58.882271: step 190, duration = 2.148
2017-11-08 05:51:20.582461: step 200, duration = 2.213
2017-11-08 05:51:42.123933: step 210, duration = 2.183
2017-11-08 05:52:03.687404: step 220, duration = 2.143
2017-11-08 05:52:25.226838: step 230, duration = 2.069
2017-11-08 05:52:46.519074: step 240, duration = 2.120
2017-11-08 05:53:08.073252: step 250, duration = 2.127
2017-11-08 05:53:29.831679: step 260, duration = 2.192
2017-11-08 05:53:51.623109: step 270, duration = 2.115
2017-11-08 05:54:13.142800: step 280, duration = 2.154
2017-11-08 05:54:34.788701: step 290, duration = 2.189
2017-11-08 05:54:56.637200: step 300, duration = 2.189
2017-11-08 05:55:17.880202: step 310, duration = 2.192
2017-11-08 05:55:39.471459: step 320, duration = 2.199
2017-11-08 05:56:01.011602: step 330, duration = 2.135
2017-11-08 05:56:22.858883: step 340, duration = 2.132
2017-11-08 05:56:44.572571: step 350, duration = 2.174
2017-11-08 05:57:06.447528: step 360, duration = 2.152
2017-11-08 05:57:27.857461: step 370, duration = 2.163
2017-11-08 05:57:49.450202: step 380, duration = 2.128
2017-11-08 05:58:10.794506: step 390, duration = 2.155
2017-11-08 05:58:32.023683: step 400, duration = 2.159
2017-11-08 05:58:53.582441: step 410, duration = 2.205
2017-11-08 05:59:15.042204: step 420, duration = 2.128
2017-11-08 05:59:36.728196: step 430, duration = 2.162
2017-11-08 05:59:58.361483: step 440, duration = 2.141
2017-11-08 06:00:20.121691: step 450, duration = 2.243
2017-11-08 06:00:41.663198: step 460, duration = 2.184
2017-11-08 06:01:03.205387: step 470, duration = 2.085
2017-11-08 06:01:24.690213: step 480, duration = 2.032
2017-11-08 06:01:46.344877: step 490, duration = 2.162
2017-11-08 06:02:08.210422: step 500, duration = 2.259
2017-11-08 06:02:29.944505: step 510, duration = 2.216
2017-11-08 06:02:51.565465: step 520, duration = 2.177
2017-11-08 06:03:13.493927: step 530, duration = 2.169
2017-11-08 06:03:35.304071: step 540, duration = 2.117
2017-11-08 06:03:57.060412: step 550, duration = 2.161
2017-11-08 06:04:18.636937: step 560, duration = 2.198
2017-11-08 06:04:40.530233: step 570, duration = 2.193
2017-11-08 06:05:02.245949: step 580, duration = 2.080
2017-11-08 06:05:23.844664: step 590, duration = 2.183
2017-11-08 06:05:45.584621: step 600, duration = 2.095
2017-11-08 06:06:07.099464: step 610, duration = 2.187
2017-11-08 06:06:28.560438: step 620, duration = 2.219
2017-11-08 06:06:49.917412: step 630, duration = 2.130
2017-11-08 06:07:11.609222: step 640, duration = 2.189
2017-11-08 06:07:33.251463: step 650, duration = 2.255
2017-11-08 06:07:54.876450: step 660, duration = 2.132
2017-11-08 06:08:16.583307: step 670, duration = 2.166
2017-11-08 06:08:38.267694: step 680, duration = 2.125
2017-11-08 06:08:59.882207: step 690, duration = 2.134
2017-11-08 06:09:21.450221: step 700, duration = 2.190
2017-11-08 06:09:43.155801: step 710, duration = 2.214
2017-11-08 06:10:04.820039: step 720, duration = 2.099
2017-11-08 06:10:26.385044: step 730, duration = 2.130
2017-11-08 06:10:47.886203: step 740, duration = 2.165
2017-11-08 06:11:09.602586: step 750, duration = 2.235
2017-11-08 06:11:31.550771: step 760, duration = 2.162
2017-11-08 06:11:53.299665: step 770, duration = 2.165
2017-11-08 06:12:14.700675: step 780, duration = 2.135
2017-11-08 06:12:36.240794: step 790, duration = 2.165
2017-11-08 06:12:57.813201: step 800, duration = 2.124
2017-11-08 06:13:19.519619: step 810, duration = 2.208
2017-11-08 06:13:41.186552: step 820, duration = 2.203
2017-11-08 06:14:02.883421: step 830, duration = 2.134
2017-11-08 06:14:24.479100: step 840, duration = 2.085
2017-11-08 06:14:46.029128: step 850, duration = 2.202
2017-11-08 06:15:07.472714: step 860, duration = 2.136
2017-11-08 06:15:29.235741: step 870, duration = 2.154
2017-11-08 06:15:50.978900: step 880, duration = 2.222
2017-11-08 06:16:12.863239: step 890, duration = 2.150
2017-11-08 06:16:34.638555: step 900, duration = 2.140
2017-11-08 06:16:56.655465: step 910, duration = 2.123
2017-11-08 06:17:18.088204: step 920, duration = 2.068
2017-11-08 06:17:39.567198: step 930, duration = 2.119
2017-11-08 06:18:01.212498: step 940, duration = 2.145
2017-11-08 06:18:22.815202: step 950, duration = 2.151
2017-11-08 06:18:44.359878: step 960, duration = 2.170
2017-11-08 06:19:05.635295: step 970, duration = 2.160
2017-11-08 06:19:27.223514: step 980, duration = 2.102
2017-11-08 06:19:48.647787: step 990, duration = 2.171
2017-11-08 06:20:05.608923: across 1000 steps, 2.293 +/- 0.239 sec / batch
```
single node cpu

```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-08 08:01:07.229839: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 08:01:07.233577: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 08:01:07.233647: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-08 08:01:07.233670: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-08 08:01:07.233726: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 08:01:07.233763: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 08:01:07.233799: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 08:01:07.233820: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 08:01:07.233987452   15603 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 08:01:07.237941: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 08:01:07.238401: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 08:01:07.864994: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 0678fd233ace0fd6 with config: 
2017-11-08 08:01:20.045280: step 0, duration = 1.031
2017-11-08 08:01:30.122087: step 10, duration = 1.009
2017-11-08 08:01:40.238243: step 20, duration = 1.042
2017-11-08 08:01:50.301763: step 30, duration = 1.004
2017-11-08 08:02:00.394787: step 40, duration = 1.008
2017-11-08 08:02:10.471841: step 50, duration = 1.007
2017-11-08 08:02:20.566151: step 60, duration = 1.009
2017-11-08 08:02:30.652791: step 70, duration = 1.010
2017-11-08 08:02:40.753311: step 80, duration = 1.007
2017-11-08 08:02:50.816097: step 90, duration = 1.007
2017-11-08 08:03:00.918179: step 100, duration = 1.011
2017-11-08 08:03:10.992027: step 110, duration = 1.013
2017-11-08 08:03:21.094570: step 120, duration = 1.007
2017-11-08 08:03:31.162590: step 130, duration = 1.009
2017-11-08 08:03:41.272650: step 140, duration = 1.010
2017-11-08 08:03:51.354134: step 150, duration = 1.007
2017-11-08 08:04:01.440954: step 160, duration = 1.004
2017-11-08 08:04:11.526252: step 170, duration = 1.006
2017-11-08 08:04:21.628496: step 180, duration = 1.009
2017-11-08 08:04:31.701703: step 190, duration = 1.004
2017-11-08 08:04:41.820523: step 200, duration = 1.010
2017-11-08 08:04:51.883778: step 210, duration = 1.003
2017-11-08 08:05:01.984041: step 220, duration = 1.002
2017-11-08 08:05:12.060956: step 230, duration = 1.005
2017-11-08 08:05:22.173043: step 240, duration = 1.012
2017-11-08 08:05:32.244326: step 250, duration = 1.011
2017-11-08 08:05:42.334842: step 260, duration = 1.004
2017-11-08 08:05:52.413593: step 270, duration = 1.010
2017-11-08 08:06:02.518601: step 280, duration = 1.009
2017-11-08 08:06:12.589684: step 290, duration = 1.009
2017-11-08 08:06:22.698617: step 300, duration = 1.008
2017-11-08 08:06:32.775773: step 310, duration = 1.008
2017-11-08 08:06:42.883308: step 320, duration = 1.012
2017-11-08 08:06:52.958487: step 330, duration = 1.008
2017-11-08 08:07:03.065811: step 340, duration = 1.008
2017-11-08 08:07:13.138214: step 350, duration = 1.006
2017-11-08 08:07:23.239687: step 360, duration = 1.003
2017-11-08 08:07:33.323976: step 370, duration = 1.010
2017-11-08 08:07:43.434325: step 380, duration = 1.011
2017-11-08 08:07:53.514347: step 390, duration = 1.008
2017-11-08 08:08:03.624526: step 400, duration = 1.007
2017-11-08 08:08:13.682102: step 410, duration = 1.009
2017-11-08 08:08:23.781903: step 420, duration = 1.010
2017-11-08 08:08:33.852666: step 430, duration = 1.006
2017-11-08 08:08:43.963224: step 440, duration = 1.014
2017-11-08 08:08:54.035890: step 450, duration = 1.007
2017-11-08 08:09:04.155372: step 460, duration = 1.006
2017-11-08 08:09:14.227447: step 470, duration = 1.008
2017-11-08 08:09:24.325492: step 480, duration = 1.008
2017-11-08 08:09:34.419390: step 490, duration = 1.004
2017-11-08 08:09:44.512942: step 500, duration = 1.011
2017-11-08 08:09:54.597134: step 510, duration = 1.009
2017-11-08 08:10:04.716330: step 520, duration = 1.000
2017-11-08 08:10:14.798939: step 530, duration = 1.010
2017-11-08 08:10:24.902856: step 540, duration = 1.008
2017-11-08 08:10:34.985973: step 550, duration = 1.007
2017-11-08 08:10:45.083778: step 560, duration = 1.006
2017-11-08 08:10:55.157902: step 570, duration = 1.005
2017-11-08 08:11:05.266648: step 580, duration = 1.005
2017-11-08 08:11:15.445389: step 590, duration = 1.007
2017-11-08 08:11:25.556362: step 600, duration = 1.018
2017-11-08 08:11:35.629136: step 610, duration = 1.006
2017-11-08 08:11:45.837524: step 620, duration = 1.007
2017-11-08 08:11:56.022355: step 630, duration = 1.049
2017-11-08 08:12:06.141564: step 640, duration = 1.011
2017-11-08 08:12:16.226459: step 650, duration = 1.006
2017-11-08 08:12:26.323913: step 660, duration = 1.009
2017-11-08 08:12:36.401077: step 670, duration = 1.003
2017-11-08 08:12:46.520042: step 680, duration = 1.044
2017-11-08 08:12:56.579299: step 690, duration = 1.009
2017-11-08 08:13:06.653412: step 700, duration = 1.007
2017-11-08 08:13:16.695652: step 710, duration = 1.005
2017-11-08 08:13:26.780760: step 720, duration = 1.004
2017-11-08 08:13:36.837649: step 730, duration = 1.002
2017-11-08 08:13:46.995313: step 740, duration = 1.001
2017-11-08 08:13:57.043296: step 750, duration = 1.006
2017-11-08 08:14:07.133540: step 760, duration = 1.003
2017-11-08 08:14:17.189880: step 770, duration = 1.009
2017-11-08 08:14:27.271267: step 780, duration = 1.011
2017-11-08 08:14:37.333569: step 790, duration = 1.008
2017-11-08 08:14:47.442289: step 800, duration = 1.004
2017-11-08 08:14:57.518014: step 810, duration = 1.007
2017-11-08 08:15:07.624553: step 820, duration = 1.008
2017-11-08 08:15:17.694537: step 830, duration = 1.007
2017-11-08 08:15:27.798301: step 840, duration = 1.005
2017-11-08 08:15:37.854264: step 850, duration = 1.004
2017-11-08 08:15:47.913307: step 860, duration = 1.006
2017-11-08 08:15:57.963390: step 870, duration = 1.004
2017-11-08 08:16:08.046696: step 880, duration = 0.999
2017-11-08 08:16:18.103154: step 890, duration = 1.008
2017-11-08 08:16:28.187725: step 900, duration = 1.007
2017-11-08 08:16:38.232489: step 910, duration = 1.000
2017-11-08 08:16:48.322185: step 920, duration = 1.010
2017-11-08 08:16:58.389604: step 930, duration = 1.009
2017-11-08 08:17:08.486578: step 940, duration = 1.002
2017-11-08 08:17:18.549359: step 950, duration = 1.013
2017-11-08 08:17:28.617978: step 960, duration = 1.001
2017-11-08 08:17:38.659185: step 970, duration = 1.007
2017-11-08 08:17:48.737934: step 980, duration = 1.003
2017-11-08 08:17:58.801978: step 990, duration = 1.011
2017-11-08 08:18:07.889808: across 1000 steps, 1.019 +/- 0.101 sec / batch
```

gpu

```bash
root@98154222840c:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000  
2017-11-08 08:22:42.169794: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 08:22:42.272355: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-08 08:22:42.272864: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-08 08:22:42.272909: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1108 08:22:42.328922672   12001 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-08 08:22:42.333069: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 08:22:42.333747: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 08:22:42.975038: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 92084ff3b3e87b76 with config: 
2017-11-08 08:22:45.106942: step 0, duration = 0.051
2017-11-08 08:22:45.621442: step 10, duration = 0.052
2017-11-08 08:22:46.136273: step 20, duration = 0.051
2017-11-08 08:22:46.651325: step 30, duration = 0.052
2017-11-08 08:22:47.167296: step 40, duration = 0.052
2017-11-08 08:22:47.684377: step 50, duration = 0.052
2017-11-08 08:22:48.199452: step 60, duration = 0.052
2017-11-08 08:22:48.715555: step 70, duration = 0.052
2017-11-08 08:22:49.231489: step 80, duration = 0.051
2017-11-08 08:22:49.745849: step 90, duration = 0.051
2017-11-08 08:22:50.261751: step 100, duration = 0.052
2017-11-08 08:22:50.777739: step 110, duration = 0.051
2017-11-08 08:22:51.292806: step 120, duration = 0.051
2017-11-08 08:22:51.808976: step 130, duration = 0.051
2017-11-08 08:22:52.324589: step 140, duration = 0.052
2017-11-08 08:22:52.839547: step 150, duration = 0.051
2017-11-08 08:22:53.354647: step 160, duration = 0.051
2017-11-08 08:22:53.869083: step 170, duration = 0.052
2017-11-08 08:22:54.384582: step 180, duration = 0.051
2017-11-08 08:22:54.899365: step 190, duration = 0.052
2017-11-08 08:22:55.416307: step 200, duration = 0.052
2017-11-08 08:22:55.932724: step 210, duration = 0.052
2017-11-08 08:22:56.447968: step 220, duration = 0.051
2017-11-08 08:22:56.963031: step 230, duration = 0.051
2017-11-08 08:22:57.479537: step 240, duration = 0.052
2017-11-08 08:22:57.994734: step 250, duration = 0.052
2017-11-08 08:22:58.511771: step 260, duration = 0.052
2017-11-08 08:22:59.027057: step 270, duration = 0.052
2017-11-08 08:22:59.543679: step 280, duration = 0.052
2017-11-08 08:23:00.059662: step 290, duration = 0.052
2017-11-08 08:23:00.576132: step 300, duration = 0.052
2017-11-08 08:23:01.092284: step 310, duration = 0.052
2017-11-08 08:23:01.609871: step 320, duration = 0.052
2017-11-08 08:23:02.124670: step 330, duration = 0.051
2017-11-08 08:23:02.639863: step 340, duration = 0.052
2017-11-08 08:23:03.155792: step 350, duration = 0.052
2017-11-08 08:23:03.670440: step 360, duration = 0.051
2017-11-08 08:23:04.186326: step 370, duration = 0.052
2017-11-08 08:23:04.703792: step 380, duration = 0.052
2017-11-08 08:23:05.218165: step 390, duration = 0.052
2017-11-08 08:23:05.731853: step 400, duration = 0.052
2017-11-08 08:23:06.246750: step 410, duration = 0.052
2017-11-08 08:23:06.762797: step 420, duration = 0.052
2017-11-08 08:23:07.276367: step 430, duration = 0.051
2017-11-08 08:23:07.791314: step 440, duration = 0.051
2017-11-08 08:23:08.307660: step 450, duration = 0.052
2017-11-08 08:23:08.823120: step 460, duration = 0.052
2017-11-08 08:23:09.339010: step 470, duration = 0.052
2017-11-08 08:23:09.855927: step 480, duration = 0.052
2017-11-08 08:23:10.372181: step 490, duration = 0.051
2017-11-08 08:23:10.888871: step 500, duration = 0.052
2017-11-08 08:23:11.405527: step 510, duration = 0.052
2017-11-08 08:23:11.920897: step 520, duration = 0.052
2017-11-08 08:23:12.437171: step 530, duration = 0.051
2017-11-08 08:23:12.952242: step 540, duration = 0.051
2017-11-08 08:23:13.469260: step 550, duration = 0.052
2017-11-08 08:23:13.983786: step 560, duration = 0.051
2017-11-08 08:23:14.500685: step 570, duration = 0.052
2017-11-08 08:23:15.015667: step 580, duration = 0.052
2017-11-08 08:23:15.530481: step 590, duration = 0.051
2017-11-08 08:23:16.046380: step 600, duration = 0.052
2017-11-08 08:23:16.562565: step 610, duration = 0.052
2017-11-08 08:23:17.078783: step 620, duration = 0.052
2017-11-08 08:23:17.594503: step 630, duration = 0.052
2017-11-08 08:23:18.109219: step 640, duration = 0.051
2017-11-08 08:23:18.624056: step 650, duration = 0.052
2017-11-08 08:23:19.139862: step 660, duration = 0.052
2017-11-08 08:23:19.656983: step 670, duration = 0.052
2017-11-08 08:23:20.173225: step 680, duration = 0.051
2017-11-08 08:23:20.688259: step 690, duration = 0.051
2017-11-08 08:23:21.203732: step 700, duration = 0.052
2017-11-08 08:23:21.719871: step 710, duration = 0.051
2017-11-08 08:23:22.236237: step 720, duration = 0.052
2017-11-08 08:23:22.752547: step 730, duration = 0.052
2017-11-08 08:23:23.269040: step 740, duration = 0.052
2017-11-08 08:23:23.785041: step 750, duration = 0.052
2017-11-08 08:23:24.301015: step 760, duration = 0.052
2017-11-08 08:23:24.815395: step 770, duration = 0.052
2017-11-08 08:23:25.330125: step 780, duration = 0.052
2017-11-08 08:23:25.846287: step 790, duration = 0.051
2017-11-08 08:23:26.362953: step 800, duration = 0.052
2017-11-08 08:23:26.877267: step 810, duration = 0.051
2017-11-08 08:23:27.392346: step 820, duration = 0.052
2017-11-08 08:23:27.909450: step 830, duration = 0.052
2017-11-08 08:23:28.424568: step 840, duration = 0.052
2017-11-08 08:23:28.939873: step 850, duration = 0.051
2017-11-08 08:23:29.454375: step 860, duration = 0.051
2017-11-08 08:23:29.970810: step 870, duration = 0.052
2017-11-08 08:23:30.487223: step 880, duration = 0.052
2017-11-08 08:23:31.003544: step 890, duration = 0.052
2017-11-08 08:23:31.518972: step 900, duration = 0.051
2017-11-08 08:23:32.035275: step 910, duration = 0.052
2017-11-08 08:23:32.549607: step 920, duration = 0.051
2017-11-08 08:23:33.064863: step 930, duration = 0.052
2017-11-08 08:23:33.580855: step 940, duration = 0.052
2017-11-08 08:23:34.095258: step 950, duration = 0.052
2017-11-08 08:23:34.610488: step 960, duration = 0.052
2017-11-08 08:23:35.125814: step 970, duration = 0.052
2017-11-08 08:23:35.640683: step 980, duration = 0.051
2017-11-08 08:23:36.155500: step 990, duration = 0.052
2017-11-08 08:23:36.618146: across 1000 steps, 0.053 +/- 0.022 sec / batch
```

### 20 layer 10 fully 4094

worker 1
```bash
root@98154222840c:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-08 10:00:38.211211: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 10:00:38.333797: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-08 10:00:38.334271: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-08 10:00:38.334318: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1108 10:00:38.424071062   13584 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-08 10:00:38.428080: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-08 10:00:38.428153: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-08 10:00:38.428565: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 10:00:39.271406: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 3fa29228259cb726 with config: 
2017-11-08 10:01:39.590747: step 0, duration = 4.015
2017-11-08 10:02:22.789143: step 10, duration = 4.511
2017-11-08 10:03:05.069481: step 20, duration = 4.230
2017-11-08 10:03:48.685558: step 30, duration = 4.526
2017-11-08 10:04:32.485115: step 40, duration = 4.214
2017-11-08 10:05:15.506867: step 50, duration = 4.153
2017-11-08 10:05:58.705940: step 60, duration = 4.560
2017-11-08 10:06:42.554400: step 70, duration = 4.658
2017-11-08 10:07:25.707225: step 80, duration = 4.535
2017-11-08 10:08:08.389743: step 90, duration = 4.492
2017-11-08 10:08:51.487999: step 100, duration = 4.210
2017-11-08 10:09:34.410960: step 110, duration = 4.019
2017-11-08 10:10:17.939612: step 120, duration = 4.266
2017-11-08 10:11:05.486422: step 130, duration = 4.566
2017-11-08 10:11:49.543907: step 140, duration = 4.596
2017-11-08 10:12:33.221744: step 150, duration = 4.157
2017-11-08 10:13:16.869924: step 160, duration = 4.173
2017-11-08 10:14:00.422564: step 170, duration = 4.528
2017-11-08 10:14:43.648563: step 180, duration = 4.617
2017-11-08 10:15:26.714895: step 190, duration = 4.232
2017-11-08 10:16:09.529490: step 200, duration = 4.005
2017-11-08 10:16:52.892986: step 210, duration = 4.143
2017-11-08 10:17:35.271679: step 220, duration = 4.407
2017-11-08 10:18:18.371938: step 230, duration = 4.123
2017-11-08 10:19:01.511180: step 240, duration = 4.381
2017-11-08 10:19:45.470715: step 250, duration = 4.105
2017-11-08 10:20:28.756298: step 260, duration = 4.283
2017-11-08 10:21:18.569166: step 270, duration = 4.212
2017-11-08 10:22:01.804251: step 280, duration = 4.303
2017-11-08 10:22:44.311390: step 290, duration = 4.051
2017-11-08 10:23:27.321329: step 300, duration = 4.571
2017-11-08 10:24:10.073156: step 310, duration = 4.132
2017-11-08 10:24:52.507349: step 320, duration = 4.246
2017-11-08 10:25:35.884300: step 330, duration = 4.202
2017-11-08 10:26:19.160586: step 340, duration = 4.184
2017-11-08 10:27:02.185788: step 350, duration = 4.053
2017-11-08 10:27:45.113776: step 360, duration = 4.128
2017-11-08 10:28:27.347150: step 370, duration = 3.929
2017-11-08 10:29:10.920584: step 380, duration = 4.122
2017-11-08 10:29:54.329398: step 390, duration = 4.361
2017-11-08 10:30:37.267869: step 400, duration = 4.341
2017-11-08 10:31:24.645759: step 410, duration = 4.164
2017-11-08 10:32:07.307377: step 420, duration = 3.981
2017-11-08 10:32:49.734530: step 430, duration = 4.010
2017-11-08 10:33:32.917597: step 440, duration = 4.212
2017-11-08 10:34:14.958373: step 450, duration = 4.344
2017-11-08 10:34:57.425481: step 460, duration = 4.393
2017-11-08 10:35:39.758212: step 470, duration = 4.403
2017-11-08 10:36:22.185233: step 480, duration = 4.530
2017-11-08 10:37:04.948709: step 490, duration = 4.409
2017-11-08 10:37:47.812536: step 500, duration = 4.260
2017-11-08 10:38:30.328538: step 510, duration = 4.356
2017-11-08 10:39:13.056725: step 520, duration = 4.311
2017-11-08 10:39:55.992618: step 530, duration = 4.201
2017-11-08 10:40:38.569507: step 540, duration = 4.429
2017-11-08 10:41:25.521451: step 550, duration = 4.241
2017-11-08 10:42:08.396599: step 560, duration = 4.146
2017-11-08 10:42:51.205410: step 570, duration = 4.152
2017-11-08 10:43:33.748523: step 580, duration = 3.853
2017-11-08 10:44:16.330075: step 590, duration = 3.999
2017-11-08 10:44:59.234198: step 600, duration = 4.321
2017-11-08 10:45:41.443627: step 610, duration = 3.900
2017-11-08 10:46:23.814963: step 620, duration = 4.156
2017-11-08 10:47:06.228732: step 630, duration = 4.198
2017-11-08 10:47:48.532663: step 640, duration = 4.347
2017-11-08 10:48:31.060525: step 650, duration = 4.344
2017-11-08 10:49:13.642950: step 660, duration = 4.287
2017-11-08 10:49:56.324446: step 670, duration = 4.228
2017-11-08 10:50:38.297982: step 680, duration = 4.058
2017-11-08 10:51:25.127658: step 690, duration = 4.227
2017-11-08 10:52:07.989251: step 700, duration = 4.261
2017-11-08 10:52:50.950872: step 710, duration = 4.291
2017-11-08 10:53:32.340286: step 720, duration = 4.103
2017-11-08 10:54:14.795821: step 730, duration = 4.234
2017-11-08 10:54:57.962653: step 740, duration = 4.315
2017-11-08 10:55:40.286657: step 750, duration = 4.295
2017-11-08 10:56:21.914879: step 760, duration = 4.140
2017-11-08 10:57:04.286757: step 770, duration = 4.203
2017-11-08 10:57:46.649414: step 780, duration = 4.270
2017-11-08 10:58:29.187249: step 790, duration = 4.184
2017-11-08 10:59:12.487523: step 800, duration = 4.382
2017-11-08 10:59:55.402571: step 810, duration = 4.459
2017-11-08 11:00:38.670713: step 820, duration = 4.430
2017-11-08 11:01:25.812122: step 830, duration = 4.107
2017-11-08 11:02:08.429199: step 840, duration = 4.063
2017-11-08 11:02:52.094145: step 850, duration = 4.408
2017-11-08 11:03:34.686931: step 860, duration = 4.432
2017-11-08 11:04:16.968433: step 870, duration = 4.354
2017-11-08 11:05:00.765281: step 880, duration = 4.613
2017-11-08 11:05:43.377619: step 890, duration = 4.418
2017-11-08 11:06:26.044384: step 900, duration = 4.506
2017-11-08 11:07:08.810282: step 910, duration = 4.284
2017-11-08 11:07:51.069257: step 920, duration = 3.942
2017-11-08 11:08:33.416259: step 930, duration = 4.232
2017-11-08 11:09:15.872618: step 940, duration = 4.154
2017-11-08 11:09:58.181821: step 950, duration = 4.328
2017-11-08 11:10:41.256633: step 960, duration = 4.572
2017-11-08 11:11:30.101793: step 970, duration = 4.262
2017-11-08 11:12:13.248242: step 980, duration = 4.290
2017-11-08 11:12:55.656783: step 990, duration = 4.464
2017-11-08 11:13:34.301154: across 1000 steps, 4.369 +/- 0.201 sec / batch
```

worker 2

```bash
root@610546c83414:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 1 --batch_size 10 --num_batches 1000
2017-11-08 10:00:12.142897: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 10:00:12.146496: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 10:00:12.146556: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 610546c83414
2017-11-08 10:00:12.146579: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 610546c83414
2017-11-08 10:00:12.146634: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 10:00:12.146670: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 10:00:12.146708: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 10:00:12.146726: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 10:00:12.146888366    5615 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 10:00:12.152196: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-08 10:00:12.152292: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> localhost:2222, 2 -> 172.17.0.5:2222}
2017-11-08 10:00:12.152841: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 10:00:22.960123: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:0
2017-11-08 10:00:23.972133: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session f86704c35d111d79 with config: 
2017-11-08 10:00:54.446412: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session 0c608d447ffc64c5 with config: 
2017-11-08 10:02:49.466753: step 0, duration = 10.472
2017-11-08 10:04:33.142812: step 10, duration = 9.993
2017-11-08 10:06:18.096968: step 20, duration = 10.101
2017-11-08 10:08:01.777786: step 30, duration = 11.250
2017-11-08 10:09:46.958970: step 40, duration = 10.394
2017-11-08 10:11:33.066939: step 50, duration = 10.105
2017-11-08 10:13:16.715288: step 60, duration = 9.880
2017-11-08 10:14:59.620441: step 70, duration = 9.927
2017-11-08 10:16:42.953465: step 80, duration = 10.341
2017-11-08 10:18:26.856833: step 90, duration = 10.290
2017-11-08 10:20:06.924621: step 100, duration = 10.313
2017-11-08 10:21:52.602479: step 110, duration = 9.707
2017-11-08 10:23:35.767805: step 120, duration = 10.765
2017-11-08 10:25:21.455474: step 130, duration = 10.117
2017-11-08 10:27:04.084295: step 140, duration = 10.656
2017-11-08 10:28:48.411520: step 150, duration = 10.121
2017-11-08 10:30:32.107223: step 160, duration = 10.100
2017-11-08 10:32:19.945765: step 170, duration = 10.250
2017-11-08 10:34:03.766380: step 180, duration = 10.288
2017-11-08 10:35:46.603308: step 190, duration = 10.395
2017-11-08 10:37:30.939605: step 200, duration = 9.861
2017-11-08 10:39:17.089455: step 210, duration = 10.254
2017-11-08 10:41:01.051017: step 220, duration = 11.615
2017-11-08 10:42:44.365975: step 230, duration = 10.122
2017-11-08 10:44:27.981038: step 240, duration = 10.522
2017-11-08 10:46:13.565803: step 250, duration = 10.459
2017-11-08 10:47:58.917182: step 260, duration = 10.511
2017-11-08 10:49:42.769381: step 270, duration = 10.477
2017-11-08 10:51:28.156560: step 280, duration = 10.491
2017-11-08 10:53:11.755517: step 290, duration = 10.258
2017-11-08 10:54:56.920859: step 300, duration = 10.906
2017-11-08 10:56:44.461688: step 310, duration = 10.239
2017-11-08 10:58:30.442242: step 320, duration = 10.305
2017-11-08 11:00:13.390798: step 330, duration = 10.432
2017-11-08 11:01:58.654622: step 340, duration = 10.502
2017-11-08 11:03:44.087484: step 350, duration = 11.211
2017-11-08 11:05:27.417671: step 360, duration = 10.008
2017-11-08 11:07:09.989627: step 370, duration = 10.283
2017-11-08 11:08:53.905622: step 380, duration = 9.715
2017-11-08 11:10:40.595231: step 390, duration = 10.663
2017-11-08 11:12:27.238339: step 400, duration = 10.493
2017-11-08 11:13:59.769747: step 410, duration = 6.602
2017-11-08 11:15:09.138281: step 420, duration = 7.107
2017-11-08 11:16:18.375907: step 430, duration = 6.720
2017-11-08 11:17:28.970052: step 440, duration = 6.917
2017-11-08 11:18:38.774777: step 450, duration = 6.717
2017-11-08 11:19:48.404480: step 460, duration = 7.153
2017-11-08 11:20:57.163571: step 470, duration = 7.260
2017-11-08 11:22:06.527111: step 480, duration = 7.032
2017-11-08 11:23:15.927485: step 490, duration = 7.167
2017-11-08 11:24:23.902291: step 500, duration = 6.762
2017-11-08 11:25:31.548002: step 510, duration = 6.392
2017-11-08 11:26:40.444224: step 520, duration = 6.768
2017-11-08 11:27:49.386488: step 530, duration = 7.184
2017-11-08 11:28:57.136499: step 540, duration = 6.725
2017-11-08 11:30:06.663231: step 550, duration = 7.259
2017-11-08 11:31:14.498339: step 560, duration = 6.487
2017-11-08 11:32:25.385293: step 570, duration = 6.906
2017-11-08 11:33:36.098333: step 580, duration = 6.748
2017-11-08 11:34:44.442804: step 590, duration = 6.973
2017-11-08 11:35:54.563680: step 600, duration = 7.025
2017-11-08 11:37:05.668916: step 610, duration = 7.408
2017-11-08 11:38:16.382552: step 620, duration = 7.116
2017-11-08 11:39:26.839317: step 630, duration = 6.870
2017-11-08 11:40:35.171640: step 640, duration = 6.671
2017-11-08 11:41:44.346625: step 650, duration = 7.005
2017-11-08 11:42:54.389504: step 660, duration = 7.151
2017-11-08 11:44:04.119468: step 670, duration = 7.277
2017-11-08 11:45:12.729641: step 680, duration = 6.776
2017-11-08 11:46:22.425583: step 690, duration = 7.070
2017-11-08 11:47:31.364479: step 700, duration = 6.940
2017-11-08 11:48:39.473609: step 710, duration = 6.573
2017-11-08 11:49:49.351926: step 720, duration = 6.810
2017-11-08 11:50:59.225087: step 730, duration = 6.678
2017-11-08 11:52:09.608418: step 740, duration = 6.648
2017-11-08 11:53:18.197053: step 750, duration = 7.300
2017-11-08 11:54:27.520726: step 760, duration = 7.247
2017-11-08 11:55:37.315794: step 770, duration = 6.798
2017-11-08 11:56:47.635076: step 780, duration = 7.150
2017-11-08 11:57:59.420253: step 790, duration = 7.356
2017-11-08 11:59:08.385493: step 800, duration = 6.566
2017-11-08 12:00:18.112803: step 810, duration = 6.854
2017-11-08 12:01:27.670761: step 820, duration = 7.404
2017-11-08 12:02:37.784218: step 830, duration = 6.550
2017-11-08 12:03:47.774249: step 840, duration = 7.090
2017-11-08 12:04:57.511322: step 850, duration = 7.000
2017-11-08 12:06:08.447887: step 860, duration = 7.556
2017-11-08 12:07:18.286590: step 870, duration = 6.924
2017-11-08 12:08:28.054817: step 880, duration = 6.667
2017-11-08 12:09:37.070254: step 890, duration = 6.907
2017-11-08 12:10:45.239293: step 900, duration = 7.395
2017-11-08 12:11:56.081457: step 910, duration = 7.182
2017-11-08 12:13:04.621418: step 920, duration = 6.911
2017-11-08 12:14:14.528466: step 930, duration = 7.267
2017-11-08 12:15:23.738811: step 940, duration = 6.842
2017-11-08 12:16:32.168389: step 950, duration = 6.723
2017-11-08 12:17:42.005352: step 960, duration = 6.709
2017-11-08 12:18:50.173450: step 970, duration = 6.784
2017-11-08 12:19:59.448542: step 980, duration = 6.899
2017-11-08 12:21:08.249451: step 990, duration = 7.100
2017-11-08 12:22:11.128975: across 1000 steps, 8.476 +/- 1.551 sec / batch
```

worker 3
```bash
root@5dee89c483b9:~/isc# python3 agoniii.py --ps_host 172.17.0.2:2222 --worker_hosts 172.17.0.3:2222,172.17.0.4:2222,172.17.0.5:2222 --job_name worker --task_index 2 --batch_size 10 --num_batches 1000
2017-11-08 10:00:17.503901: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 10:00:17.507461: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 10:00:17.507537: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-08 10:00:17.507560: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-08 10:00:17.507611: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 10:00:17.507654: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 10:00:17.507700: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 10:00:17.507726: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 10:00:17.507883276   16679 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 10:00:17.511684: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-08 10:00:17.511754: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> 172.17.0.3:2222, 1 -> 172.17.0.4:2222, 2 -> localhost:2222}
2017-11-08 10:00:17.512482: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 10:00:24.346044: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session d9743b9b8a82171f with config: 
2017-11-08 10:00:54.458120: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session f78d19e07c7507d3 with config: 
2017-11-08 10:02:55.434588: step 0, duration = 10.041
2017-11-08 10:04:40.707229: step 10, duration = 11.225
2017-11-08 10:06:26.197297: step 20, duration = 10.140
2017-11-08 10:08:13.630570: step 30, duration = 10.331
2017-11-08 10:09:57.947720: step 40, duration = 10.657
2017-11-08 10:11:44.663236: step 50, duration = 9.863
2017-11-08 10:13:28.764002: step 60, duration = 10.466
2017-11-08 10:15:15.443381: step 70, duration = 11.171
2017-11-08 10:17:02.055937: step 80, duration = 10.938
2017-11-08 10:18:52.127619: step 90, duration = 12.012
2017-11-08 10:20:37.442567: step 100, duration = 9.729
2017-11-08 10:22:28.296259: step 110, duration = 10.515
2017-11-08 10:24:14.024283: step 120, duration = 11.218
2017-11-08 10:25:59.392456: step 130, duration = 10.998
2017-11-08 10:27:44.692242: step 140, duration = 9.899
2017-11-08 10:29:33.817161: step 150, duration = 11.772
2017-11-08 10:31:18.180383: step 160, duration = 11.240
2017-11-08 10:33:03.100552: step 170, duration = 11.044
2017-11-08 10:34:52.281212: step 180, duration = 10.607
2017-11-08 10:36:39.762229: step 190, duration = 10.975
2017-11-08 10:38:25.102322: step 200, duration = 10.336
2017-11-08 10:40:12.909490: step 210, duration = 11.010
2017-11-08 10:41:59.085854: step 220, duration = 10.560
2017-11-08 10:43:45.324417: step 230, duration = 10.797
2017-11-08 10:45:30.518219: step 240, duration = 10.595
2017-11-08 10:47:17.264252: step 250, duration = 10.873
2017-11-08 10:49:02.892651: step 260, duration = 10.427
2017-11-08 10:50:52.104741: step 270, duration = 10.695
2017-11-08 10:52:36.002266: step 280, duration = 9.920
2017-11-08 10:54:25.811684: step 290, duration = 10.309
2017-11-08 10:56:10.656242: step 300, duration = 10.315
2017-11-08 10:57:54.878459: step 310, duration = 10.348
2017-11-08 10:59:39.557259: step 320, duration = 10.492
2017-11-08 11:01:25.987900: step 330, duration = 10.471
2017-11-08 11:03:10.752283: step 340, duration = 10.698
2017-11-08 11:04:54.784845: step 350, duration = 10.759
2017-11-08 11:06:42.404399: step 360, duration = 11.443
2017-11-08 11:08:29.528321: step 370, duration = 11.714
2017-11-08 11:10:15.549286: step 380, duration = 10.282
2017-11-08 11:12:00.421787: step 390, duration = 10.242
2017-11-08 11:13:42.168361: step 400, duration = 7.231
2017-11-08 11:14:53.224617: step 410, duration = 7.290
2017-11-08 11:16:04.792876: step 420, duration = 7.053
2017-11-08 11:17:14.667829: step 430, duration = 6.947
2017-11-08 11:18:25.603979: step 440, duration = 6.769
2017-11-08 11:19:37.352132: step 450, duration = 6.736
2017-11-08 11:20:49.634279: step 460, duration = 6.907
2017-11-08 11:22:00.747170: step 470, duration = 6.948
2017-11-08 11:23:12.522686: step 480, duration = 6.972
2017-11-08 11:24:24.616613: step 490, duration = 7.175
2017-11-08 11:25:36.928725: step 500, duration = 7.382
2017-11-08 11:26:47.616223: step 510, duration = 6.799
2017-11-08 11:27:59.203522: step 520, duration = 7.654
2017-11-08 11:29:10.555253: step 530, duration = 7.041
2017-11-08 11:30:22.059552: step 540, duration = 6.670
2017-11-08 11:31:33.072419: step 550, duration = 7.054
2017-11-08 11:32:43.742012: step 560, duration = 6.966
2017-11-08 11:33:54.032235: step 570, duration = 6.705
2017-11-08 11:35:05.300862: step 580, duration = 7.420
2017-11-08 11:36:16.175075: step 590, duration = 7.162
2017-11-08 11:37:27.022271: step 600, duration = 7.388
2017-11-08 11:38:38.090232: step 610, duration = 7.441
2017-11-08 11:39:49.956501: step 620, duration = 7.254
2017-11-08 11:41:00.317075: step 630, duration = 7.158
2017-11-08 11:42:12.741162: step 640, duration = 7.074
2017-11-08 11:43:22.972294: step 650, duration = 6.928
2017-11-08 11:44:32.337412: step 660, duration = 7.409
2017-11-08 11:45:44.502031: step 670, duration = 6.751
2017-11-08 11:46:55.139209: step 680, duration = 6.778
2017-11-08 11:48:07.430277: step 690, duration = 7.548
2017-11-08 11:49:19.392610: step 700, duration = 6.858
2017-11-08 11:50:30.207673: step 710, duration = 6.933
2017-11-08 11:51:40.728221: step 720, duration = 6.970
2017-11-08 11:52:51.473432: step 730, duration = 7.483
2017-11-08 11:54:02.709933: step 740, duration = 7.005
2017-11-08 11:55:12.207890: step 750, duration = 7.156
2017-11-08 11:56:22.389483: step 760, duration = 7.002
2017-11-08 11:57:34.837262: step 770, duration = 7.835
2017-11-08 11:58:44.398665: step 780, duration = 7.055
2017-11-08 11:59:55.081498: step 790, duration = 7.172
2017-11-08 12:01:06.000753: step 800, duration = 6.972
2017-11-08 12:02:15.757267: step 810, duration = 7.204
2017-11-08 12:03:26.251650: step 820, duration = 7.246
2017-11-08 12:04:36.531843: step 830, duration = 6.909
2017-11-08 12:05:46.661550: step 840, duration = 6.892
2017-11-08 12:06:57.699370: step 850, duration = 6.676
2017-11-08 12:08:08.042304: step 860, duration = 7.236
2017-11-08 12:09:19.031221: step 870, duration = 6.793
2017-11-08 12:10:30.507330: step 880, duration = 6.964
2017-11-08 12:11:40.331480: step 890, duration = 7.286
2017-11-08 12:12:50.008683: step 900, duration = 6.785
2017-11-08 12:14:00.625658: step 910, duration = 7.238
2017-11-08 12:15:12.986399: step 920, duration = 7.223
2017-11-08 12:16:24.429209: step 930, duration = 6.844
2017-11-08 12:17:35.459555: step 940, duration = 7.303
2017-11-08 12:18:48.167417: step 950, duration = 7.201
2017-11-08 12:20:00.540646: step 960, duration = 7.613
2017-11-08 12:21:13.437232: step 970, duration = 7.255
2017-11-08 12:22:19.365197: step 980, duration = 4.403
2017-11-08 12:22:56.966242: step 990, duration = 3.835
2017-11-08 12:23:31.440708: across 1000 steps, 8.557 +/- 1.698 sec / batch
```

cpu
```bash
root@5dee89c483b9:~/isc# tar -cvf alexnet_train_logs_cpu_20_10.tar alexnet_train_logs
alexnet_train_logs/
alexnet_train_logs/graph.pbtxt
alexnet_train_logs/events.out.tfevents.1510128068.5dee89c483b9
alexnet_train_logs/model.ckpt.data-00000-of-00001
alexnet_train_logs/model.ckpt.index
alexnet_train_logs/checkpoint
alexnet_train_logs/model.ckpt.meta
alexnet_train_logs/events.out.tfevents.1510144168.5dee89c483b9
root@5dee89c483b9:~/isc# rm alexnet_train_logs
rm: cannot remove 'alexnet_train_logs': Is a directory
root@5dee89c483b9:~/isc# rm -r alexnet_train_logs
root@5dee89c483b9:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000
2017-11-08 12:32:08.804252: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 12:32:08.807759: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_NO_DEVICE
2017-11-08 12:32:08.807812: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:158] retrieving CUDA diagnostic information for host: 5dee89c483b9
2017-11-08 12:32:08.807835: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:165] hostname: 5dee89c483b9
2017-11-08 12:32:08.807888: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:189] libcuda reported version is: 384.81.0
2017-11-08 12:32:08.807923: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:369] driver version file contents: """NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.81  Sat Sep  2 02:43:11 PDT 2017
GCC version:  gcc version 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC) 
"""
2017-11-08 12:32:08.807959: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:193] kernel reported version is: 384.81.0
2017-11-08 12:32:08.807978: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:300] kernel version seems to match DSO: 384.81.0
E1108 12:32:08.808136986   18205 ev_epoll1_linux.c:1051]     grpc epoll fd: 3
2017-11-08 12:32:08.812426: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 12:32:08.812894: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 12:32:09.620168: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session fcdbd3a621dac086 with config: 
2017-11-08 12:32:45.513850: step 0, duration = 2.546
2017-11-08 12:33:12.584148: step 10, duration = 2.550
2017-11-08 12:33:39.113822: step 20, duration = 2.587
2017-11-08 12:34:05.769478: step 30, duration = 2.755
2017-11-08 12:34:31.825101: step 40, duration = 2.577
2017-11-08 12:34:57.837033: step 50, duration = 2.555
2017-11-08 12:35:23.973976: step 60, duration = 2.765
2017-11-08 12:35:50.517995: step 70, duration = 2.571
2017-11-08 12:36:17.010078: step 80, duration = 2.755
2017-11-08 12:36:43.282545: step 90, duration = 2.565
2017-11-08 12:37:09.817103: step 100, duration = 2.571
2017-11-08 12:37:36.535970: step 110, duration = 2.578
2017-11-08 12:38:02.817672: step 120, duration = 2.566
2017-11-08 12:38:29.148984: step 130, duration = 2.749
2017-11-08 12:38:55.200597: step 140, duration = 2.563
2017-11-08 12:39:21.622861: step 150, duration = 2.776
2017-11-08 12:39:47.827478: step 160, duration = 2.560
2017-11-08 12:40:14.786712: step 170, duration = 2.737
2017-11-08 12:40:41.285160: step 180, duration = 2.741
2017-11-08 12:41:07.687457: step 190, duration = 2.560
2017-11-08 12:41:34.131736: step 200, duration = 2.759
2017-11-08 12:42:00.563925: step 210, duration = 2.582
2017-11-08 12:42:27.602941: step 220, duration = 2.750
2017-11-08 12:42:53.872710: step 230, duration = 2.603
2017-11-08 12:43:20.496791: step 240, duration = 2.586
2017-11-08 12:43:46.933611: step 250, duration = 2.558
2017-11-08 12:44:13.433184: step 260, duration = 2.569
2017-11-08 12:44:39.653457: step 270, duration = 2.599
2017-11-08 12:45:06.259674: step 280, duration = 2.764
2017-11-08 12:45:32.509279: step 290, duration = 2.702
2017-11-08 12:45:59.101661: step 300, duration = 2.688
2017-11-08 12:46:25.299615: step 310, duration = 2.575
2017-11-08 12:46:51.728901: step 320, duration = 2.566
2017-11-08 12:47:18.413817: step 330, duration = 2.576
2017-11-08 12:47:44.900663: step 340, duration = 2.734
2017-11-08 12:48:11.626431: step 350, duration = 2.570
2017-11-08 12:48:37.980064: step 360, duration = 2.727
2017-11-08 12:49:04.328011: step 370, duration = 2.770
2017-11-08 12:49:30.582517: step 380, duration = 2.571
2017-11-08 12:49:56.646429: step 390, duration = 2.571
2017-11-08 12:50:23.229638: step 400, duration = 2.577
2017-11-08 12:50:49.557916: step 410, duration = 2.732
2017-11-08 12:51:15.636768: step 420, duration = 2.539
2017-11-08 12:51:41.949709: step 430, duration = 2.552
2017-11-08 12:52:08.297549: step 440, duration = 2.702
2017-11-08 12:52:35.468079: step 450, duration = 2.589
2017-11-08 12:53:01.412669: step 460, duration = 2.562
2017-11-08 12:53:27.418349: step 470, duration = 2.549
2017-11-08 12:53:53.584529: step 480, duration = 2.551
2017-11-08 12:54:19.860615: step 490, duration = 2.718
2017-11-08 12:54:45.802940: step 500, duration = 2.643
2017-11-08 12:55:11.549658: step 510, duration = 2.540
2017-11-08 12:55:37.560988: step 520, duration = 2.733
2017-11-08 12:56:03.579979: step 530, duration = 2.544
2017-11-08 12:56:29.716737: step 540, duration = 2.532
2017-11-08 12:56:55.867447: step 550, duration = 2.734
2017-11-08 12:57:21.877887: step 560, duration = 2.563
2017-11-08 12:57:48.208814: step 570, duration = 2.729
2017-11-08 12:58:14.307565: step 580, duration = 2.684
2017-11-08 12:58:40.698223: step 590, duration = 2.592
2017-11-08 12:59:07.292254: step 600, duration = 2.733
2017-11-08 12:59:33.389652: step 610, duration = 2.532
2017-11-08 12:59:59.632441: step 620, duration = 2.726
2017-11-08 13:00:25.603029: step 630, duration = 2.548
2017-11-08 13:00:51.769337: step 640, duration = 2.543
2017-11-08 13:01:18.256029: step 650, duration = 2.726
2017-11-08 13:01:44.570424: step 660, duration = 2.540
2017-11-08 13:02:11.010167: step 670, duration = 2.542
2017-11-08 13:02:38.122787: step 680, duration = 2.732
2017-11-08 13:03:04.236999: step 690, duration = 2.544
2017-11-08 13:03:30.363906: step 700, duration = 2.541
2017-11-08 13:03:56.477740: step 710, duration = 2.543
2017-11-08 13:04:22.670954: step 720, duration = 2.541
2017-11-08 13:04:49.033335: step 730, duration = 2.542
2017-11-08 13:05:15.239348: step 740, duration = 2.547
2017-11-08 13:05:41.742994: step 750, duration = 2.606
2017-11-08 13:06:08.237861: step 760, duration = 2.544
2017-11-08 13:06:34.251324: step 770, duration = 2.689
2017-11-08 13:07:00.469958: step 780, duration = 2.570
2017-11-08 13:07:26.281176: step 790, duration = 2.550
2017-11-08 13:07:52.679103: step 800, duration = 2.723
2017-11-08 13:08:18.783294: step 810, duration = 2.533
2017-11-08 13:08:44.990506: step 820, duration = 2.541
2017-11-08 13:09:10.873680: step 830, duration = 2.732
2017-11-08 13:09:37.049789: step 840, duration = 2.549
2017-11-08 13:10:03.292177: step 850, duration = 2.570
2017-11-08 13:10:29.525573: step 860, duration = 2.545
2017-11-08 13:10:55.626079: step 870, duration = 2.536
2017-11-08 13:11:21.935458: step 880, duration = 2.641
2017-11-08 13:11:47.906085: step 890, duration = 2.547
2017-11-08 13:12:13.882342: step 900, duration = 2.535
2017-11-08 13:12:41.054050: step 910, duration = 2.564
2017-11-08 13:13:07.407583: step 920, duration = 2.537
2017-11-08 13:13:33.350138: step 930, duration = 2.702
2017-11-08 13:13:59.527109: step 940, duration = 2.758
2017-11-08 13:14:25.494170: step 950, duration = 2.623
2017-11-08 13:14:51.995607: step 960, duration = 2.726
2017-11-08 13:15:17.828776: step 970, duration = 2.538
2017-11-08 13:15:43.777970: step 980, duration = 2.549
2017-11-08 13:16:09.799437: step 990, duration = 2.541
2017-11-08 13:16:33.399654: across 1000 steps, 2.658 +/- 0.245 sec / batch
```

gpu
```bash
root@98154222840c:~/isc# python3 agoniii.py --worker_hosts localhost:2222 --job_name worker --task_index 0 --batch_size 10 --num_batches 1000  
2017-11-08 13:38:06.162433: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-08 13:38:06.267620: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-08 13:38:06.268111: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 11.09GiB
2017-11-08 13:38:06.268158: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1108 13:38:06.383442922   14679 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-08 13:38:06.388116: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222}
2017-11-08 13:38:06.388581: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
2017-11-08 13:38:07.206486: I tensorflow/core/distributed_runtime/master_session.cc:1004] Start master session ae1e0df50e058d03 with config: 
2017-11-08 13:38:17.956440: step 0, duration = 0.123
2017-11-08 13:38:19.182905: step 10, duration = 0.122
2017-11-08 13:38:20.394976: step 20, duration = 0.121
2017-11-08 13:38:21.611876: step 30, duration = 0.120
2017-11-08 13:38:22.837313: step 40, duration = 0.124
2017-11-08 13:38:24.056406: step 50, duration = 0.122
2017-11-08 13:38:25.274064: step 60, duration = 0.123
2017-11-08 13:38:26.493842: step 70, duration = 0.123
2017-11-08 13:38:27.711857: step 80, duration = 0.122
2017-11-08 13:38:28.941401: step 90, duration = 0.122
2017-11-08 13:38:30.162123: step 100, duration = 0.123
2017-11-08 13:38:31.389432: step 110, duration = 0.122
2017-11-08 13:38:32.616833: step 120, duration = 0.124
2017-11-08 13:38:33.839386: step 130, duration = 0.123
2017-11-08 13:38:35.054765: step 140, duration = 0.120
2017-11-08 13:38:36.275977: step 150, duration = 0.122
2017-11-08 13:38:37.503275: step 160, duration = 0.124
2017-11-08 13:38:38.726066: step 170, duration = 0.122
2017-11-08 13:38:39.951718: step 180, duration = 0.124
2017-11-08 13:38:41.180661: step 190, duration = 0.122
2017-11-08 13:38:42.406443: step 200, duration = 0.122
2017-11-08 13:38:43.622759: step 210, duration = 0.122
2017-11-08 13:38:44.850374: step 220, duration = 0.122
2017-11-08 13:38:46.070679: step 230, duration = 0.120
2017-11-08 13:38:47.291375: step 240, duration = 0.121
2017-11-08 13:38:48.509586: step 250, duration = 0.122
2017-11-08 13:38:49.730242: step 260, duration = 0.124
2017-11-08 13:38:50.945063: step 270, duration = 0.124
2017-11-08 13:38:52.167699: step 280, duration = 0.122
2017-11-08 13:38:53.384779: step 290, duration = 0.122
2017-11-08 13:38:54.605588: step 300, duration = 0.125
2017-11-08 13:38:55.831948: step 310, duration = 0.125
2017-11-08 13:38:57.050838: step 320, duration = 0.124
2017-11-08 13:38:58.269465: step 330, duration = 0.122
2017-11-08 13:38:59.495771: step 340, duration = 0.123
2017-11-08 13:39:00.712047: step 350, duration = 0.122
2017-11-08 13:39:01.931250: step 360, duration = 0.121
2017-11-08 13:39:03.158038: step 370, duration = 0.123
2017-11-08 13:39:04.379712: step 380, duration = 0.123
2017-11-08 13:39:05.602264: step 390, duration = 0.120
2017-11-08 13:39:06.830706: step 400, duration = 0.121
2017-11-08 13:39:08.057116: step 410, duration = 0.121
2017-11-08 13:39:09.288023: step 420, duration = 0.124
2017-11-08 13:39:10.503657: step 430, duration = 0.122
2017-11-08 13:39:11.722860: step 440, duration = 0.122
2017-11-08 13:39:12.941275: step 450, duration = 0.123
2017-11-08 13:39:14.165367: step 460, duration = 0.122
2017-11-08 13:39:15.384629: step 470, duration = 0.121
2017-11-08 13:39:16.603407: step 480, duration = 0.124
2017-11-08 13:39:17.822765: step 490, duration = 0.123
2017-11-08 13:39:19.049736: step 500, duration = 0.124
2017-11-08 13:39:20.270195: step 510, duration = 0.123
2017-11-08 13:39:21.490982: step 520, duration = 0.122
2017-11-08 13:39:22.718552: step 530, duration = 0.123
2017-11-08 13:39:23.939954: step 540, duration = 0.121
2017-11-08 13:39:25.160138: step 550, duration = 0.124
2017-11-08 13:39:26.383873: step 560, duration = 0.121
2017-11-08 13:39:27.604812: step 570, duration = 0.124
2017-11-08 13:39:28.827331: step 580, duration = 0.124
2017-11-08 13:39:30.053281: step 590, duration = 0.121
2017-11-08 13:39:31.282109: step 600, duration = 0.123
2017-11-08 13:39:32.506297: step 610, duration = 0.122
2017-11-08 13:39:33.725805: step 620, duration = 0.121
2017-11-08 13:39:34.950575: step 630, duration = 0.123
2017-11-08 13:39:36.168087: step 640, duration = 0.122
2017-11-08 13:39:37.385547: step 650, duration = 0.123
2017-11-08 13:39:38.604782: step 660, duration = 0.122
2017-11-08 13:39:39.830401: step 670, duration = 0.124
2017-11-08 13:39:41.052217: step 680, duration = 0.124
2017-11-08 13:39:42.273710: step 690, duration = 0.122
2017-11-08 13:39:43.493938: step 700, duration = 0.122
2017-11-08 13:39:44.714119: step 710, duration = 0.120
2017-11-08 13:39:45.931953: step 720, duration = 0.122
2017-11-08 13:39:47.156403: step 730, duration = 0.122
2017-11-08 13:39:48.382394: step 740, duration = 0.123
2017-11-08 13:39:49.608820: step 750, duration = 0.123
2017-11-08 13:39:50.833395: step 760, duration = 0.124
2017-11-08 13:39:52.052451: step 770, duration = 0.125
2017-11-08 13:39:53.269561: step 780, duration = 0.120
2017-11-08 13:39:54.492646: step 790, duration = 0.121
2017-11-08 13:39:55.717639: step 800, duration = 0.125
2017-11-08 13:39:56.938769: step 810, duration = 0.121
2017-11-08 13:39:58.164263: step 820, duration = 0.122
2017-11-08 13:39:59.383825: step 830, duration = 0.123
2017-11-08 13:40:00.606545: step 840, duration = 0.125
2017-11-08 13:40:01.825000: step 850, duration = 0.123
2017-11-08 13:40:03.041414: step 860, duration = 0.123
2017-11-08 13:40:04.268879: step 870, duration = 0.122
2017-11-08 13:40:05.488809: step 880, duration = 0.122
2017-11-08 13:40:06.708833: step 890, duration = 0.124
2017-11-08 13:40:07.929369: step 900, duration = 0.123
2017-11-08 13:40:09.146286: step 910, duration = 0.123
2017-11-08 13:40:10.360532: step 920, duration = 0.120
2017-11-08 13:40:11.575970: step 930, duration = 0.121
2017-11-08 13:40:12.801403: step 940, duration = 0.125
2017-11-08 13:40:14.022830: step 950, duration = 0.122
2017-11-08 13:40:15.243257: step 960, duration = 0.122
2017-11-08 13:40:16.470167: step 970, duration = 0.124
2017-11-08 13:40:17.687466: step 980, duration = 0.121
2017-11-08 13:40:18.917070: step 990, duration = 0.122
2017-11-08 13:40:20.010950: across 1000 steps, 0.128 +/- 0.140 sec / batch
```