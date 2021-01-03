from simple_flask_rest_api.product_api.dbconfig import app,db,Product,UserInfo
# another application which might be running using python/java/.net php --> going to request to this application
#MVC --> HTTP METHOD TYPES --> MVC --> REQUEST --> BROWSER --> GET -- POST -->
#REST --> HTTP METHOD TYPES -> RESTAPI --> REQUEST --> ANOTHER APPLICATION CAN BE RUNNING - ON DIFF PLATFORM OR USING DIFF LANG -->
        # METHOD TYPES --> get post put delete          patch delete head option
# get --> to retrive                    head
        # req -no body: retrive         resp - no body --  ack

# post --> to create
# delete --> to remove
# put   --> to modify       --> patch --> to modify partial object contents

#options --> server capabilities..
                                                    # http://localhost:5000     -->     /product/       --> post --
from flask import request
import json

MANDATORY_FIELDS  = ['product_name','product_vendor','product_price','product_qty']

def check_for_mandatory_fields(reqdata):
    fields = reqdata.keys()
    errors = {}
    for field in MANDATORY_FIELDS:
        if field not in fields:
            errors[field] = f"{field} not present"

    return errors

ERROR = "ERROR"
SUCCESS = "SUCCESS"

def serialize_product(prod):
    return {"PRODUCT_ID": prod.id,
                 "PRODUCT_NAME": prod.name,
                 "PRODUCT_QUANTITY": prod.qty,
                 "PRODUCT_PRICE": prod.price,
                 "PRODUCT_VENDOR": prod.vendor}


@app.route('/product/',methods=['POST'])        #http://localhost:5000/product/     post        --> request body
def add_product():
    returnval = {"error" : "Product Fields Not present so cannot  add a Product..!"}
    reqdata = request.get_json()          # yenar data --> serialized -               --> browser --> request.form
    if reqdata:
        errors = check_for_mandatory_fields(reqdata)
        if errors:
            returnval[ERROR] = errors
        else:
            prod = Product.query.filter(Product.name == reqdata.get('product_name')).first()
            if prod:
                returnval[ERROR]="Duplicate Product Name "
            else:
                prod = Product(name=reqdata.get('product_name'),
                               vendor=reqdata.get('product_vendor'),
                               price=reqdata.get('product_price'),
                               qty=reqdata.get('product_qty'))
                db.session.add(prod)
                db.session.commit()
                returnval = {SUCCESS : "Product ({}) Added Successfully...!".format(prod.id)}

    return returnval


@app.route('/product/<int:pid>',methods=['DELETE'])      #http://localhost:5000/product/{}     delete
def delete_product(pid):
    prod = Product.query.filter_by(id=pid).first()
    if prod:
        db.session.delete(prod)
        db.session.commit()
        return {SUCCESS : "Product {} removed Successfully...!".format(pid)}
    return {ERROR : "Product with given id={} Not found!".format(pid)}

@app.route('/product/<int:pid>',methods=['PUT'])          #http://localhost:5000/product/     put       --> req uri-id + req body
def update_product(pid):
    returnval = {ERROR: F"Product WITH GIVEN ID {pid} NOT PRESENT .!"}
    prod = Product.query.filter_by(id=pid).first()
    if prod:
        returnval = {ERROR: "Product Fields Not present so cannot  add a Product..!"}
        reqdata = request.get_json()  # yenar data --> serialized -               --> browser --> request.form
        if reqdata:
            errors = check_for_mandatory_fields(reqdata)
            if errors:
                returnval[ERROR] = errors
            else:
                prod.name  = reqdata.get('product_name')
                prod.qty = reqdata.get('product_qty')
                prod.price = reqdata.get('product_price')
                prod.vendor = reqdata.get('product_vendor')
                db.session.commit()
                returnval = {SUCCESS: f"Product {pid} record updated successfully...!"}
    return returnval

@app.route('/product/<int:pid>',methods=['GET'])          #http://localhost:5000/product/{pid}     get
def get_single_product(pid):
    prod = Product.query.filter_by(id=pid).first()
    if prod:
        return {SUCCESS : serialize_product(prod)}
    return {ERROR : f"Product with given id={pid} not found..!"}


@app.route('/product/<token>',methods=['GET'])         #http://localhost:5000/product/     get
def get_all_products(token):
    users =UserInfo.query.all()
    for user in users:
        if check_password_hash(user.token,token):
            prodlist = Product.query.all()
            if prodlist:
                final_product_list = []
                for prod in prodlist:
                    final_product_list.append(serialize_product(prod))
                return json.dumps({SUCCESS: final_product_list})
            return {ERROR: "No Products..!"}

    return {ERROR : "You are not Authorized to Access this API.."}



def sorted_collection(): # query -- all --> inside memory --> and memory madhe sorting-->       db independent
    prod_list = Product.query.all()
    if prod_list:   # if products asetil
        prod_list.sort(key = lambda prod : prod.price) # asc --> last product max price
        return {SUCCESS:serialize_product(prod_list[-1])}
    return {ERROR : "NO PRODUCTS"}
from sqlalchemy import text

def ordered_collection():  # this one is fast -->  orm --> db dependent
    sql = text('select * from product order by prod_price desc')
    result = db.engine.execute(sql)
    for row in result:
        return {SUCCESS: {"PRODUCT_ID": row[0],
                          "PRODUCT_NAME": row[1],
                          "PRODUCT_QUANTITY": row[4],
                          "PRODUCT_PRICE": row[3],
                          "PRODUCT_VENDOR": row[2]}}

    return {ERROR :"NO PRODUCTS"}

@app.route('/product/max',methods=['GET'])   #http://localhost:5000/product/max     get
def product_with_max_price():       # sorted collection             ordered collection
    return sorted_collection()




@app.route('/product/vendor/<vname>',methods=['GET'])  #http://localhost:5000/product/cate     get
def get_product_based_on_category(vname):
    vname = vname.lower()
    print(vname)
    prodlist = Product.query.filter(Product.vendor == vname).all()
    if prodlist:
        final_product_list = []
        for prod in prodlist:
            final_product_list.append(serialize_product(prod))
            return json.dumps({SUCCESS: final_product_list})
    return {ERROR: "No Products with Given Vendor..!"}


from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/user/new/',methods=["POST"])       # http://localhost:5000/user/new/   post        {user pwd name}
def add_user_credentials():
    reqdata = request.get_json()
    username = reqdata.get("user")
    password = reqdata.get('pwd')
    fullname = reqdata.get('name')
    userob = UserInfo(fullname=fullname,username=username,password=generate_password_hash(password))
    db.session.add(userob)
    db.session.commit()
    return {SUCCESS : "User Added Successfully...!"}

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
    db.create_all() # to create tables
    app.run(debug=True) # to start application
