from OneToOne.NO_MAPPING.flask_with_mvc.flask_with_mvc.config import db


class Employee(db.Model):
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(50))
    role = db.Column('emp_role', db.String(50))
    salary = db.Column('emp_salary', db.Float())

    @classmethod
    def get_dummy_emp(cls):
        return cls(id=0,name='',role='',salary=0.0)

class Address(db.Model):
    id = db.Column('adr_id', db.Integer(), primary_key=True)
    city = db.Column('adr_city', db.String(50))
    state = db.Column('adr_state', db.String(50))
    pincode = db.Column('adr_pincode', db.Integer())


    @classmethod
    def get_dummy_address(cls):
        return cls(id=0,city='',state='',pincode=0)


db.create_all() # whenever someone loads --> model.py -- create all zal pahije -- table banle pahijet