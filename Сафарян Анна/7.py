from flask import Flask, request
from math import sqrt, log, pow

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
<title>Строковый калькулятор</title>
</head>
<body>
    <h1 align="center"> Строковый калькулятор к Вашим услугам!</h1>
    
    <center>
    <form name="test" method="get" action="calc">
        <input name="expression" type="text" size="45" placeholder="{}">        
        <input type="submit" value="="> {}
    <p>Введите выражение с клавиатуры или воспользуйтесь кнопками:</p>
        <table border="0" cellspacing="5" align="center">
        <tr>    
            <td><input name="0" type="button" value = "0" onClick="document.test.expression.value+='0'"></td>
            <td><input name="1" type="button" value = "1" onClick="document.test.expression.value+='1'"></td>
            <td><input name="2" type="button" value = "2" onClick="document.test.expression.value+='2'"></td>
            <td><input name="3" type="button" value = "3" onClick="document.test.expression.value+='3'"></td>
            <td><input name="4" type="button" value = "4" onClick="document.test.expression.value+='4'"></td>
            <td><input name="5" type="button" value = "5" onClick="document.test.expression.value+='5'"></td>
            <td><input name="6" type="button" value = "6" onClick="document.test.expression.value+='6'"></td>
            <td><input name="7" type="button" value = "7" onClick="document.test.expression.value+='7'"></td>
            <td><input name="8" type="button" value = "8" onClick="document.test.expression.value+='8'"></td>
            <td><input name="9" type="button" value = "9" onClick="document.test.expression.value+='9'"></td>
        </tr>
        <tr>    
            <td><input name="+" type="button" value = "+" onClick="document.test.expression.value+='+'"></td>
            <td><input name="-" type="button" value = "-" onClick="document.test.expression.value+='-'"></td>
            <td><input name="*" type="button" value = "*" onClick="document.test.expression.value+='*'"></td>
            <td><input name="/" type="button" value = "/" onClick="document.test.expression.value+='/'"></td>
            <td><input name="^" type="button" value = "^" onClick="document.test.expression.value+='pow(,)'"></td>
            <td><input name="√" type="button" value = "√" onClick="document.test.expression.value+='sqrt()'"></td>
            <td><input name="log" type="button" value = "l" onClick="document.test.expression.value+='log(,)'"></td>
            <td><input name="(" type="button" value = "(" onClick="document.test.expression.value+='('"></td>
            <td><input name=")" type="button" value = ")" onClick="document.test.expression.value+=')'"></td>
            <td><input name="." type="button" value = "." onClick="document.test.expression.value+='.'"></td>
        </tr>
        </table>
    </form>
    </center>
    <h3>  Пояснение к кнопкам:</h3>
    <ul>
        <li> ^ возводит в степень. Введите в скобках число и степень через запятую.
        <li> √ вычисляет квадратный корень. Введите число или выражение в скобках.
        <li> l вычисляет логарифм. Введите в скобках число и основание логарифма через запятую.
    </ul>
</body>
</html>
"""


@app.route('/')
def home():
    expression = 'Введите выражение'
    result = ''
    return template.format(expression, result)

@app.route('/calc', methods=['GET'])
def count(): #к одному декоратору крепится только одна функция
    expression = request.args.get('expression')
    result = eval(expression)
    return template.format(expression, result)


if __name__ == "__main__":
    app.run(port=8081, debug=True) # по умолчанию запускает localhost:5000
    # debug отслеживает изменения и сам обновляет сервер
