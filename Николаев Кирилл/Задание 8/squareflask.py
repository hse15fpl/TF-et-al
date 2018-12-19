from flask import Flask, request
import numpy as np
import tensorflow as tf


app = Flask(__name__)

template1 = """
<!DOCTYPE html>
<html><head>
<title>Парабола на машобуче</title>
</head>
<body>
	<p>Введите x, и наша слишком умная система найдёт y по x**2 + p </p>
	<form name="test" method="get" action="form"
	<p><b>Введите X:</b><br>
		<input name="name1" type="text" size="40">
	</p>
	<input type="submit" value=Посчитать">
</form>
<h1>Ответ:</h1>
<p>%s</p>
</body></html>
"""

template2 = """
<!DOCTYPE html>
<html><head>
<title>СУПЕРМЕГАКАЛЬКУЛЯТОР™!</title>
</head>
<body>
	<p>Введите x, и наша слишком умная система найдёт y по x**2 + p </p>
	<form name="test" method="get" action="form"
	<p><b>Введите X:</b><br>
		<input name="name1" type="text" size="40">
	</p>
	<input type="submit" value="Посчитать">
</form>
<h1>Ответ для числа {0}:</h1>
<p>{1}</p>
</body></html>
"""

@app.route('/')
def hw():
	return template1 %'Пока ответа нет, введите число!'
	
def calculate(x):
    b = tf.Variable(0.42)
    x_plh = tf.placeholder(tf.float32)
    y_hat = tf.add(tf.square(x_plh), b)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, 'models/my_first_model.ckpt')
        y_pred = sess.run([y_hat], feed_dict = {x_plh:x})
    return y_pred[0]

@app.route('/form', methods=['GET'])
def form():
	n = request.args.get('name1')
	answer = calculate(n)
	return template2.format(n, answer)
	
if __name__ == "__main__":
	app.run(port=8081, debug=True)