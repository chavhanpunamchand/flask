from flask_initial_web_service_demo.config import db

class GenericModel(db.Model):
    __abstract__ = True
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10),default='Yes')

#Hotel(id=1111,name='Sayaji',address='Pune,wakad',contact='020-12234453',website='www.sayaji.com')
class Hotel(GenericModel):
    id = db.Column('hotel_id',db.Integer(),primary_key=True)
    name = db.Column('hotel_name',db.String(40),unique=True)
    address = db.Column('hotel_address',db.String(40))
    contact = db.Column('hotel_contact',db.String(40))
    website = db.Column('hotel_website', db.String(40))
    accno = db.Column("acc_id", db.ForeignKey("account.acc_no"), unique=False, nullable=True)
    menuref = db.relationship("Menu",lazy=True,backref="hotelref",uselist=True)
    roomref = db.relationship("Room",lazy=True,backref="hotelref",uselist=True)
    orderref = db.relationship("Mainorder", lazy=True, backref="hotelref", uselist=True)

#Room(id=1,type='STD',charge=1922.45,status='A',hotelid=)

class Room(GenericModel):
    id = db.Column('room_id', db.Integer(), primary_key=True)
    type = db.Column('room_type', db.String(40),)
    charge = db.Column('room_charge',db.Float())
    status = db.Column('room_status',db.String(30))
    hotelid = db.Column("hotel_id",db.ForeignKey("hotel.hotel_id"),unique=False,nullable=True)

#Account(id=111,type='Current',balance=1022.234)
class Account(GenericModel):
    id = db.Column('acc_no', db.Integer(), primary_key=True)
    type = db.Column('acc_type', db.String(40))
    balance = db.Column('acc_bal', db.Float())
    hotelref = db.relationship(Hotel,lazy=True,backref="accref",uselist=True)
    custref = db.relationship("Customer",lazy=True,backref="accref",uselist=True)

#Menu(id=991,name='XXXXX',price=394.45,hotelid=12)
class Menu(GenericModel):
    id = db.Column('menu_id', db.Integer(), primary_key=True)
    name = db.Column('menu_name', db.String(40),)
    price = db.Column('menu_price', db.Float(),default=350.0)
    hotelid = db.Column("hotel_id", db.ForeignKey("hotel.hotel_id"), unique=False, nullable=False)


class Customer(GenericModel):
    id = db.Column('cust_id', db.Integer(), primary_key=True)
    name = db.Column('cust_name', db.String(40), unique=True)
    address = db.Column('cust_address', db.String(40),)
    contact = db.Column('cust_contact',db.Integer())
    email = db.Column('cust_email',db.String(40))
    accno = db.Column("acc_id", db.ForeignKey("account.acc_no"), unique=False, nullable=True)
    orderref = db.relationship("Mainorder",lazy=True,backref="custref",uselist=True)

class ProcessedOrder(GenericModel):
    id = db.Column('pr_order_id', db.Integer(), primary_key=True)
    orderId = db.Column("order_id",db.ForeignKey("mainorder.order_id"),unique=False)
    menuid =  db.Column("menus",db.ForeignKey("menu.menu_id"),unique=False,nullable=True)
    roomid = db.Column("room",db.ForeignKey("room.room_id"),unique=False,nullable=True)
    finalprice = db.Column('menu_price', db.Float())
    qty = db.Column('menu_qty', db.Integer())

class Mainorder(GenericModel):
    id = db.Column('order_id', db.Integer(), primary_key=True)
    cid = db.Column('cust_id', db.ForeignKey("customer.cust_id"),nullable=False,unique=False)
    hid = db.Column('hotel_id', db.ForeignKey("hotel.hotel_id"),nullable=False,unique=False)
    billamount = db.Column('total_bill', db.Float())

if __name__ == '__main__':
    db.create_all()
    ht = Hotel(101, 'Sayaji', 'Pune-wakad', '020-12234453', 'www.sayaji.com',None)
    db.session.add(ht)
    db.session.commit()

'''
Hotel Booking Service..
        Hotel
        Rooms
        Account
        Menu
        Order
        Customer
        
ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';


ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
'''