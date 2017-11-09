from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from datetime import datetime
import math
import sys
import time

from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

tf.app.flags.DEFINE_string("ps_hosts", "", "Comma-separated list of hostname:port pairs")
tf.app.flags.DEFINE_string("worker_hosts", "", "Comma-separated list of hostname:port pairs")

tf.app.flags.DEFINE_string("job_name", "", "One of 'ps', 'worker'")
tf.app.flags.DEFINE_integer("task_index", 0, "Index of task within the job")
tf.app.flags.DEFINE_integer("batch_size", 100, "Training batch size")
tf.app.flags.DEFINE_integer('num_batches', 100, "Number of batches to run.")

FLAGS = tf.app.flags.FLAGS

slim = tf.contrib.slim
trunc_normal = lambda stddev: tf.truncated_normal_initializer(0, 0, stddev)


def alexnet_v2_arg_scope(weight_decay=0.0005):
    with slim.arg_scope([slim.conv2d, slim.fully_connected],
                        activation_fn=tf.nn.relu,
                        biases_initializer=tf.constant_initializer(0.1),
                        weights_regularizer=slim.l2_regularizer(weight_decay)):
        with slim.arg_scope([slim.conv2d], padding='SAME'):
            with slim.arg_scope([slim.max_pool2d], padding='VALID') as arg_sc:
                return arg_sc


def alexnet_v2(inputs,
               num_classes=1000,
               is_training=True,
               dropout_keep_prob=0.5,
               spatial_squeeze=True,
               scope='alexnet_v2'):
    with tf.variable_scope(scope, 'Variable', [inputs]) as sc:
        end_points_collection = sc.name + '_end_points'
        # Collect outputs for conv2d, fully_connected and max_pool2d.
        with slim.arg_scope([slim.conv2d, slim.fully_connected, slim.max_pool2d],
                            outputs_collections=[end_points_collection]):
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
            net = slim.fully_connected(net, 4096, scope='fc/fc_1')
            net = slim.fully_connected(net, 4096, scope='fc/fc_2')
            net = slim.fully_connected(net, 4096, scope='fc/fc_3')
            net = slim.fully_connected(net, 4096, scope='fc/fc_4')
            net = slim.fully_connected(net, 4096, scope='fc/fc_5')
            net = slim.fully_connected(net, 4096, scope='fc/fc_6')
            net = slim.fully_connected(net, 4096, scope='fc/fc_7')
            net = slim.fully_connected(net, 4096, scope='fc/fc_8')
            net = slim.fully_connected(net, 4096, scope='fc/fc_9')
            net = slim.fully_connected(net, 4096, scope='fc/fc_10')
            net = slim.fully_connected(net, 4096, scope='fc/fc_11')

            # Use conv2d instead of fully_connected layers.
            with slim.arg_scope([slim.conv2d],
                                weights_initializer=trunc_normal(0.005),
                                biases_initializer=tf.constant_initializer(0.1)):
                net = slim.conv2d(net, 4096, [5, 5], padding='VALID',
                                  scope='fc6')
                net = slim.dropout(net, dropout_keep_prob, is_training=is_training,
                                   scope='dropout6')
                net = slim.conv2d(net, 4096, [1, 1], scope='fc7')
                net = slim.dropout(net, dropout_keep_prob, is_training=is_training,
                                   scope='dropout7')
                net = slim.conv2d(net, num_classes, [1, 1],
                                  activation_fn=None,
                                  normalizer_fn=None,
                                  biases_initializer=tf.zeros_initializer,
                                  scope='fc8')

            # Convert end_points_collection into a end_point dict.
            end_points = slim.utils.convert_collection_to_dict(end_points_collection)
            if spatial_squeeze:
                net = tf.squeeze(net, [1, 2], name='fc8/squeezed')
                end_points[sc.name + '/fc8'] = net
            return net, end_points


def main(_):
    # Construct the cluster and start the server
    ps_hosts = FLAGS.ps_hosts.split(",")
    worker_hosts = FLAGS.worker_hosts.split(",")

    cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})

    server = tf.train.Server(cluster, job_name=FLAGS.job_name, task_index=FLAGS.task_index)

    if FLAGS.job_name == "ps":
        server.join()

    elif FLAGS.job_name == "worker":
        with tf.device(tf.train.replica_device_setter(worker_device="/job:worker/task:%d" % FLAGS.task_index,
                                                      cluster=cluster)):

            image_size = 224
            images = tf.Variable(
                tf.random_normal([FLAGS.batch_size, image_size, image_size, 3], dtype=tf.float32, stddev=1e-1))

            with slim.arg_scope(alexnet_v2_arg_scope()):
                logits, end_points = alexnet_v2(images, is_training=False)
            saver = tf.train.Saver()
            summary_op = tf.summary.merge_all()
            # summary_op = tf.summary.merge_all()
            init_op = tf.global_variables_initializer()

        # Create a Supervisor that will checkpoint the model and computes summaries。
        sv = tf.train.Supervisor(is_chief=(FLAGS.task_index == 0), logdir="./alexnet_train_logs", init_op=init_op,
                                 summary_op=summary_op, saver=saver, save_model_secs=600)

        # Get a TensorFlow session managed by the supervisor.
        with sv.managed_session(server.target) as sess:
            num_steps_burn_in = 10
            total_duration = 0.0
            total_duration_squared = 0.0
            for i in xrange(FLAGS.num_batches + num_steps_burn_in):
                start_time = time.time()
                _ = sess.run(logits)
                duration = time.time() - start_time
                if i >= num_steps_burn_in:
                    if not i % 10:
                        print('%s: step %d, duration = %.3f' % (datetime.now(), i - num_steps_burn_in, duration))
                total_duration += duration
                total_duration_squared += duration * duration
            mn = total_duration / FLAGS.num_batches
            vr = total_duration_squared / FLAGS.num_batches - mn * mn
            sd = math.sqrt(abs(vr))
            print('%s: across %d steps, %.3f +/- %.3f sec / batch' % (datetime.now(), FLAGS.num_batches, mn, sd))

        # Stop TensorFlow Session
        sv.stop()


if __name__ == "__main__":
    tf.app.run()
