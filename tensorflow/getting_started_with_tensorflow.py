import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)

sess = tf.Session()
print(sess.run([node1,node2]))

#node3 = tf.add(node1, node2)
node3 = node1 + node2
print("sess.run(node3) = ", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add_node = a + b # + provides a shortcut for tf.add(a, b)
add_triple_node = add_node * 3
print(sess.run(add_node, {a: 5, b: 6}))
print(sess.run(add_node, {a: [11, 22], b: [33, 44]}))
print(sess.run(add_triple_node, {a: 3, b: 4.5}))

W = tf.Variable([.3], dtype = tf.float32)
b = tf.Variable([-.3], dtype = tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)

init = tf.global_variables_initializer()
sess.run(init)

#print(sess.run(linear_model, {x: [1,2,3,4]}))
#print(sess.run(squared_delta, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

