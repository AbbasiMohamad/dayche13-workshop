from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From Negin!'


@app.route('/bye')
def bye_dayche():
    return 'Bye, From Negin!'
