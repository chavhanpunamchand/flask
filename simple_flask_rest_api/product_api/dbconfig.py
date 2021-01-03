from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manytone.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@localhost/restapi1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column('prod_id', db.Integer(), primary_key=True)
    name = db.Column('prod_name', db.String(40), unique=True)
    vendor = db.Column('prod_vendor', db.String(40),)
    price = db.Column('prod_price',db.Float())
    qty = db.Column('prod_qty',db.Integer())

#UserInfo(fullname,username,password)
class UserInfo(db.Model):
    fullname = db.Column('fullname', db.String(40))
    username = db.Column('username', db.String(40), primary_key=True)
    password = db.Column('password', db.String(256))
    token = db.Column('user_token', db.String(256),unique=True,nullable=True)
    active = db.Column('active',db.String(10),default='Y')
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
#Product(name=,vendor,price,qty)