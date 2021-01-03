from flask import Flask,render_template,request

app = Flask(__name__)


class Book:

    def __init__(self, bkid, bknm, bkauth):
        self.bookId = bkid
        self.bookName = bknm
        self.bookAuthor = bkauth

    def __str__(self):
        return f'''{self.bookId},{self.bookName},{self.bookAuthor}'''

    def __repr__(self):
        return str(self)



#b1 = Book() #--> class la calling
#b1.m1() # method
#m2()    # functional ---> every function is object --> thats why they are saying-- > object callable


num1 = 10
num2 = 20
name = "john"

names = ["abc","pqr","xyz","tts"]
count = 100
def getbook():
    global count
    count = count +1
    return Book(count,f"AAAA{count}",f"XXXX{count}")

booklist = [getbook() for item in range(10)]


@app.route("/index")
def welcome_page():
    result = num1 + num2
    print(len(name))
    val = {1,2,3}
    #return render_template('demo.html', user = None,ans = result,n1 = num1,n2 = num2,bkob = Book(101,"Python","abcd pqrs"))
    return render_template('demo.html', user="abcdefg",
                           value = val,
                           books = booklist,
                           namelist = names)


if __name__ == '__main__':
    app.run(debug=True)