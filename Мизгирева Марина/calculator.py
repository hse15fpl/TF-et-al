from flask import Flask, request
app = Flask(__name__)
template = "%s"

form_template = """
<!DOCTYPE html>
<html>
<head>
<title>Hello:)</title>
</head>
<body>
<form name="test" method="get" action="form">
<p><b>Сложение</b></p>
<p><b>Введите два числа:</b></p>
<input name="number1" type="text" size="40"><br>
<br>
<input name="number2" type="text" size="40"><br>
<br>
<p><b>Введите знак операции, которую хотите применить к числам (+, -, *, /)</b></p>
<p>P.S. если знак операции ввести неверно, то программа выдаст ошибочный результат.</p>
<input name="operation" type="text" size="40"><br>
<br>
<input type="submit" value="Отправить"><br>
<br>
</form>
<h1>Результат</h1>
<p>%s</p>
<br>
"""


@app.route('/')
def hw():
    return form_template %'Калькулятор'

@app.route('/form', methods=['GET'])
def summa():
    operation = request.args.get('operation')
    number1 = request.args.get('number1')
    number2 = request.args.get('number2')
    if operation == "+":
        result = int(number1) + int(number2)
    if operation == "-":
        result = int(number1)-int(number2)
    if operation == "*":
        result = int(number1)*int(number2)
    if operation == "/":
        result = int(number1)/int(number2)
    return form_template %result

if __name__ == "__main__":
    app.run(port=8081, debug=True)






  

