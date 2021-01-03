from flask import *

app=Flask(__name__)

@app.route('/')
def login():
    return render_template('LogIn.html')


@app.route('/user/<uname>')
def welcome(uname):
    return render_template('LogIn.html',name=uname)
if __name__ == '__main__':
    app.run(debug=True)


