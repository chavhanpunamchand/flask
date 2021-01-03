from FirstApp_Flask.flask_config import app
from flask import request,render_template
from FirstApp_Flask.employeeInfo import Employee



@app.route('/')
def home():
    return render_template('LogIn.html')


@app.route('/index',methods=['POST'])
def index():
    uname=request.form['uname']
    password=request.form['password']
    if uname=="Punamchand" and password=="Punam@123":
        return render_template('index.html',name=uname)
    else:
        return render_template('LogIn.html',msg="Invalid username or password")


@app.route('/registerForm',methods=['GET','POST'])
def resisterForm():
    if request.method=='POST':
        return render_template('registerForm.html')



if __name__ == '__main__':
    app.run(debug=True)







