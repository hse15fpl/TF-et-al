from flask import Flask, request

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
<td colspan=4 align='right'><input name="button" type="button" value="C" onclick="calc.input.value=''"></td>
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
        
</body>
</html>'''
@app.route('/')
def hw():
    return template

@app.route('/form', methods=['GET'])
def form():
    my_name = request.args.get('name1')
    return template_calc % '2*2'

if __name__ ==  "__main__":
    app.run(port=8081, debug=True)


