from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onetone.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#app.template_folder = "/pages"
db = SQLAlchemy(app)

class Student(db.Model): #class level fields - init --> makes instance level fields
   id = db.Column('stud_id', db.Integer(), primary_key = True)
   fname = db.Column('stud_fname',db.String(100))
   lname = db.Column('stud_lname', db.String(100))
   fees = db.Column('stud_fees',db.Float())
   aid = db.Column('aid',db.ForeignKey("address.adr_id"),unique=True,nullable=False) #tighly coupled

   @classmethod
   def get_dummy_instance(cls):
        return cls(id=0,fname='',lname='',fees=0.0)

class Address(db.Model):
    id = db.Column('adr_id', db.Integer, primary_key=True)
    city = db.Column('adr_city', db.String(50))
    state = db.Column('adr_state', db.String(200))
    pin = db.Column('adr_pin', db.Integer())
    studref = db.relationship(Student,backref="adrrefs",uselist=False,lazy=True)

    @classmethod
    def get_dummy_instance(cls):
        return cls(id=0,city='',state='',pin=0)

db.create_all() #anyone imports this modules tables shud be created.