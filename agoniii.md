

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