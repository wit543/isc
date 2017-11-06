```bash
root@98154222840c:~/isc# python3 alexnet.py  --job_name worker --task_index 0
2017-11-06 08:55:14.487736: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
2017-11-06 08:55:14.593120: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-11-06 08:55:14.593446: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties: 
name: Tesla K40c major: 3 minor: 5 memoryClockRate(GHz): 0.745
pciBusID: 0000:01:00.0
totalMemory: 11.17GiB freeMemory: 497.25MiB
2017-11-06 08:55:14.593495: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
E1106 08:55:14.595931841     717 ev_epoll1_linux.c:1051]     grpc epoll fd: 19
2017-11-06 08:55:14.599824: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job ps -> {0 -> 172.17.0.2:2222}
2017-11-06 08:55:14.599887: I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:215] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> 172.17.0.4:2222, 2 -> 172.17.0.5:2222}
2017-11-06 08:55:14.600456: I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:324] Started server with target: grpc://localhost:2222
conv1   [128, 56, 56, 64]
pool1   [128, 27, 27, 64]
conv2   [128, 27, 27, 192]
pool2   [128, 13, 13, 192]
conv3   [128, 13, 13, 384]
conv4   [128, 13, 13, 256]
conv5   [128, 13, 13, 256]
pool5   [128, 6, 6, 256]
2017-11-06 08:55:14.659722: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K40c, pci bus id: 0000:01:00.0, compute capability: 3.5)
2017-11-06 08:55:24.919606: W tensorflow/core/common_runtime/bfc_allocator.cc:273] Allocator (GPU_0_bfc) ran out of memory trying to allocate 74.16MiB.  Current allocation summary follows.
2017-11-06 08:55:24.919712: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (256):   Total Chunks: 4, Chunks in use: 4. 1.0KiB allocated for chunks. 1.0KiB in use in bin. 520B client-requested in use in bin.
2017-11-06 08:55:24.919769: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (512):   Total Chunks: 2, Chunks in use: 2. 1.5KiB allocated for chunks. 1.5KiB in use in bin. 1.5KiB client-requested in use in bin.
2017-11-06 08:55:24.919818: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (1024):  Total Chunks: 7, Chunks in use: 7. 8.5KiB allocated for chunks. 8.5KiB in use in bin. 8.0KiB client-requested in use in bin.
2017-11-06 08:55:24.919900: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (2048):  Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.919962: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (4096):  Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920003: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (8192):  Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920040: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (16384):         Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920080: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (32768):         Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920155: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (65536):         Total Chunks: 1, Chunks in use: 1. 90.8KiB allocated for chunks. 90.8KiB in use in bin. 90.8KiB client-requested in use in bin.
2017-11-06 08:55:24.920201: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (131072):        Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920238: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (262144):        Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920275: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (524288):        Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920315: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (1048576):       Total Chunks: 2, Chunks in use: 1. 2.34MiB allocated for chunks. 1.17MiB in use in bin. 1.17MiB client-requested in use in bin.
2017-11-06 08:55:24.920359: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (2097152):       Total Chunks: 5, Chunks in use: 3. 14.06MiB allocated for chunks. 8.16MiB in use in bin. 8.16MiB client-requested in use in bin.
2017-11-06 08:55:24.920399: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (4194304):       Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920435: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (8388608):       Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920472: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (16777216):      Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920506: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (33554432):      Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920545: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (67108864):      Total Chunks: 3, Chunks in use: 2. 255.74MiB allocated for chunks. 189.32MiB in use in bin. 171.50MiB client-requested in use in bin.
2017-11-06 08:55:24.920584: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (134217728):     Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920623: I tensorflow/core/common_runtime/bfc_allocator.cc:627] Bin (268435456):     Total Chunks: 0, Chunks in use: 0. 0B allocated for chunks. 0B in use in bin. 0B client-requested in use in bin.
2017-11-06 08:55:24.920664: I tensorflow/core/common_runtime/bfc_allocator.cc:643] Bin for 74.16MiB was 64.00MiB, Chunk State: 
2017-11-06 08:55:24.920708: I tensorflow/core/common_runtime/bfc_allocator.cc:649]   Size: 66.42MiB | Requested Size: 0B | in_use: 0, prev:   Size: 3.38MiB | Requested Size: 3.38MiB | in_use: 1, next:   Size: 256B | Requested Size: 256B | in_use: 1
2017-11-06 08:55:24.920744: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a40000 of size 1280
2017-11-06 08:55:24.920773: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a40500 of size 1280
2017-11-06 08:55:24.920801: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a40a00 of size 256
2017-11-06 08:55:24.920827: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a40b00 of size 256
2017-11-06 08:55:24.920853: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a40c00 of size 256
2017-11-06 08:55:24.920879: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a40d00 of size 768
2017-11-06 08:55:24.920905: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a41000 of size 1536
2017-11-06 08:55:24.920931: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a41600 of size 1024
2017-11-06 08:55:24.920961: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a41a00 of size 92928
2017-11-06 08:55:24.920991: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905a58500 of size 2359296
2017-11-06 08:55:24.921020: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905c98500 of size 1228800
2017-11-06 08:55:24.921053: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x905dc4500 of size 2654208
2017-11-06 08:55:24.921086: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90604c500 of size 3538944
2017-11-06 08:55:24.921120: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90a618500 of size 256
2017-11-06 08:55:24.921151: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90a744600 of size 768
2017-11-06 08:55:24.921183: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90a9cc900 of size 1536
2017-11-06 08:55:24.921213: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90ad2cf00 of size 1024
2017-11-06 08:55:24.921243: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90ad2d300 of size 1024
2017-11-06 08:55:24.921275: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90ad2d700 of size 77070336
2017-11-06 08:55:24.921303: I tensorflow/core/common_runtime/bfc_allocator.cc:661] Chunk at 0x90f6ad700 of size 121448704
2017-11-06 08:55:24.921335: I tensorflow/core/common_runtime/bfc_allocator.cc:670] Free at 0x9063ac500 of size 69648384
2017-11-06 08:55:24.921365: I tensorflow/core/common_runtime/bfc_allocator.cc:670] Free at 0x90a618600 of size 1228800
2017-11-06 08:55:24.921395: I tensorflow/core/common_runtime/bfc_allocator.cc:670] Free at 0x90a744900 of size 2654208
2017-11-06 08:55:24.921423: I tensorflow/core/common_runtime/bfc_allocator.cc:670] Free at 0x90a9ccf00 of size 3538944
2017-11-06 08:55:24.921452: I tensorflow/core/common_runtime/bfc_allocator.cc:676]      Summary of in-use Chunks by size: 
2017-11-06 08:55:24.921487: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 4 Chunks of size 256 totalling 1.0KiB
2017-11-06 08:55:24.921519: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 2 Chunks of size 768 totalling 1.5KiB
2017-11-06 08:55:24.921551: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 3 Chunks of size 1024 totalling 3.0KiB
2017-11-06 08:55:24.921583: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 2 Chunks of size 1280 totalling 2.5KiB
2017-11-06 08:55:24.921613: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 2 Chunks of size 1536 totalling 3.0KiB
2017-11-06 08:55:24.921645: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 92928 totalling 90.8KiB
2017-11-06 08:55:24.921678: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 1228800 totalling 1.17MiB
2017-11-06 08:55:24.921711: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 2359296 totalling 2.25MiB
2017-11-06 08:55:24.921743: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 2654208 totalling 2.53MiB
2017-11-06 08:55:24.921771: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 3538944 totalling 3.38MiB
2017-11-06 08:55:24.921799: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 77070336 totalling 73.50MiB
2017-11-06 08:55:24.921828: I tensorflow/core/common_runtime/bfc_allocator.cc:679] 1 Chunks of size 121448704 totalling 115.82MiB
2017-11-06 08:55:24.921856: I tensorflow/core/common_runtime/bfc_allocator.cc:683] Sum Total of in-use chunks: 198.75MiB
2017-11-06 08:55:24.921887: I tensorflow/core/common_runtime/bfc_allocator.cc:685] Stats: 
Limit:                   285474816
InUse:                   208404480
MaxInUse:                208404480
NumAllocs:                      26
MaxAllocSize:            121448704

2017-11-06 08:55:24.921949: W tensorflow/core/common_runtime/bfc_allocator.cc:277] ****_______________________*******************************************************************xxxxxx
2017-11-06 08:55:24.921993: W tensorflow/core/framework/op_kernel.cc:1192] Resource exhausted: OOM when allocating tensor with shape[128,225,225,3]
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 1323, in _do_call
    return fn(*args)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 1302, in _run_fn
    status, run_metadata)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/framework/errors_impl.py", line 473, in __exit__
    c_api.TF_GetCode(self.status.status))
tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[128,225,225,3]
         [[Node: conv1/Conv2D = Conv2D[T=DT_FLOAT, data_format="NHWC", padding="SAME", strides=[1, 4, 4, 1], use_cudnn_on_gpu=true, _device="/job:localhost/replica:0/task:0/device:GPU:0"](Variable/read, conv1/weights/read)]]
         [[Node: pool5/_1 = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_55_pool5", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "alexnet.py", line 288, in <module>
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/platform/app.py", line 48, in run
    _sys.exit(main(_sys.argv[:1] + flags_passthrough))
  File "alexnet.py", line 257, in main
    run_benchmark()
  File "alexnet.py", line 246, in run_benchmark
    time_tensorflow_run(sess, pool5, "Forward")
  File "alexnet.py", line 183, in time_tensorflow_run
    _ = session.run(target)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 889, in run
    run_metadata_ptr)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 1120, in _run
    feed_dict_tensor, options, run_metadata)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 1317, in _do_run
    options, run_metadata)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 1336, in _do_call
    raise type(e)(node_def, op, message)
tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[128,225,225,3]
         [[Node: conv1/Conv2D = Conv2D[T=DT_FLOAT, data_format="NHWC", padding="SAME", strides=[1, 4, 4, 1], use_cudnn_on_gpu=true, _device="/job:localhost/replica:0/task:0/device:GPU:0"](Variable/read, conv1/weights/read)]]
         [[Node: pool5/_1 = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_55_pool5", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]

Caused by op 'conv1/Conv2D', defined at:
  File "alexnet.py", line 288, in <module>
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/platform/app.py", line 48, in run
    _sys.exit(main(_sys.argv[:1] + flags_passthrough))
  File "alexnet.py", line 257, in main
    run_benchmark()
  File "alexnet.py", line 233, in run_benchmark
    pool5, parameters = inference(images)
  File "alexnet.py", line 65, in inference
    conv = tf.nn.conv2d(images, kernel, [1, 4, 4, 1], padding='SAME')
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/ops/gen_nn_ops.py", line 631, in conv2d
    data_format=data_format, name=name)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/framework/op_def_library.py", line 787, in _apply_op_helper
    op_def=op_def)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/framework/ops.py", line 2956, in create_op
    op_def=op_def)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/framework/ops.py", line 1470, in __init__
    self._traceback = self._graph._extract_stack()  # pylint: disable=protected-access

ResourceExhaustedError (see above for traceback): OOM when allocating tensor with shape[128,225,225,3]
         [[Node: conv1/Conv2D = Conv2D[T=DT_FLOAT, data_format="NHWC", padding="SAME", strides=[1, 4, 4, 1], use_cudnn_on_gpu=true, _device="/job:localhost/replica:0/task:0/device:GPU:0"](Variable/read, conv1/weights/read)]]
         [[Node: pool5/_1 = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_55_pool5", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]
```