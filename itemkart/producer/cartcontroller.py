from itemkart.producer.models import Cart
from itemkart.producer.config import app
from itemkart.producer.cart_service import CartServiceImpl
from flask import request
import json

CART_URI = "/api/cart/"

pservice = CartServiceImpl()

@app.route(CART_URI,methods=['POST']) #http://127.0.0.1:5000/api/cart/  POST with body
def add_item():
    reqdata = request.get_json()
    try:
        item = Cart(name = reqdata.get("item_name"),
                      qty = reqdata.get("item_qty"),
                      cat=reqdata.get("item_cat"),
                      price = reqdata.get("item_price")
                      )
        flag = pservice.add_entity(item)
        if flag:
            return json.dumps({"SUCCESS" : "item Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in item Add.."})


@app.route(CART_URI+"<int:itemid>",methods=['DELETE']) #http://127.0.0.1:5000/api/product/1
def delete_item(itemid):
    try:
        flag = pservice.remove_entity(itemid)
        if flag:
            return json.dumps({"SUCCESS" : "Item Removed Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in item delete.."})


@app.route(CART_URI+"<int:itemid>",methods=['PUT']) #http://127.0.0.1:5000/api/product/1 body
def update_item(itemid):
    try:
        reqdata = request.get_json()
        item = Cart(name=reqdata.get("product_name"),
                       qty=reqdata.get("product_qty"),
                       cat=reqdata.get("product_cat"),
                       price=reqdata.get("product_price")
                       )
        flag = pservice.update_entity(itemid,item)
        if flag:
            return json.dumps({"SUCCESS": "item Updated Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in item Update.."})


def serialize_item(item):
   return {
        "item_id": item.id,
        "item_name" : item.name,
        "item_cat":item.cat,
        "item_price" : item.price,
        "item_quantity": item.qty
     }


@app.route(CART_URI+"<int:itemid>",methods=['GET']) #http://localhost:5000/api/product/{} GET
def get_item_details(itemid):
    try:
        item = pservice.fetch_entity(itemid)
        if item:
            return json.dumps({"SUCCESS":serialize_item(item)})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No item With Given Id..!"})


@app.route(CART_URI,methods=['GET']) #http://localhost:5000/api/product/
def get_all_item_details():
    try:
        items = pservice.fetch_all_entities()
        item_list = []
        if items:
            for item in items:
                item_list.append(serialize_item(item))
            return json.dumps({"SUCCESS":item_list})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No items--Empty Table.."})


