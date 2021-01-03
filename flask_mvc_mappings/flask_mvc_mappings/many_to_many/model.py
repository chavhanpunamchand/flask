from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manytomany.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

stud_adr_mapping = db.Table('stud_adr_mapping',
            db.Column('mp_id', db.Integer(), primary_key = True),
            db.Column('st_id', db.ForeignKey("student.stud_id"),unique=False),
            db.Column('ad_id',  db.ForeignKey("address.adr_id"),unique=False)
)

class Student(db.Model): #class level fields - init --> makes instance level fields
   id = db.Column('stud_id', db.Integer(), primary_key = True)
   fname = db.Column('stud_fname',db.String(100))
   lname = db.Column('stud_lname', db.String(100))
   fees = db.Column('stud_fees',db.Float())


class Address(db.Model):
    id = db.Column('adr_id', db.Integer, primary_key=True)
    city = db.Column('adr_city', db.String(50))
    state = db.Column('adr_state', db.String(200))
    pin = db.Column('adr_pin', db.Integer())
    studrefs = db.relationship(Student,secondary=stud_adr_mapping,backref=db.backref('adrrefs',lazy=True))

if __name__ == '__main__':
    db.create_all()