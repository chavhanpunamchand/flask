'''
cart service implementation
'''
from itemkart.producer.config import db
from itemkart.producer.service import ApplicationServices
from itemkart.producer.models import Cart


class CartServiceImpl(ApplicationServices):  # actual implementations

    def add_entity(self,item):
        if type(item) == Cart:
            db.session.add(item)
            db.session.commit()
            print('item Added in cart')
            return True
        print('Invalid items')
        return False

    def remove_entity(self,itemid):
        dbitem = self.fetch_entity(itemid)
        if dbitem:
            db.session.delete(dbitem)
            db.session.commit()
            print('item Removed')
            return True
        print('No item with given Id cannot remove')
        return False



    def update_entity(self,itemid,item):
        dbitem = self.fetch_entity(itemid)
        if dbitem:
            dbitem.name = item.name
            dbitem.qty  = item.qty
            dbitem.cat  = item.cat
            dbitem.price = item.price
            db.session.commit()
            print('Item Updated...')
            return self.fetch_entity(itemid)
        print('No item..cannot update..')

    def fetch_entity(self,itemid):
        if type(itemid)==int and itemid>0:
            item = Cart.query.filter_by(id=itemid).first()
            if item:
                return item

    def fetch_all_entities(self):
        return Cart.query.all()

    def get_entity_as_per_cat(self,cat):
        return Cart.query.filter_by(cat=cat)