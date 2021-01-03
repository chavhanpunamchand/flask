from flask_initial_web_service_demo.config import *
from flask import request,render_template

@app.route('/error')
def error():
    return "<p><strong>Enter correct password</strong></p>"


@app.route('/')
def login():
    return render_template("log_in.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == "POST":
        uname = request.form['uname']
        password = request.form['pass']

    if password == "12345":
        resp=make_response(render_template('home.html'))
        resp.set_cookie('uname',uname)

        return resp
    else:
        return redirect(url_for('error'))




app.run(debug=True)


