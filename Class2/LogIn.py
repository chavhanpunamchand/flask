from flask import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('LogIn.html')

@app.route('/index',methods=['POST'])
def index():
    uname=request.form['uname']
    password=request.form['password']
    if uname=="Punamchand" and password=="Punam@123":
        return render_template('index.html',uname)
    else:
        return render_template('LogIn',msg="Invalid username or password")


if __name__ == '__main__':
    app.run(debug=True)