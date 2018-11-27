from flask import Flask, request

app = Flask(__name__)
template = "%s"
form_template = """
<!DOCTYPE html>
<html>
<head>
<title>Calculator</title>
</head>
<body>
<h1>Калькулятор</h1>
    <form name="test" method="get" action="form">
		<p><b><h3>Введите два числа:</b><br>
		</p>
        <p><b>Число 1:</b><br>
            <input name="number1" type="test" size=40>
        </p>

        <p><b>Число 2:</b><br>
            <input name="number2" type="test" size=40>
        </p>
		<p><b>Выберите знак операции:</b><br>
		</p>
        <p>
        <input type="radio" value="+" name="count"> + <br>
        <input type="radio" value="-" name="count"> - <br>
        <input type="radio" value="*" name="count"> * <br>
        <input type="radio" value=":" name="count"> : <br>
		<input type="radio" value="^" name="count"> ^ <br>
        </p>
        <input type="submit" value="Отправить">
    </form>
<h1>Результат:</h1>
<p>%s</p>
</body>
</html>
"""

@app.route('/')
def hw():
    return form_template %'Hello!'


@app.route('/form', methods=['GET'])
def my_form():
    n1 = int(request.args.get('number1'))
    n2 = int(request.args.get('number2'))
    sign = request.args.get('count')
    def count(n1, n2, sign):
        if sign == "+":
            return n1+n2
        elif sign == '-':
            return n1-n2
        elif sign == "*":
            return n1*n2
        elif sign == ":":
            return n1/n2
        elif sign == "^":
            return pow(n1,n2)
    result = str(count(n1, n2, sign))
    return form_template %result

if __name__ == "__main__":
    app.run(port=8081, debug=True)
