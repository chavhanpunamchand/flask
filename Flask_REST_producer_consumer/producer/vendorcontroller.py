from Flask_REST_producer_consumer.producer.models import Vendor,Product
from Flask_REST_producer_consumer.producer.config import app,db
from Flask_REST_producer_consumer.producer.vendor_service import VendorServiceImpl
from flask import request
import json

VENDOR_URI = "/api/vendor/"

vservice = VendorServiceImpl()

@app.route(VENDOR_URI,methods=['POST'])
def add_vendor():
    reqdata = request.get_json()
    try:
        ven = Vendor(name = reqdata.get("vendor_name"),email = reqdata.get("vendor_email"))
        flag = vservice.add_entity(ven)
        if flag:
            return json.dumps({"SUCCESS" : "Vendor Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Vendor Add.."})


@app.route(VENDOR_URI+"<int:vid>",methods=['DELETE'])
def delete_vendor(vid):
    try:
        flag = vservice.remove_entity(vid)
        if flag:
            return json.dumps({"SUCCESS" : "Vendor Removed Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Vendor delete.."})


@app.route(VENDOR_URI+"<int:vid>",methods=['PUT'])
def update_vendor(vid):
    try:
        reqdata = request.get_json()
        ven = Vendor(name=reqdata.get("vendor_name"), email=reqdata.get("vendor_email"))
        flag = vservice.update_entity(vid,ven)
        if flag:
            return json.dumps({"SUCCESS": "Vendor Updated Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No Vendor with Given Id"})


def serialize_vendor(ven):
   return {
        "vendor_id": ven.id,
        "vendor_name" : ven.name,
        "vendor_email" : ven.email
     }


@app.route(VENDOR_URI+"<int:vid>",methods=['GET'])
def get_vendor_details(vid):
    try:
        vendor = vservice.fetch_entity(vid)
        if vendor:
            return json.dumps({"SUCCESS":serialize_vendor(vendor)})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No Vendor With Given Id..!"})


@app.route(VENDOR_URI,methods=['GET'])
def get_all_vendor_details():
    try:
        vendors = vservice.fetch_all_entities()
        ven_list = []
        if vendors:
            for ven in vendors:
                ven_list.append(serialize_vendor(ven))
            return json.dumps({"SUCCESS":ven_list})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No Vendors--Empty Table.."})

def deserialize_product(reqdata):
    return Product(id = reqdata.get("PRODUCT_ID"),
            name=reqdata.get("PRODUCT_NAME"),
            qty=reqdata.get("PRODUCT_QTY"),
            price=reqdata.get("PRODUCT_PRICE"))
@app.route(VENDOR_URI+"v1/",methods=['POST'])
def add_vendor_with_products():
    reqdata = request.get_json() # list of products and single vendor
    try:
        prodata = reqdata.get("PRODUCTS")
        products = []
        for prod in prodata:
            #products.append(deserialize_product(prod))
            dbpr = deserialize_product(prod)
            db.session.add(dbpr)
            db.session.commit()
            products.append(dbpr)

        ven = Vendor(id=reqdata.get("VENDOR_ID"),
                     name = reqdata.get("VENDOR_NAME"),
                     email = reqdata.get("VENDOR_EMAIL"))
        ven.prodrefs.extend(products)
        db.session.add(ven)
        db.session.commit()
        
        return json.dumps({"SUCCESS" : "Vendor alogn with Products Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Vendor Add.."})

