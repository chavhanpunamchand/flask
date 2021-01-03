from flask import Flask

app=Flask(__name__)

@app.route('/home')
def home():
    return "<h1>This is home page</h1>"

@app.route('/home/<name>')
def Home(name):
    return "<h1>Hi</h1>,"+name

@app.route('/index/<int:age>')
def index(age):
    return "your age is: %d"%age


if __name__ == '__main__':
    app.run(debug=True)