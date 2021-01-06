from Login_REST_api.producer.config import *
from Login_REST_api.producer.models import *
from flask import request
import json
from werkzeug.security import generate_password_hash, check_password_hash



ERROR = "ERROR"
SUCCESS = "SUCCESS"


MANDATORY_FIELDS  = ['user','pwd','name']
def check_for_mandatory_fields(reqdata):
    fields = reqdata.keys()
    
    errors = {}
    for field in MANDATORY_FIELDS:
        if field not in fields:
            errors[field] = f"{field} not present"

    return errors



@app.route('/user/new/',methods=["POST"])       # http://localhost:5000/user/new/   post        {user pwd name}
def add_user_credentials():
    returnval = {"error": "User Fields Not present so cannot  add a user..!"}
    reqdata = request.get_json()
    if reqdata:
        errors = check_for_mandatory_fields(reqdata)
        if errors:
            returnval[ERROR] = errors
        else:
            username = reqdata.get("user")
            password = reqdata.get('pwd')
            fullname = reqdata.get('name')
            userob = UserInfo(fullname=fullname,username=username,password=generate_password_hash(password))
            db.session.add(userob)
            db.session.commit()
            return {SUCCESS : "User Added Successfully...!"}
    return returnval

import random
@app.route("/user/token/",methods=["PATCH"])     # http://localhost:5000/user/token/   patch        {user pwd }
def get_user_token():       # either get or create toekn
    reqdata = request.get_json()
    if not reqdata:
        return {ERROR : "Username and Password required.."}
    username = reqdata.get("user")
    password = reqdata.get('pwd')
    userob = UserInfo.query.filter(UserInfo.username == username,UserInfo.active=='Y').first()
    if userob and check_password_hash(userob.password,password):
        if userob.token:
            return {SUCCESS : {username : userob.token}}

        num = random.randint(111111,999999)
        token = username + password + str(num)
        userob.token = generate_password_hash(token)  # encryption
        db.session.commit()
        return {SUCCESS : {username : token}}
    return {ERROR : "Invalid Credentails"}


if __name__ == '__main__':
    # db.create_all()  # to create tables
    app.run(debug=True)  # to start application
