from flask_initial_web_service_new.model import *
from flask import render_template,request,session

@app.route('/login/',methods=['GET',"POST"])
def authenticate_user():
    msg = ''
    if request.method == 'POST':
        fuser = request.form['user']
        fpass = request.form['pass']
        login = Login.query.filter(Login.username==fuser,Login.password==fpass).first()
        if login:
            print(login.__dict__)
            session['userinfo'] = login.username
            return render_template('dashboard.html',user=session['userinfo'])
        msg = "Invalid Credentials"

    return render_template('login.html',resp = msg)

@app.route('/home/',methods=['GET'])
def dashboard_page():
    if 'userinfo' in session:
        return render_template('dashboard.html', user=session['userinfo'] )
    return render_template('login.html', resp='')

@app.route('/logout/',methods=['GET'])
def logout():
    if 'userinfo' in session:
        session.pop('userinfo')
    return render_template('login.html', resp='')


if __name__ == '__main__':
    app.run(debug=True)

