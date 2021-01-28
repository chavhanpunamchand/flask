import json
from flask import request
from itemkart.producer.login_controller import token_required
from itemkart.producer.config import app
from itemkart.producer.models import Cart
from itemkart.producer.cart_service import CartServiceImpl

CART_URI = "/api/cart/"
pservice = CartServiceImpl()


def serialize_item(item) :
    return {"item_id" : item.id ,
            "item_name" : item.name ,
            "item_cat" : item.cat ,
            "item_price" : item.price ,
            "item_quantity" : item.qty}


# http://127.0.0.1:5000/api/cart/  POST with body
@app.route(CART_URI , methods = ['POST'])
@token_required
def add_item(current_user) :
    reqdata = request.get_json()
    try :
        item = Cart(name = reqdata.get("item_name") , qty = reqdata.get("item_qty") , cat = reqdata.get("item_cat") ,
            price = reqdata.get("item_price"))
        flag = pservice.add_entity(item)
        if flag :
            return json.dumps({"SUCCESS" : "item Added Successfully..."})
    except BaseException as b :
        print(b.args)
    return json.dumps({"ERROR" : "Problem in item Add.."})


# http://127.0.0.1:5000/api/cart/1
@app.route(CART_URI + "<int:itemid>" , methods = ['DELETE'])
@token_required
def delete_item(current_user , itemid) :
    try :
        flag = pservice.remove_entity(itemid)
        if flag :
            return json.dumps({"SUCCESS" : "Item Removed Successfully..."})
    except BaseException as b :
        print(b.args)
    return json.dumps({"ERROR" : "Problem in item delete.."})


# http://127.0.0.1:5000/api/cart/1  with body
@app.route(CART_URI + "<int:itemid>" , methods = ['PUT'])
@token_required
def update_item(current_user , itemid) :
    try :
        reqdata = request.get_json()
        item = Cart(name = reqdata.get("item_name") , qty = reqdata.get("item_qty") , cat = reqdata.get("item_cat") ,
            price = reqdata.get("item_price"))
        flag = pservice.update_entity(itemid , item)
        if flag :
            return json.dumps({"SUCCESS" : "item Updated Successfully..."})
    except BaseException as b :
        print(b.args)
    return json.dumps({"ERROR" : "Problem in item Update.."})


# http://localhost:5000/api/cart/itemid  GET
@app.route(CART_URI + "<int:itemid>" , methods = ['GET'])
@token_required
def get_item_details(current_user , itemid) :
    try :
        item = pservice.fetch_entity(itemid)
        if item :
            return json.dumps({"SUCCESS" : serialize_item(item)})
    except BaseException as b :
        print(b.args)
    return json.dumps({"ERROR" : "No item With Given Id..!"})


# http://localhost:5000/api/cart/ method=get
@app.route(CART_URI , methods = ['GET'])
@token_required
def get_all_item_details(current_user) :
    try :
        items = pservice.fetch_all_entities()
        item_list = []
        if items :
            for item in items :
                item_list.append(serialize_item(item))
            return json.dumps({"SUCCESS" : item_list})
    except BaseException as b :
        print(b.args)
    return json.dumps({"ERROR" : "No items--Empty Table.."})


# http://localhost:5000/api/cart/category  method=get
@app.route(CART_URI + "/<cat>" , methods = ['GET'])
@token_required
def get_all_item_as_per_cat(current_user , cat) :
    try :
        items = pservice.get_entity_as_per_cat(cat)
        item_list = []
        if items :
            for item in items :
                item_list.append(serialize_item(item))
            return json.dumps({"SUCCESS" : item_list})
    except BaseException as b :
        print(b.args)
    return json.dumps({"ERROR" : "No items--Empty Table.."})
