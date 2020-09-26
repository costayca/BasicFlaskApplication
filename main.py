from flask import Flask
app = Flask("basic app")

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Index Page'