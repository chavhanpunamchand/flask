from flask import *

app = Flask(__name__)


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
        # resp = make_response(render_template('success.html'))
        # resp.set_cookie('uname', uname)
        resp=make_response(render_template('success.html'))
        resp.set_cookie('uname',uname)

        return resp
    else:
        return redirect(url_for('error'))


@app.route('/viewprofile')
def profile():
    uname= request.cookies.get('uname')
    resp = make_response(render_template('profile.html', name=uname))
    return resp


if __name__ == "__main__":
    app.run(debug=True)
