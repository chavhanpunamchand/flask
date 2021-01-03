from flask_rest_api_end_to_end.producer.models import Vendor
from flask_rest_api_end_to_end.producer.config import db,app
from flask_rest_api_end_to_end.producer.vendor_service import VendorServiceImpl
from flask import Flask,request
# from flask_rest_api_end_to_end.producer.vendor_service import
import json

VENDOR_URI="/api/vendor/"
vservice=VendorServiceImpl

@app.route(VENDOR_URI, methods=['POST'])
def add_vendor():
    reqdata=request.get_json()
    try:
        ven=Vendor(name=reqdata.get("vendor_name"),email=reqdata.get("Vendor_email"))
        flag=vservice.add_entity(ven)
        if flag:
            return json.dumps({"SUCCESS" : "Vendor Added successfully...."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "problem in vendor Add.."})

@app.route(VENDOR_URI +"<int:vid>", methods=['DELETE'])
def delete_vendor(vid):
    try:
        flag=vservice.remove_entity(vid)

        if flag:
            return json.dumps({"SUCCESS" : "Vendor removed successfully...."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "problem in vendor delete.."})


@app.route(VENDOR_URI+"<int:vid>", methods=['PUT'])
def update_vendor(vid):
    try:
        reqdata=request.get_json()
        ven = Vendor(name=reqdata.get("vendor_name"), email=reqdata.get("Vendor_email"))
        flag=vservice.update_entity(vid,ven)
        if flag:
            return json.dumps({"SUCCESS" : "Vendor updated successfully...."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "problem in vendor update.."})

def serialize_vendor(vendor):
    return {
        "vendor_id":vendor.id,
        "vendor_name":vendor.name,
        "vendor_email":vendor.email
    }

@app.route(VENDOR_URI+"<int:vid>", methods=['GET'])
def get_vendor_details(vid):
    try:
        vendor=vservice.fetch_entity(vid)
        if vendor:
            return json.dumps({"SUCCESS":serialize_vendor(vendor)})

    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "No vendor with given id"})


@app.route(VENDOR_URI, methods=['GET'])
def get_all_vendor_details():
    try:
        vendors=vservice.fetch_all_entities()
        ven_list=[]
        if vendors:
            for ven in vendors:
                ven_list.append(serialize_vendor(ven))
            return json.dumps({"SUCCESS":ven_list})

    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR" : "No vendors empty table..."})

