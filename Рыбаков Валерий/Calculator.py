from flask import Flask, request

app = Flask(__name__)
template = """ 
<!DOCTYPE html>
<head>
    <title>Calculator</title>
</head>
<body>
<form name="test" method="get" action="form">
    <table border="0" cellspacing="20" align="center">
        <h1 align="center">Калькулятор</h1><br>
        <tr>
            <td><input style="height:60px;width:60px;font-size:30px" name="0" type="button" value = " 0 " onClick="document.test.answer.value+='0'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="1" type="button" value = " 1 " onClick="document.test.answer.value+='1'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="2" type="button" value = " 2 " onClick="document.test.answer.value+='2'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="3" type="button" value = " 3 " onClick="document.test.answer.value+='3'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="4" type="button" value = " 4 " onClick="document.test.answer.value+='4'"></td><br>
        </tr>
        <tr>
            <td><input style="height:60px;width:60px;font-size:30px" name="5" type="button" value = " 5 " onClick="document.test.answer.value+='5'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="6" type="button" value = " 6 " onClick="document.test.answer.value+='6'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="7" type="button" value = " 7 " onClick="document.test.answer.value+='7'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="8" type="button" value = " 8 " onClick="document.test.answer.value+='8'"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="9" type="button" value = " 9 " onClick="document.test.answer.value+='9'"></td><br>
        </tr>
        <tr>
            <td><input style="height:60px;width:60px;font-size:30px" name="plus" type="button" value = " + " onClick="document.test.answer.value+=' + '"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="minus" type="button" value = " - " onClick="document.test.answer.value+=' - '"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="mult" type="button" value = " * " onClick="document.test.answer.value+=' * '"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="div" type="button" value = " / " onClick="document.test.answer.value+=' / '"></td>
            <td><input style="height:60px;width:60px;font-size:30px" name="power" type="button" value = " ^ " onClick="document.test.answer.value+=' ** '"></td>
        </tr>
    </table>
        <p align="center"><input style="height:60px;font-size:30px" name="res" type="submit" value = " Ответ " answer.value="document.test.answer.value"></p>
        <p align="center"><input style="height:60px;font-size:30px; border:none" name="answer" type="textfield"></p>
</form>
<p style="height:60px;font-size:30px" align="center">%s</p>
</body>
</html> """


@app.route('/')
def hw():
    return template % ''

@app.route('/form', methods=['GET'])
def result():
    result_val = eval(request.args.get('answer'))
    return  '<p align="center">' + template % result_val + '</p>'

if __name__ == "__main__":
    app.run(port=8081, debug=True)