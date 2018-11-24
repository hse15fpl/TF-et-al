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
<p><b>Введите название операции, которую хотите применить к числам (сложение, вычитание, умножение, деление)</b></p>
<p>P.S. Если название операции ввести неправильно, то результат будет неверным.</p>
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
    if operation == "сложение" or "Сложение":
        result = int(number1)+int(number2)
    if operation == "вычитание" or "Вычитание":
        result = int(number1)-int(number2)
    if operation == "умножение" or "Умножение":
        result = int(number1)*int(number2)
    if operation == "деление" or "Деление":
        result = int(number1)/int(number2)
    return form_template %result

if __name__ == "__main__":
    app.run(port=8081, debug=True)






  

