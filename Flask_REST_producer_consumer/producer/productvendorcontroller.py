from Flask_REST_producer_consumer.producer.models import Product,Vendor,db
from Flask_REST_producer_consumer.producer.config import app
from flask import request
import json


@app.route("/api/products/vendor",methods=['PATCH'])
def assign_vendor_to_products():
    reqdata = request.get_json()
    prodlist = reqdata.get('PRODUCT_IDS')  #listofids
    vendor = reqdata.get('VENDOR_ID')      #id
    vendorob = Vendor.query.filter_by(id=vendor).first()
    if vendorob:
        valid_products = []
        invalid_pids = []
        for prodid in prodlist:
            prod = Product.query.filter_by(id=prodid).first()
            if prod:
                valid_products.append(prod)
            else:
                invalid_pids.append(prodid)
        if valid_products:
            vendorob.prodrefs.extend(valid_products)
            db.session.commit()
            if not invalid_pids:
                return json.dumps({"SUCCESS" : "All PRODUCTS GIVEN TO VENDOR"})
            else:
                return json.dumps({"SUCCESS": "Few PRODUCTS GIVEN TO VENDOR","FAILED":invalid_pids})
    return json.dumps({"ERROR" : "invalid vendor/products"})

@app.route("/api/product/vendor",methods=['PATCH'])
def assign_product_to_vendor():
    reqdata = request.get_json()
    prodid = reqdata.get('PRODUCT_ID')    # id
    venid = reqdata.get('VENDOR_ID')      #id
    venob = Vendor.query.filter_by(id=venid).first()
    if venob:
        product = Product.query.filter_by(id=prodid).first()
        if product:
            venob.prodrefs.append(product)
            db.session.commit()
            return json.dumps({"SUCCESS" : "PRODUCT GIVEN TO VENDOR"})
        else:
            return json.dumps({"ERROR": "INVALID PRODUCT "})
    return json.dumps({"ERROR": "INVALID VENDOR/PRODUCT "})