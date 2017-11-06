import datetime
import alexnet
import tensorflow as tf
BATCH_SIZE = 10
NUM_LABELS = 10
LEARNING_RATE = .02
# input flags
tf.app.flags.DEFINE_string("job_name", "", "Either 'ps' or 'worker'")
tf.app.flags.DEFINE_integer("task_index", 0, "Index of task within the job")
FLAGS = tf.app.flags.FLAGS
ps_hosts = FLAGS.ps_hosts.split(",")
worker_hosts = FLAGS.worker_hosts.split(",")

# Create a cluster from the parameter server and worker hosts.
cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})

# Create and start a server for the local task.
server = tf.train.Server(cluster,
                         job_name=FLAGS.job_name,
                         task_index=FLAGS.task_index)

if FLAGS.job_name == "ps":
    server.join()
elif FLAGS.job_name == "worker":

    gpu = FLAGS.task_index % 4

    # Assigns ops to the local worker by default.
    with tf.device(tf.train.replica_device_setter(
            # '/gpu:%d' % i
            worker_device="/job:worker/task:%d" % FLAGS.task_index,
            # worker_device='/gpu:%d' % gpu,
            cluster=cluster)):

        summary_op = tf.merge_all_summaries()

        y, x = get_graph()

        y_ = tf.placeholder(tf.float32, [None, NUM_LABELS])

        cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

        global_step = tf.Variable(0)

        gradient_descent_opt = tf.train.GradientDescentOptimizer(LEARNING_RATE)

        num_workers = len(worker_hosts)
        sync_rep_opt = tf.train.SyncReplicasOptimizer(gradient_descent_opt, replicas_to_aggregate=num_workers,
                                                      replica_id=FLAGS.task_index, total_num_replicas=num_workers)

        train_op = sync_rep_opt.minimize(cross_entropy, global_step=global_step)

        init_token_op = sync_rep_opt.get_init_tokens_op()
        chief_queue_runner = sync_rep_opt.get_chief_queue_runner()

        # saver = tf.train.Saver()
        summary_op = tf.summary.merge_all()

        init_op = tf.initialize_all_variables()
        saver = tf.train.Saver()

    is_chief = (FLAGS.task_index == 0)

    # Create a "supervisor", which oversees the training process.
    sv = tf.train.Supervisor(is_chief=(FLAGS.task_index == 0),
                             # logdir="/tmp/train_logs",
                             init_op=init_op,
                             summary_op=summary_op,
                             saver=saver,
                             global_step=global_step)
    # save_model_secs=600)

    # The supervisor takes care of session initialization, restoring from
    # a checkpoint, and closing when done or an error occurs.
    with sv.managed_session(server.target) as sess:

        if is_chief:
            sv.start_queue_runners(sess, [chief_queue_runner])
            sess.run(init_token_op)

        num_steps_burn_in = 1000
        total_duration = 0
        total_duration_squared = 0
        step = 0

        while step <= 40000:

            print('Iteration %d' % step)
            tf.sys.stdout.flush()
            batch_xs, batch_ys = get_data(BATCH_SIZE)
            train_feed = {x: batch_xs, y_: batch_ys}

            start_time = datetime.time()

            _, step = sess.run([train_op, global_step], feed_dict=train_feed)

            duration = datetime.time() - start_time
            if step > num_steps_burn_in:
                total_duration += duration
                total_duration_squared += duration * duration

                if not step % 1000:
                    iterations = step - num_steps_burn_in
                    images_processed = BATCH_SIZE * iterations
                    print('%s: step %d, images processed: %d, images per second: %.3f, time taken: %.2f' %
                          (datetime.now(), iterations, images_processed, images_processed / total_duration,
                           total_duration))
                    tf.sys.stdout.flush()
    sv.stop()
