from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manytone.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@localhost/restapi2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


#UserInfo(fullname,username,password)
class UserInfo(db.Model):
    fullname = db.Column('fullname', db.String(40))
    username = db.Column('username', db.String(40), primary_key=True)
    password = db.Column('password', db.String(256))
    token = db.Column('user_token', db.String(256),unique=True,nullable=True)
    active = db.Column('active',db.String(10),default='Y')
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
