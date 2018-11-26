from flask import Flask, request

app = Flask(__name__)
template = """
<!DOCTYPE html>
<html><head>
<title>Калькулятор</title>
</head><body>
    <form name="test" method="get" action="form">
    <p><b>Что посчитать?</b><br><br>
    <input type="button" onclick="document.getElementById('eq').value+=0" value="0">
    <input type="button" onclick="document.getElementById('eq').value+=1" value="1">
    <input type="button" onclick="document.getElementById('eq').value+=2" value="2">
    <input type="button" onclick="document.getElementById('eq').value+=3" value="3">
    <input type="button" onclick="document.getElementById('eq').value+=4" value="4">
    <input type="button" onclick="document.getElementById('eq').value+=5" value="5">
    <input type="button" onclick="document.getElementById('eq').value+=6" value="6">
    <input type="button" onclick="document.getElementById('eq').value+=7" value="7">
    <input type="button" onclick="document.getElementById('eq').value+=8" value="8">
    <input type="button" onclick="document.getElementById('eq').value+=9" value="9"><br><br>
    <input type="button" onclick="document.getElementById('eq').value+='+'" value="+">
    <input type="button" onclick="document.getElementById('eq').value+='-'" value="-">
    <input type="button" onclick="document.getElementById('eq').value+='*'" value="*">
    <input type="button" onclick="document.getElementById('eq').value+='\'" value="\\">
    <input type="button" onclick="document.getElementById('eq').value+='('" value="(">
    <input type="button" onclick="document.getElementById('eq').value+=')'" value=")"><br><br>
    <input name="equation" id="eq" type="text" size="35">
    </p>
    <input type="submit" value="Вычислить">
    <input type="reset" value="Сбросить">
</form>
<h2>Результат</h2>
<p>%s</p>
</body>
</html>

"""

@app.route('/')
def hw():
    return template %'Я - маленький калькулятор :)'

@app.route('/form', methods=['GET'])
def form():
    equation = request.args.get("equation")
    result = eval(equation)
    return template %result

if __name__ == "__main__":
    app.run(port=8081, debug=True)
