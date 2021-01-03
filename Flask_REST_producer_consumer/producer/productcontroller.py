from Flask_REST_producer_consumer.producer.models import Product
from Flask_REST_producer_consumer.producer.config import app
from Flask_REST_producer_consumer.producer.product_service import ProductServiceImpl
from flask import request
import json

PRODUCT_URI = "/api/product/"

pservice = ProductServiceImpl()

@app.route(PRODUCT_URI,methods=['POST']) #http://127.0.0.1:5000/api/product/  POST with body
def add_product():
    reqdata = request.get_json()
    try:
        prod = Product(name = reqdata.get("product_name"),
                      qty = reqdata.get("product_qty"),
                      price = reqdata.get("product_price"),
                      photo = reqdata.get("product_photo"))
        flag = pservice.add_entity(prod)
        if flag:
            return json.dumps({"SUCCESS" : "Product Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Product Add.."})


@app.route(PRODUCT_URI+"<int:pid>",methods=['DELETE'])
def delete_product(pid):
    try:
        flag = pservice.remove_entity(pid)
        if flag:
            return json.dumps({"SUCCESS" : "PRODUCT Removed Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Product delete.."})


@app.route(PRODUCT_URI+"<int:pid>",methods=['PUT'])
def update_product(pid):
    try:
        reqdata = request.get_json()
        prod = Product(name=reqdata.get("product_name"),
                       qty=reqdata.get("product_qty"),
                       price=reqdata.get("product_price"),
                       photo=reqdata.get("product_photo"))
        flag = pservice.update_entity(pid,prod)
        if flag:
            return json.dumps({"SUCCESS": "Product Updated Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Product Update.."})


def serialize_product(prod):
   return {
        "product_id": prod.id,
        "product_name" : prod.name,
        "product_price" : prod.price,
       "product_quantity": prod.qty,
       "product_photo": prod.photo
     }


@app.route(PRODUCT_URI+"<int:pid>",methods=['GET']) #http://localhost:5000/api/product/{} GET
def get_product_details(pid):
    try:
        product = pservice.fetch_entity(pid)
        if product:
            return json.dumps({"SUCCESS":serialize_product(product)})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No Product With Given Id..!"})


@app.route(PRODUCT_URI,methods=['GET'])
def get_all_product_details():
    try:
        products = pservice.fetch_all_entities()
        prod_list = []
        if products:
            for prod in products:
                prod_list.append(serialize_product(prod))
            return json.dumps({"SUCCESS":prod_list})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No Product--Empty Table.."})



@app.route(PRODUCT_URI+"photo/",methods=['POST'])
def add_product_with_photo():
    reqdata = request.form  # text format wala      request.form['name']      request.form.getlist('name')
    file = request.files['product_photo']           #request.files['dp']     request.files.getlist('dp')
    print("File",file)
    print("other data",reqdata)

    name = reqdata.get("product_name")
    file.save(name+".png")

    try:
        prod = Product(name = reqdata.get("product_name"),
                      qty = reqdata.get("product_qty"),
                      price = reqdata.get("product_price"),
                      photo = name+".png")
        flag = pservice.add_entity(prod)
        if flag:
            return json.dumps({"SUCCESS" : "Product Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Product Add.."})
