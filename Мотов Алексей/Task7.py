from flask import Flask, request

app = Flask(__name__)
template = """
<DOCTYPE html>
<html>
<head>
<title>Калькулятор</title>
</head>
<body>
<h2 align="center"><font color="blue">Калькулятор</font></h2>
<form name = "test" method = "get" action="form">
        <br><h3>Введите пример: <input name="answer" type="textfield"></h3>
</form>
<h3>Ответ: %s</h3>
</body>
</html>"""

@app.route('/')
def hw():
    return template %''

@app.route('/form', methods=['GET'])

def evaluate():
    ans = eval(request.args.get('answer'))
    return template %ans

if __name__ == "__main__":
    app.run(debug=True)