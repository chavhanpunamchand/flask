from flask import Flask,render_template
app = Flask(__name__)

@app.route("/sample/")
def say_hi():
    return render_template('sample.html')


if __name__ == '__main__':
    app.run(debug=True)