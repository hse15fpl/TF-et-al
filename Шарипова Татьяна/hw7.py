from flask import Flask, request 

app = Flask(__name__) 
template = "%f" 
form_template = """ 
<!DOCTYPE html> 
<html> 
<head> 
<title>Calculator</title> 
</head> 
<body> 
<form name="test" method="get" action="form"> 

<p><b>Число 1:</b><br> 
<input name="first_number" type="test" size=40> 
</p>

<p><b>Знак</b><br> 
<input name="sign" type="test" size=40>
</p>

<p><b>Число 2:</b><br> 
<input name="second_number" type="test" size=40> 
</p>

<input type="submit" value="Отправить"> 
</form> 

<h1>Результат:</h1> 
<p>%f</p> 
</body> 
</html> 
""" 

@app.route('/') 
def hw(): 
	return form_template %0

@app.route('/form', methods=['GET']) 
def my_form(): #к одному декоратору крепится только одна функция 
	first = float(request.args.get("first_number"))
	second = float(request.args.get("second_number"))
	sign = request.args.get("sign")
	s = 0
	if sign == "+":
		s = first + second
	elif sign == "-":
		s = first - second
	elif sign == "*":
		s = first * second
	elif sign == "/":
		s = first / second
	return form_template %s

if __name__ == "__main__": 
	app.run(debug=True)
	#app.run(port=8081, debug=True) # по умолчанию запускает localhost:5000 
	# debug отследивает изменения и сам обновляет сервер