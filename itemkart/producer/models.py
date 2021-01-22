from itemkart.producer.config import db,app


class Cart(db.Model):
    id = db.Column('item_id',db.Integer(),primary_key=True)
    name = db.Column('item_name',db.String(30))
    qty = db.Column('item_qty', db.Integer())
    cat = db.Column('item_cat',db.String(50))
    price = db.Column('item_price', db.Integer())


class UserInfo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # public_id = db.Column(db.Integer(max(11)))
    fullname = db.Column('fullname', db.String(40))
    username = db.Column('username', db.String(40))
    password = db.Column('password', db.String(50))
    # token = db.Column('user_token', db.String(256),unique=True,nullable=True)
    admin = db.Column('admin',db.Boolean)

    # created_on = db.Column(db.DateTime, server_default=db.func.now())
    # updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


if __name__ == '__main__':
    pro = Cart(name = "ABCD",email="abc@gmail.com")
    db.session.add(pro)
    db.session.commit()
    import sys
    sys.exit(0)
    db.create_all()
