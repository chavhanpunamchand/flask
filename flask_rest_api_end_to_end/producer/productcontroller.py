from flask_rest_api_end_to_end.producer.models import Product
from flask_rest_api_end_to_end.producer.config import db,app
from flask_rest_api_end_to_end.producer.product_service import ProductServiceImpl
from flask import Flask,request
# from flask_rest_api_end_to_end.producer.product_service import
import json

PRODUCT_URI="/api/product/"
pservice=ProductServiceImpl

@app.route(PRODUCT_URI, methods=['POST'])
def add_product():
    reqdata=request.get_json()
    try:
        prod=Product(name=reqdata.get("product_name"),email=reqdata.get("product_email"))
        flag=pservice.add_entity(prod)
        if flag:
            return json.dumps({"SUCCESS" : "product Added successfully...."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "problem in product Add.."})

@app.route(PRODUCT_URI +"<int:vid>", methods=['DELETE'])
def delete_product(vid):
    try:
        flag= vservice.remove_entity(vid)

        if flag:
            return json.dumps({"SUCCESS" : "product removed successfully...."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "problem in product delete.."})


@app.route(PRODUCT_URI+"<int:vid>", methods=['PUT'])
def update_product(vid):
    try:
        reqdata=request.get_json()
        ven = product(name=reqdata.get("product_name"), email=reqdata.get("product_email"))
        flag=vservice.update_entity(vid,ven)
        if flag:
            return json.dumps({"SUCCESS" : "product updated successfully...."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "problem in product update.."})

def serialize_product(product):
    return {
        "product_id":product.id,
        "product_name":product.name,
        "product_email":product.email
    }

@app.route(PRODUCT_URI+"<int:vid>", methods=['GET'])
def get_product_details(vid):
    try:
        product=vservice.fetch_entity(vid)
        if product:
            return json.dumps({"SUCCESS":serialize_product(product)})

    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "No product with given id"})


@app.route(PRODUCT_URI, methods=['GET'])
def get_all_product_details():
    try:
        products=vservice.fetch_all_entities()
        ven_list=[]
        if products:
            for ven in products:
                ven_list.append(serialize_product(ven))
            return json.dumps({"SUCCESS":ven_list})

    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "No products empty table..."})

