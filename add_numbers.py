
# # A function for adding two numbers 

# def add_numbers(num1, num2):
#     """Add two numbers and return the result."""
#     return num1 + num2

from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add_numbers():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None or num2 is None:
        return 'Error: missing argument(s)', 400
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return 'Error: invalid argument(s)', 400
    result = num1 + num2
    return str(result)

if __name__ == '__main__':
    app.run()