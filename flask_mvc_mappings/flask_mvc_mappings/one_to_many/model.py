from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onetomany.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
#1stud-manyaddress
class Student(db.Model): #class level fields - init --> makes instance level fields
   id = db.Column('stud_id', db.Integer(), primary_key = True)
   fname = db.Column('stud_fname',db.String(100))
   lname = db.Column('stud_lname', db.String(100))
   fees = db.Column('stud_fees',db.Float())
   adrrefs = db.relationship("Address", backref="studref", uselist=True, lazy=True)

   @classmethod
   def get_dummy_instance(cls):
       return cls(id=0, fname='', lname='', fees=0.0)

class Address(db.Model):
    id = db.Column('adr_id', db.Integer, primary_key=True)
    city = db.Column('adr_city', db.String(50))
    state = db.Column('adr_state', db.String(200))
    pin = db.Column('adr_pin', db.Integer())
    sid = db.Column('sid', db.ForeignKey("student.stud_id"), unique=False, nullable=True)

    @classmethod
    def get_dummy_instance(cls):
        return cls(id=0, city='', state='', pin=0)


db.create_all()