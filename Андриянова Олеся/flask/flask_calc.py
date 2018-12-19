from flask import Flask, request
import tf_graph
import tensorflow as tf
import re
import numpy as np

app = Flask(__name__)

template = '''
<DOCTYPE html> 
<html> 
<head> 
<title>Calculator</title> 
</head>
<body> 
<form action="/form">
<input type="submit" name="go_to_calc" value="Go to Caculator">
</form>
</body>
</html>
'''

template_calc = ''' 
<DOCTYPE html> 
<html> 
<head> 
<title>Calculator</title> 
</head>
<body> 

<style type="text/css">   
   tbody {
   background-color: silver;
   }
   
  </style>

<form name="calc">
<table align="center" border="1">
<thead>
<tr>
<td colspan=4><input name="input" type="text" value="%s"></td>
</tr>
</thead>

<tbody>
<tr>
<td colspan=2 align='right'><input name="button" type="button" value="C" onclick="calc.input.value=''"></td>
<td colspan=2 align='left'><input name="button" type="button" value="Sqrt TF""></td>
</tr>

<tr>
<td><input name="button" type="button" value="7" onclick="calc.input.value+='7'"></td>
<td><input name="button" type="button" value="8" onclick="calc.input.value+='8'"></td>
<td><input name="button" type="button" value="9" onclick="calc.input.value+='9'"></td>
<td><input name="button" type="button" value="&#247;" onclick="calc.input.value+='/'"></td>
</tr>

<tr>
<td><input name="button" type="button" value="4" onclick="calc.input.value+='4'"></td>
<td><input name="button" type="button" value="5" onclick="calc.input.value+='5'"></td>
<td><input  name="button" type="button" value="6" onclick="calc.input.value+='6'"></td>
<td><input name="button" type="button" value="*" onclick="calc.input.value+='*'"></td>
</tr>

<tr>
<td><input  name="button" type="button" value="1" onclick="calc.input.value+='1'"></td>
<td><input  name="button" type="button" value="2" onclick="calc.input.value+='2'"></td>
<td><input  name="button" type="button" value="3" onclick="calc.input.value+='3'"></td>
<td><input  name="button" type="button" value="-" onclick="calc.input.value+='-'"></td>
</tr>

<tr>
<td><input type="button" value="0" onclick="calc.input.value+='0'"></td>
<td><input type="button" value="." onclick="calc.input.value+='.'"></td>
<td><input type="button" value="+" onclick="calc.input.value+='+'"></td>
<td><input type="button" value="=" onclick="calc.input.value=eval(calc.input.value)"></td>
</tr>
</tbody>
</table>
</form>
<p>Try the Sqrt TF function! It will count the square of your input number multiplied to 2.</p>
<p>To try it, just input the equation as follows: <code>TF your_number</code> and press <b>Enter</b>.</p> 
</body>
</html>'''
@app.route('/')
def hw():
    return template

@app.route('/form', methods=['GET'])
def form():
    v = request.args.get('input')
    if "TF" in v:
        nums = v.split(' ')
        n = tf.Variable(np.random.rand())
        x = float(nums[1])
        x_plh = tf.placeholder(tf.float32)
        ans = tf.multiply(tf.sqrt(x_plh), n)
        saver = tf.train.Saver()
        with tf.Session() as sess:
            saver.restore(sess, 'models/calc_graph.ckpt')
            ans_1 = sess.run([ans], feed_dict = {x_plh:x})
        return template_calc % ans_1[0]

    else:
        return template_calc % "2*2"

if __name__ ==  "__main__":
    app.run(port=8081, debug=True)



