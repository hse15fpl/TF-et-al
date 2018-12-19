def tf_graph(v):
    #func = re.compile(r'\d+*sqrt\(\d+\)')
    #nums = re.findall(func, v)
    nums = v.split(",")
    if len(nums) > 0:
        n = tf.Variable(nums[0])
        x = nums[1]
        x_plh = tf.placeholder(tf.float32)
        ans = tf.multiply(tf.sqrt(x_plh), n)
        saver = tf.train.Saver()
        with tf.Session() as sess:
            saver.restore(sess, 'models/calc_model.ckpt')
            ans_1 = sess.run([ans], feed_dict = {x_plh:x})
        return template_calc % ans_1[0]

    else:
        return template_calc % "Error! Your function does not match the pattern!"