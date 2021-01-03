from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hi This is index page" \
           "All information available here"


if __name__ == '__main__':
    app.run(debug=True)