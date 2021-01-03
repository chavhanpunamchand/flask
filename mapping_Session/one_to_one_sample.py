from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app=Flask(__name__)


# mysql://username:password@server/db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SQLALCHEMY_ECHO']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://{}:{}@{}/{}'.format('root','root','localhost','flask_mapp')
db=SQLAlchemy(app)

class Employees(db.Model):
    eid = db.Column('Emp_Id', db.Integer(), primary_key=True)
    ename = db.Column('Emp_Name', db.String(50))
    adrref=db.relationship('Address',uselist=False,lazy=False,backref='empref')


class Address(db.Model):
    aid = db.Column('Addr_Id', db.Integer(), primary_key=True)
    acity = db.Column('Addr_city', db.String(50))
    empid = db.Column('eid', db.ForeignKey('employees.Emp_Id'),unique=True,nullable=True)


def save_instance(instance):
    db.session.add(instance)
    db.session.commit()



if __name__ == '__main__':
    db.create_all()
    e2=Employees(eid=2,ename="Pallavi")
    # a3=Address(aid=103,acity="Mumbai")
    save_instance(e2)

    # add=Address(101,"pune")
