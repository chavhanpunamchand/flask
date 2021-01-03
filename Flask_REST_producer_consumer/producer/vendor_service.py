from Flask_REST_producer_consumer.producer.config import db
from Flask_REST_producer_consumer.producer.service import ApplicationServices
from Flask_REST_producer_consumer.producer.models import Vendor

class VendorServiceImpl(ApplicationServices):

    def add_entity(self, ven):
        if type(ven) == Vendor:
            db.session.add(ven)
            db.session.commit()
            print('Vendor Added')
            return True
        print('Invalid Vendor')
        return False

    def remove_entity(self, vid):
        dbven = self.fetch_entity(vid)
        if dbven:
            db.session.delete(dbven)
            db.session.commit()
            print('Vendor Removed')
            return True
        print('No Vendor with given Id cannot remove')
        return False

    def update_entity(self, vid, ven):
        dbven = self.fetch_entity(vid)
        if dbven:
            dbven.name = ven.name
            dbven.email = ven.email
            db.session.commit()
            print('Vendor Updated...')
            return self.fetch_entity(vid)
        print('No Vendor..cannot update..')

    def fetch_entity(self, vid):
        if type(vid) == int and vid > 0:
            ven = Vendor.query.filter_by(id=vid).first()
            if ven:
                return ven

    def fetch_all_entities(self):
        return Vendor.query.all()