from flask import request
import json
from flask_rest_api_end_to_end.producer.config import db

from flask_rest_api_end_to_end.producer.models import Product
from flask_rest_api_end_to_end.producer.service import ApplicationServices

class ProductServiceImpl(ApplicationServices):
    def add_entity(self,prod):
        if type(prod)==Product:
            db.session.add(prod)
            db.session.commit()
            print("Product added successfully")
            return True
        print("invalid Product ")
        return False

    def remove_entity(self,prid):
        dbprod=self.fetch_entity(prid)
        if dbprod:
            db.session.delete(dbprod)
            db.session.commit()
            print("Product removed")
            return True
        print("No Product with given id cannot removed")

        return False

    def update_entity(self,prid,prod):
        dbprod=self.fetch_entity(prid)
        if dbprod:
            dbprod.name=prod.name
            dbprod.qty=prod.qty
            dbprod.price=prod.price
            print("Product updated.....")
            return self.fetch_entity(prid)
        print("No product cannot update...")
    def fetch_entity(self,prid):
        if type(prid)==int and prid>0:
            prod=Product.query.filter_by(id=prid).first()
            if prod:
                return prod

    def fetch_all_entities(self):
        return Product.query.all()

