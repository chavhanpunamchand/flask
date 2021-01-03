from flask import request
import json
from flask_rest_api_end_to_end.producer.models import Vendor
from flask_rest_api_end_to_end.producer.config import db

from flask_rest_api_end_to_end.producer.service import ApplicationServices

class VendorServiceImpl(ApplicationServices):
    def add_entity(self,ven):
        if type(ven)==Vendor:
            db.session.add(ven)
            db.session.commit()
            print("Vendor added successfully")
            return True
        print("invalid Vendor ")
        return False

    def remove_entity(self,vid):
        dbven=self.fetch_entity(vid)
        if dbven:
            db.session.delete(dbven)
            db.session.commit()
            print("Vendor removed")
            return True
        print("No Vendor with given id cannot removed")

        return False

    def update_entity(self,vid,ven):
        dbven=self.fetch_entity(vid)
        if dbven:
            dbven.name=ven.name
            dbven.email=ven.email
            print("Vendor updated.....")
            return self.fetch_entity(vid)
        print("No Vendor cannot update...")
    def fetch_entity(self,vid):
        if type(vid)==int and vid>0:
            ven=Vendor.query.filter_by(id=vid).first()
            if ven:
                return ven

    def fetch_all_entities(self):
        return Vendor.query.all()


