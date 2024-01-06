from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(f'The parameter is: {parameter}')
    return parameter

@app.route('/count/<int:parameter>')
def count_parameter(parameter):
    return '\n'.join(map(str, range(parameter)))

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math_operation(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            abort(400, "Invalid operation")
        return str(result)
    except ZeroDivisionError:
        abort(400, "Cannot divide by zero")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
