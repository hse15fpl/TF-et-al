from flask import Flask, request

app = Flask(__name__)
template = "%s"
form_template = """
<!DOCTYPE html>
<html>
<head>
<title>Calculator</title>
</head>
<body>
<h1>Calculator!</h1>
    <form name="test" method="get" action="form">
        <p>Numbers:</p>
        <p><b>1st:</b>
            <input name="number1" type="test" size=4>
        
        <b>2nd:</b>
            <input name="number2" type="test" size=4>
        </p>
        <p>
        <input type="submit" value="+" name="count">  
        <input type="submit" value="-" name="count">
        <input type="submit" value="*" name="count">
        <input type="submit" value="/" name="count">
        <input type="submit" value="**" name="count">
        </p>
    </form>
<h1>Result:</h1>
<p>%s</p>
</body>
</html>
"""

@app.route('/')
def hw():
    return form_template %'Give me some numbers!'
    
@app.route('/form', methods=['GET'])
def calculations(): 
    n1 = int(request.args.get('number1'))
    n2 = int(request.args.get('number2'))
    sign = request.args.get('count')
    def count(n1, n2, sign):
        if sign == "+":
            return n1+n2
        elif sign == '-':
            return n1-n2
        elif sign == "*":
            return n1*n2
        elif (sign == "/" and n2 == 0):
            return "Div. by 0 error!"
        elif sign == "/":
            return n1/n2
        elif sign == "**":
            return n1**n2
        else:
            return "Error!"
    result = str(count(n1, n2, sign))
    return form_template %result

if __name__ == "__main__":
    app.run(port=8000, debug=True)