from flask import Flask,render_template
import requests     # virtualenv --> pip install requests
app = Flask(__name__)

@app.route("/register/",methods=["GET","POST"])
def student_regiter():

    return render_template('studinfo.html')


def dummy_api():
    resp = requests.get('https://api.publicapis.org/entries')
    print(resp.json())

def get_list_of_cities():
    resp = requests.get('https://api.iamgds.com/api/CityList')
    print(resp.status_code)
    print(resp.json())

if __name__ == '__main__':
    #app.run(debug=True)
    dummy_api()