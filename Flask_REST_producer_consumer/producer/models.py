from Flask_REST_producer_consumer.producer.config import db,app


class Product(db.Model):
    id = db.Column('prod_id',db.Integer(),primary_key=True)
    name = db.Column('prod_name',db.String(30))
    qty = db.Column('prod_qty', db.Integer())
    price  = db.Column('prod_price', db.Integer())
    photo = db.Column('prod_photo',db.String(30),default='NA')
    venid = db.Column('ven_id', db.ForeignKey('vendor.ven_id'),unique=False,nullable=True)

class Vendor(db.Model):
    id = db.Column('ven_id', db.Integer(), primary_key=True)
    name = db.Column('ven_name', db.String(30))
    email = db.Column('ven_email',db.String(30))
    prodrefs = db.relationship(Product,uselist=True,lazy=True,backref='venref')

if __name__ == '__main__':
    ven = Vendor(name = "ABCD",email="abc@gmail.com")
    db.session.add(ven)
    db.session.commit()
    import sys
    sys.exit(0)
    db.create_all()
