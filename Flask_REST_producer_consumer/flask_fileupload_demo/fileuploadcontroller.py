from flask import Flask,request,render_template
#from werkzeug import secure_filename
app = Flask(__name__)

@app.route("/index/", methods = ['GET','POST'])
def welcome_page():
    if request.method == 'POST':
        print(request.files)
        print(request.form)
        name = request.form['fname']
        file = request.files['dp']
        file.save(name+".png")

    return render_template('sample.html')

if __name__ == '__main__':
    app.run(debug=True)