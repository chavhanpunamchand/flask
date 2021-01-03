from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    return "Hello this is flask first webApp"
    #http://localhost:5000/

str1="A,B,C"

y=list(str1)
print(y)



# if __name__ == '__main__':
#     app.run(debug=True)