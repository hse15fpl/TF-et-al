from flask import Flask, request

app = Flask(__name__)

template = """
<DOCTYPE html>
<html>
<head>
<title>Калькулятор</title>
</head><body background="grey">
<h2 align="center"><font color="green">Онлайн-калькулятор</font></h2>
<i>Данный калькулятор позволит Вам быстро получить правильный ответ, так как в него заложены необходимые математические правила</i>
<form name = "test" method = "get" action="form">
        <br><h3>Введите пример: <input name="answer" type="textfield"></h3>
</form>
<h3>Ответ: %s</h3>
</body>
"""

@app.route('/')
def hw():
    return template %''

@app.route('/form', methods=['GET'])

def evaluate():
    ans = eval(request.args.get('answer'))
    return template %ans

if __name__ == "__main__":
    app.run(debug=True)
