
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manytone.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Student(db.Model): #class level fields - init --> makes instance level fields
   id = db.Column('stud_id', db.Integer(), primary_key = True)
   fname = db.Column('stud_fname',db.String(100))
   lname = db.Column('stud_lname', db.String(100))
   fees = db.Column('stud_fees',db.Float())
   aid = db.Column('aid',db.ForeignKey("address.adr_id"),unique=False,nullable=True)

class Address(db.Model):
    id = db.Column('adr_id', db.Integer, primary_key=True)
    city = db.Column('adr_city', db.String(50))
    state = db.Column('adr_state', db.String(200))
    pin = db.Column('adr_pin', db.Integer())
    studrefs = db.relationship(Student,backref="adrref",uselist=True,lazy=True)

if __name__ == '__main__':
    db.create_all()