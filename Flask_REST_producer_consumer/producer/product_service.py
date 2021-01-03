from flask import request
from Flask_REST_producer_consumer.producer.config import db
import json
from Flask_REST_producer_consumer.producer.service import ApplicationServices
from Flask_REST_producer_consumer.producer.models import Product


class ProductServiceImpl(ApplicationServices):  # actual implementations

    def add_entity(self,prod):
        if type(prod) == Product:
            db.session.add(prod)
            db.session.commit()
            print('Product Added')
            return True
        print('Invalid Product')
        return False

    def remove_entity(self,prid):
        dbprod = self.fetch_entity(prid)
        if dbprod:
            db.session.delete(dbprod)
            db.session.commit()
            print('Product Removed')
            return True
        print('No product with given Id cannot remove')
        return False

    def update_entity(self,prid,prod):
        dbprod = self.fetch_entity(prid)
        if dbprod:
            dbprod.name = prod.name
            dbprod.qty  = prod.qty
            dbprod.price = prod.price
            db.session.commit()
            print('Product Updated...')
            return self.fetch_entity(prid)
        print('No product..cannot update..')

    def fetch_entity(self,prid):
        if type(prid)==int and prid>0:
            prod = Product.query.filter_by(id=prid).first()
            if prod:
                return prod

    def fetch_all_entities(self):
        return Product.query.all()