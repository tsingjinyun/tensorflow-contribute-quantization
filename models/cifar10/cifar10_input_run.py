#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

import cifar10_input

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('data_dir', '/mnt/data2/cifar-10-batches-bin', 'The directory of the CIFAR-10 data')
tf.app.flags.DEFINE_string('batch_size', 128, 'The size of batches')

def main(_):
    print(FLAGS.data_dir)

    images, labels = cifar10_input.inputs(False, data_dir=FLAGS.data_dir, batch_size=FLAGS.batch_size)
    print(images)
    print(labels)

    with tf.Session() as sess:
        res = sess.run([images, labels])
        print(res)
    pass

if __name__ == '__main__':
    tf.app.run()
