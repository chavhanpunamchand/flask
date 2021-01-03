from flask import Flask,render_template
app = Flask(__name__)

#app.template_folder = "/pages/"
@app.route("/")
def welcome_page():
    return render_template('abcd.html')

if __name__ == '__main__':
    app.run(debug=True)