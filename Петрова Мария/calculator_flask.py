from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)
template1 = '''<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Calculator</title>
</head>
<body>
<h1>Hey, do you want me to count something?<h1>
<form>
<p>Tell me the numbers and choose what do you want me to do with them</p>
    <label>First number: <input type="number" method="get" name="first_number"> </label><br>
    <label>Second number: <input type="number" method="get" name="second_number"></label><br>
    <label> <input name="math_function" type="radio" id ="func1" value="add">Add</label><br>
	<label> <input name="math_function" type="radio" id ="func2" value="subtract">Subtract</label><br>
	<label> <input name="math_function" type="radio" id ="func3" value="divide">Divide</label><br>
	<label> <input name="math_function" type="radio" id ="func4" value="mulptiply">Multiply</label><br>
	<input type="submit" value="Get result">
</form>
</body>
</html>'''

template2 = '''<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Calculator</title>
</head>
<body>
<h1>Hey, do you want me to count something?<h1>
<form>
<p>Tell me the numbers and choose what do you want me to do with them</p>
    <label>First number: <input type="number" method="get" name="first_number"> </label><br>
    <label>Second number: <input type="number" method="get" name="second_number"></label><br>
    <label> <input name="math_function" type="radio" id ="func1" value="add">Add</label><br>
	<label> <input name="math_function" type="radio" id ="func2" value="subtract">Subtract</label><br>
	<label> <input name="math_function" type="radio" id ="func3" value="divide">Divide</label><br>
	<label> <input name="math_function" type="radio" id ="func4" value="mulptiply">Multiply</label><br>
	<input type="submit" value="Get result">
</form>
<p>%s</p>
</body>
</html>
'''


def get_answer(first_number,second_number,st_add,st_divide,st_mulptiply,st_subtract): 
	func = request.args.get('math_function')
	first_number = int(first_number)
	second_number = int(second_number)
	if func == 'add':
		result = first_number+second_number
	elif func == 'divide':
		result = first_number//second_number
	elif func == 'subtract':
		result = first_number-second_number
	else:
		result = first_number*second_number
		
	return result

@app.route('/main',methods=['GET'])
def main():
	if request.args:
		first_number = request.args['first_number']
		second_number = request.args['second_number']
		st_add = True if 'add' in request.args else False
		st_subtract = True if 'subtract' in request.args else False
		st_divide = True if 'divide' in request.args else False
		st_mulptiply = True if 'mulptiply' in request.args else False
		
		result = get_answer(first_number,second_number,st_add,st_divide,st_mulptiply,st_subtract)
		return template2 %"Here's you result: "+str(result)
		
	return template1 
	



	
if __name__ == '__main__':
    app.run(port=3030,debug=True)