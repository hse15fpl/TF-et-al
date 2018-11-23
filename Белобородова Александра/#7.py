from flask import Flask, request

app = Flask(__name__)

    
template = """
<DOCTYPE html>
<html>
<head>
<title>"Калькулятор Оккама" - ничего лишнего!</title>
</head><body>
<form name = "test" method = "get" action="form">
        <table border="0" cellspacing="10" align="center">
        <caption><h3>Ввод выражений</h3></caption><br>
        <tr>
            <td><input name="0" type="button" value = " 0 " onClick="document.test.answer.value+='0'"></td>
            <td><input name="1" type="button" value = " 1 " onClick="document.test.answer.value+='1'"></td>
            <td><input name="2" type="button" value = " 2 " onClick="document.test.answer.value+='2'"></td>
            <td><input name="3" type="button" value = " 3 " onClick="document.test.answer.value+='3'"></td>
            <td><input name="4" type="button" value = " 4 " onClick="document.test.answer.value+='4'"></td><br>
        </tr>
        <tr>
            <td><input name="5" type="button" value = " 5 " onClick="document.test.answer.value+='5'"></td>
            <td><input name="6" type="button" value = " 6 " onClick="document.test.answer.value+='6'"></td>
            <td><input name="7" type="button" value = " 7 " onClick="document.test.answer.value+='7*'"></td>
            <td><input name="8" type="button" value = " 8 " onClick="document.test.answer.value+='8'"></td>
            <td><input name="1" type="button" value = " 9 " onClick="document.test.answer.value+='9'"></td><br>
        </tr>
        <tr>
            <td><input name="plus" type="button" value = " + " onClick="document.test.answer.value+='+'"></td>
            <td><input name="minus" type="button" value = " - " onClick="document.test.answer.value+='-'"></td>
            <td><input name="mult" type="button" value = " * " onClick="document.test.answer.value+='*'"></td>
            <td><input name="div" type="button" value = " / " onClick="document.test.answer.value+='/'"></td>
            <td><input name="res" type="submit" value = " = " answer.value=document.test.answer.value" align="center"></td><br>
        </tr>
    </table>
    <h3 align="center">Выражение: <input name="answer" type="textfield"></h3>
</form>
<h3 align="center">Результат: %s</h3>
</body>
"""




@app.route('/')
def hw():
    return template %'_____'

@app.route('/form', methods=['GET'])

def evaluate():
    ans = eval(request.args.get('answer'))            
    return template %ans

if __name__ == "__main__":
    app.run(debug=True)
