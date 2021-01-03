'''
entities -->
        customer        -->
        product     --> manf -->
        vendor      -->
        inventory--> Vendor
        storage --> Customer
        address
        order       --> trascation
        account --> customer/vendor


'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('root', 'root', 'localhost', 'ecomdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Account --> id type balance vid
    #10--> 3 MAPPINGS -->

cust_accounts = db.Table('cust_accounts',
    db.Column('cust_id', db.ForeignKey('customer.cust_id'), unique=False),
    db.Column('acc_id', db.ForeignKey('account.acc_id'), unique=True)
)

cust_address = db.Table('cust_address',
    db.Column('cust_id', db.ForeignKey('customer.cust_id'), unique=False),
    db.Column('adr_id', db.ForeignKey('address.adr_id'), unique=False)
)

ven_address = db.Table('ven_address',
    db.Column('adr_id', db.ForeignKey('address.adr_id'), unique=False),
    db.Column('ven_id', db.ForeignKey('vendor.ven_id'), unique=False)
)

                #A              ---> hierachical                -->             A      B     c
    #b      C       D       E                                                         d

class GenericProps(db.Model):       # TABLE NOT REQUIRED
    __abstract__ = True             # TABLE NOT REQUIRED
    created = db.Column('created', db.DateTime,
                        default=db.func.current_timestamp())  # date type --> when this record added into db
    updated = db.Column('updated', db.DateTime, default=db.func.current_timestamp(),
                        onupdate=db.func.current_timestamp())  # date type --> when last time updated
    created_by = db.Column('created_by', db.Integer(), default=0)  # who created
    updated_by = db.Column('updated_by', db.Integer(), default=0)  # who last time updated


#ac1 = Account(id=111,type='Saving',balance=992.234)
class Account(GenericProps): #account -- customer --> M-1           1
    id = db.Column('acc_id',db.Integer(),primary_key=True)
    type = db.Column('acc_type',db.String(30))
    balance = db.Column('acc_bal',db.Float())
    venref = db.relationship("Vendor", backref="accref", uselist=False, lazy=True)

#c1 = Customer(id=101,name='Mr XXX',accounts=[ac1,ac2])
class Customer(GenericProps):   #customer --Account --> 1-m     ->2
    id = db.Column('cust_id',db.Integer(),primary_key=True)
    name = db.Column('cust_name',db.String(30))
    accounts = db.relationship('Account', secondary=cust_accounts,
                               backref=db.backref('customers', lazy=True))

#v1 = Vendor(id=301,name='Flipkart',accid=ac3.id)
class Vendor(GenericProps): #vendor -account --> 1-1                -->3
    id = db.Column('ven_id',db.Integer(),primary_key=True)
    name = db.Column('ven_name',db.String(30))
    accid = db.Column('acc_id',db.ForeignKey("account.acc_id"),unique=True,nullable=True)
    products = db.relationship("Product", backref="vendor", uselist=True, lazy=True)


#ad1 = Address(id=1111,city="pune katraj',customers=[c1,c2])
class Address(GenericProps):                                #4
    id = db.Column('adr_id',db.Integer(),primary_key=True)
    city = db.Column('city',db.String(30))
    customers = db.relationship(Customer, secondary=cust_address,backref=db.backref('addresses', lazy=True))
    vendors = db.relationship(Vendor, secondary=ven_address, backref=db.backref('addresses', lazy=True))


#p1 = Product(1,name='ABCD',qty=2,price=2929.34,category='A+',vid=v1.id)
class Product(GenericProps):                            #5
    id = db.Column('prod_id',db.Integer(),primary_key=True)
    name = db.Column('name',db.String(30))
    qty = db.Column('qty', db.Integer())
    price = db.Column('price', db.Float())
    category =  db.Column('category', db.String(30))
    photo  = db.Column('prod_photo',db.String(30),default='Not Available')
    vid = db.Column('ven_id',db.ForeignKey("vendor.ven_id"),unique=False,nullable=False)


class OrderedProducts(GenericProps):                    #6
    id = db.Column('pr_in_or_id', db.Integer(), primary_key=True)
    orderid = db.Column('order_id',db.ForeignKey("order.order_id"),unique=False,nullable=False)
    pid = db.Column('prod_id',db.ForeignKey("product.prod_id"),unique=False,nullable=False)
    amount = db.Column('final_bill',db.Float())

#order = OrderInfo(id=123123,cid=c1.id,vid=v1.id,discount=100,accid=c1.accounts[1].id)
class OrderInfo(db.Model):  # order --> koni-- kay - konakd- kit purchase-- amountv--date   -->7
    id = db.Column('order_id',db.Integer(),primary_key=True)
    cid = db.Column('cust_id',db.ForeignKey("customer.cust_id"),unique=False,nullable=True)
    vid = db.Column('ven_id',db.ForeignKey("vendor.ven_id"),unique=False,nullable=True)
    discount = db.Column('discount_amount',db.Float())
    accid = db.Column('cust_accid',db.Integer())           # in case refund --> direct account la
    finalbill = db.Column('final_bill',db.Float())
    created = db.Column('created', db.DateTime,default=db.func.current_timestamp())  # date type --> when this record added into db
    orderrel = db.relationship(OrderedProducts,backref="order",uselist=False,lazy=True)


if __name__ == '__main__':
    db.create_all()