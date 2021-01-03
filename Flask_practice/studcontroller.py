from Flask_practice.flask_config import app
from flask import render_template

@app.route('/index')
def index():
    msg="Punamchand"
    return render_template("index.html",nmsg=msg)

if __name__ == '__main__':
    app.run(debug=True)