from flask import Flask, request
import math

app = Flask(__name__)
template = """
<!DOCTYPE html>
<html><head>
<title>Calculator</title>
</head><body>
    <form name="test" method="get" action="form">
    <p><b>Введите первое число:</b><br>
    <input name="number1" type="number" size="10">
    </p>
    <p><b>Введите второе число:</b><br>
    <input name="number2" type="number" size="10">
    </p>
    <p><b>Ввыберите математическую операцию:</b><br></p>
    <input type="radio" name="operation" value="addition"> Сложение<br>
    <input type="radio" name="operation" value="subtraction"> Вычитание<br>
    <input type="radio" name="operation" value="multiplication"> Умножение<br>
    <input type="radio" name="operation" value="division"> Деление<br>
    <input type="radio" name="operation" value="logarithm"> Логарифм<br>
    <input type="submit" value="Отправить">
</form>
<h1>Результат</h1>
<p>%s</p>
</body>
</html>
"""

@app.route('/')
def hw():
    return template %''

@app.route('/form', methods=['GET'])
def form():
    number1 = int(request.args.get("number1"))
    number2 = int(request.args.get("number2"))
    if request.args.get("operation") == "addition":
        result = number1 + number2
        if number2 < 0:
            line = str(number1) + ' + (' + str(number2) + ') = ' + str(result)
        else:
            line = str(number1) + ' + ' + str(number2) + ' = ' + str(result)
    elif request.args.get("operation") == "subtraction":
        result = number1 - number2
        if number2 < 0:
            line = str(number1) + ' - (' + str(number2) + ') = ' + str(result)
        else:
            line = str(number1) + ' - ' + str(number2) + ' = ' + str(result)
    elif request.args.get("operation") == "multiplication":
        result = number1 * number2
        if number2 < 0:
            line = str(number1) + ' * (' + str(number2) + ') = ' + str(result)
        else:
            line = str(number1) + ' * ' + str(number2) + ' = ' + str(result)
    elif request.args.get("operation") == "division":
        if number2 == 0:
            return template%'Деление на 0 невозможно'
        result = round(number1/ number2, 2)
        if number2 < 0:
            line = str(number1) + ' / (' + str(number2) + ') = ' + str(result)
        else:
            line = str(number1) + ' / ' + str(number2) + ' = ' + str(result)
    else:
        if number1 <= 0:
            return template %'Операцию нельзя провести'
        elif number2 <= 0 or number2 == 1:
            return template %'Операцию нельзя провести'
        result = round(math.log(number1, number2), 5)
        line = 'log' + str(number1) + ' / ' + 'log' + str(number2) + ' = ' + str(result)

    return template %line

if __name__ == "__main__":
    app.run(port=8081, debug=True)
