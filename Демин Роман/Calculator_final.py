__author__ = 'Роман'


from flask import Flask, request

app = Flask(__name__)
template = """
<DOCTYPE html>
<html>
<head>
<title>Калькулятор</title>
</head>
<body>
<h1>Онлайн Калькулятор</h1>
    <form name = "test" method = "get" action="form">
    <p><b>Введите число: </b><br>
        <input name = "digit1" type="test" size="10">
    </p>
    <p><b>Введите число: </b><br>
        <input name = "digit2" type="test" size="10">
    </p>
    <p>
    <input type = "submit" value="+">
    <input type = "submit" value="-">
    </p>
</form>
<h1>Результат: </h1>
<p> %s </p>
</body>
</html>"""

@app.route('/')
def hw():
    return template % 'Hello, world!'

@app.route('/form', methods = ['GET'])
def form():
    digit1 = int(request.args.get('digit1'))
    digit2 = int(request.args.get('digit2'))
    operation = request.args.get('value')
    if operation == '+':
        result = digit1 + digit2
    else:
        result = digit1 - digit2

    return template %result


if __name__ == '__main__':
    app.run(port=8081, debug = True)