'''
The url_for() function is used to build a URL to the specific function dynamically.
The first argument is the name of the specified function,
and then we can pass any number of keyword argument corresponding to the variable part of the URL.
This function is useful in the sense that we can avoid hard-coding the URLs into the templates by dynamically building
them using this function.

'''
from flask import  *

app=Flask(__name__)

@app.route('/admin')
def admin():
    return "Admin pages"

@app.route('/lib')
def lib():
    return "librarian pages"

@app.route('/student')
def student():
    return "student pages"

@app.route('/lecture')
def lecture():
    return "lecture pages"

@app.route('/otherStaff')
def otherStaff():
    return "otherStaff pages"

@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))

    if name=='lib':
        return redirect(url_for('lib'))

    if name=='student':
        return redirect(url_for('student'))

    if name == 'lecture':
        return redirect(url_for('lecture'))

    if name == 'otherStaff':
        return redirect(url_for('otherStaff'))


if __name__ == '__main__':
    app.run(debug=True)