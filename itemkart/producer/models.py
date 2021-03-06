from itemkart.producer.config import db


class UserInfo(db.Model):
    """
    cart and user info database models

    """
    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column('fullname', db.String(40))
    username = db.Column('username', db.String(40))
    password = db.Column('password', db.String(200))
    admin = db.Column('admin', db.Boolean)


class Cart(db.Model):
    id = db.Column('item_id', db.Integer(), primary_key=True)
    name = db.Column('item_name', db.String(30))
    qty = db.Column('item_qty', db.Integer())
    cat = db.Column('item_cat', db.String(50))
    price = db.Column('item_price', db.Integer())


# test the module
if __name__ == '__main__':
    item = Cart(name="Shoes", qty=10, cat="Sport", price=2003)
    db.session.add(item)
    db.session.commit()
    db.create_all()
