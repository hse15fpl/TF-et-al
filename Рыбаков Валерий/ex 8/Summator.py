from flask import Flask, request
import numpy as np
import tensorflow as tf

app = Flask(__name__)
template = """ 
<!DOCTYPE html>
<head>
    <title>Calculator</title>
</head>
<body>
<form name="test" method="get" action="form">
    <p align="center">
    <input name="input" type="text" size="50">
    
    <input style="height:60px;font-size:30px" name="res" type="submit" value = " Ответ ">
    </p>
</form>
<p style="height:60px;font-size:30px" align="center">Ответ: %s</p>
</body>
</html> """

@app.route('/')
def hw():
    return template % 'Введите число'

def calculate(input1, input2):
    a = tf.placeholder(tf.float32)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, 'models/addition')
        result = sess.run(z, feed_dict={a: input1, b:input2})
    return result[0]


@app.route('/form', methods=['GET'])
def result():
    input = request.args.get('input')
    result_val = calculate(input1, input2)

    return  '<p align="center">' + template % result_val + '</p>'

if __name__ == "__main__":
    app.run(port=8081, debug=True)