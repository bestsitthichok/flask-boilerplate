from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "hello my bestfriend"

@app.route('/best')
def new_one_function():
    username = request.args.get('name')
    print(username)
    return 'hi ' + username

@app.route('/sum')
def my_sum():
    a = request.args.get('a')
    a = int(a)
    b = int(request.args.get('b'))
    answer = a + b
    return str(answer)

@app.route('/mybest')
def mybest():
    username = request.args.get('name')
    return  render_template('home.html',name = username)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)