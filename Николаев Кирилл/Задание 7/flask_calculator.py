from flask import Flask, request
import calculator

app = Flask(__name__)

template1 = """
<!DOCTYPE html>
<html><head>
<title>СУПЕРМЕГАКАЛЬКУЛЯТОР™!</title>
</head>
<body>
	<p>Добро пожаловать в СУПЕРМЕГАКАЛЬКУЛЯТОР™ (СМК)!</p>
	<p>СМК умеет парсить строку, в том числе скобки :)</p>
	<p>Возможные действия: +, -, *, /, ^ (возведение в степень), v (извлечение квадратного корня). Для десятичных, пожалуйста, используйте точку. (.)</p>
	<p>Пы.Сы. При извлечении корня из отрицательных чисел, они сначала преобразуются в положительные.</p>
	<form name="test" method="get" action="form"
	<p><b>Введите выражение:</b><br>
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
	<p>Добро пожаловать в СУМЕРМЕГАКАЛЬКУЛЯТОР™ (СМК)!</p>
	<p>СМК умеет парсить строку, в том числе скобки :)</p>
	<p>Возможные действия: +, -, *, /, ^ (возведение в степень), v (извлечение квадратного корня). Для десятичных, пожалуйста, используйте точку. (.)</p>
	<p>Пы.Сы. При извлечении корня из отрицательных чисел, они сначала преобразуются в положительные.</p>
	<form name="test" method="get" action="form"
	<p><b>Введите выражение:</b><br>
		<input name="name1" type="text" size="40">
	</p>
	<input type="submit" value="Посчитать">
</form>
<h1>Ответ для выражения {0}:</h1>
<p>{1}</p>
</body></html>
"""

@app.route('/')
def hw():
	return template1 %'Пока ответа нет, введите выражение!'

@app.route('/form', methods=['GET'])
def form():
	n = request.args.get('name1')
	answer = calculator.calculate(n)
	return template2.format(n, answer)
	
if __name__ == "__main__":
	app.run(port=8081, debug=True)