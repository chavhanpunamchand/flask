from itemkart.producer.config import db,app


class Cart(db.Model):
    id = db.Column('item_id',db.Integer(),primary_key=True)
    name = db.Column('item_name',db.String(30))
    qty = db.Column('item_qty', db.Integer())
    cat = db.Column('item_cat',db.String(50))
    price = db.Column('item_price', db.Integer())




if __name__ == '__main__':
    pro = Cart(name = "ABCD",email="abc@gmail.com")
    db.session.add(pro)
    db.session.commit()
    import sys
    sys.exit(0)
    db.create_all()
