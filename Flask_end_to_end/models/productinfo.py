from Flask_end_to_end.configurations.orm_config import db


class Product(db.Model):
    pid=db.Column('Prod_Id',db.Integer(),primary_key=True)
    name=db.Column('Prod_Name',db.String(100))
    qty=db.Column('Prod_qty',db.Integer())
    price=db.Column('Prod_prince',db.Float())
    cat=db.Column('Prod_cat',db.String(100))
    vendor=db.Column('Prod_vendor',db.String(100))
    active=db.Column('active',db.String(5),default="Y")
    # created_on = db.Column(db.DateTime, server_default=db.func.now())
    # updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created=db.Column('created',db.DateTime, server_default=db.func.now())
    updated=db.Column('updated',db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_by=db.Column('created_by',db.Integer(),default=0)
    updated_by=db.Column('updated_by',db.Integer(),default=0)

    @staticmethod
    def get_dummy_product():
        return Product(pid=0,name='',qty=0,price=0.0,cat='',vendor='')

    def __str__(self):
        return f" \n pID:{self.pid} Name:{self.name} qty:{self.qty} price:{self.price} cat:{self.cat} vendor:{self.vendor}"

    def __repr__(self):
        return str(self)
if __name__ == '__main__':
    pass
    # db.create_all()
    # pr1=Product(pid=103,name='Shoes',qty=20,price=800,cat='Sport',vendor='Reebok')
    # db.session.add(pr1)
    # db.session.commit()
