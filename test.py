import tensorflow as tf
import numpy as np

tinput = tf.Variable(tf.random.normal([64, 5, 5, 3]))
tfilter = tf.Variable(tf.random.normal([3, 3, 3, 16]))

op_1 = tf.nn.conv2d(tinput, tfilter, strides=[1, 1, 1, 1], padding="SAME")
op_2 = tf.nn.conv2d(tinput, tfilter, strides=[1, 2, 2, 1], padding="SAME")

init = tf.compat.v1.global_variables_initializer()

sess = tf.compat.v1.InteractiveSession()

sess.run(init)

print(np.shape(sess.run(op_1)))
print(np.shape(sess.run(op_2)))
