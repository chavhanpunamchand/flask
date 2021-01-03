from flask_service_impl.classpro.config import db,app


#Student(name,email,mobile)
#st = Student(id=101,name="ABCD",email="abc@gmail.com")
class Student(db.Model):
    id = db.Column('stud_id',db.Integer(),primary_key=True)
    name = db.Column('stud_name',db.String(100))
    email = db.Column('stud_email', db.String(100),unique=True)
    mobile = db.Column('stud_mobile', db.BigInteger(),unique=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10), default='Yes')
    address = db.Column('addr_id',db.ForeignKey("address.address_id"),unique=False,nullable=True)



class Teacher(db.Model):
    id = db.Column('prof_id',db.Integer(),primary_key=True)
    name = db.Column('prof_name',db.String(100))
    email = db.Column('prof_email', db.String(100))
    mobile = db.Column('prof_mobile', db.BigInteger())
    exper = db.Column('total_exp', db.Integer())
    salary = db.Column('salary', db.Float())
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10), default='Yes')
    address = db.Column('addr_id', db.ForeignKey("address.address_id"), unique=False, nullable=True)
    batchinfo = db.relationship("Batch", backref="teacherref", lazy=False, uselist=True)

class Client(db.Model):
    id = db.Column('client_id',db.Integer(),primary_key=True)
    name = db.Column('client_name', db.String(100))
    email = db.Column('client_email', db.String(100))
    mobile = db.Column('client_contact', db.BigInteger())
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10), default='Yes')
    address = db.Column('addr_id', db.ForeignKey("address.address_id"), unique=False, nullable=True)
    courses = db.relationship("Courses", backref="clientref", lazy=False, uselist=True)
    batches = db.relationship("Batch", backref="clientref", lazy=False, uselist=True)

class Courses(db.Model):
    id = db.Column('course_id',db.Integer(),primary_key=True)
    name = db.Column('course_name', db.String(100))
    code = db.Column('course_code', db.String(100))
    duration = db.Column('course_duration', db.Integer())
    fees = db.Column('course_fees', db.Float())
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10), default='Yes')
    client = db.Column('client_id', db.ForeignKey("client.client_id"), unique=False, nullable=True)


class Address(db.Model):
    id = db.Column('address_id',db.Integer(),primary_key=True)
    city = db.Column('city', db.String(100))
    state = db.Column('state', db.String(100))
    pincode = db.Column('pincode', db.Integer())
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10), default='Yes')
    studadr = db.relationship(Student,backref="adrref",lazy=False,uselist=True)
    profadr = db.relationship(Teacher, backref="adrref", lazy=False, uselist=True)
    client = db.relationship(Client, backref="adrref", lazy=False, uselist=True)

class Batch(db.Model):
    batchcode = db.Column('batch_code',db.String(100),primary_key=True)
    startdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    enddate = db.Column(db.DateTime, default=db.func.current_timestamp())
    upperlimit =  db.Column('limit', db.Integer())
    teacher = db.Column("prof_id",db.ForeignKey("teacher.prof_id"),unique=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column('active', db.String(10), default='Yes')
    client = db.Column('client_id', db.ForeignKey("client.client_id"), unique=False, nullable=True)

#sid -->  check for student -- present or absent --> StudBatchInfo --> trno ---> batchcode --> BatchDetails
class StudBatchInfo(db.Model):
    id = db.Column('stud_batch_id', db.Integer(),primary_key=True)
    tr_id = db.Column('tr_data', db.ForeignKey("trascational.serial_no"), unique=False, nullable=True)
    studid = db.Column('stud_id', db.ForeignKey("student.stud_id"), unique=False, nullable=True)


class Trascational(db.Model):
    id = db.Column('serial_no', db.String(100), primary_key=True)
    client = db.Column('clientinfo', db.ForeignKey("client.client_id"), unique=False, nullable=True)
    batchcode = db.Column('batch_no', db.ForeignKey("batch.batch_code"), unique=False, nullable=True)
    courseid = db.Column('course_id', db.ForeignKey("courses.course_id"), unique=False, nullable=True)
    fees = db.Column('that_time_fees', db.Integer())
    batchesinfo = db.relationship(StudBatchInfo, backref="trdata", lazy=False, uselist=True)

import time
if __name__ == '__main__':
    db.create_all()                  # id   name   email   mobile
    for item in range(1,11):
        st = Student(id=item, name="ABCD {}".format(item), email="{}abc@gmail.com".format(item),mobile="897654207{}".format(item))
        time.sleep(1)
        db.session.add(st)
        db.session.commit()
        print("Inserted ... {}".format(st.id))


'''
import sys
sys.exit(0)
from datetime import datetime, timedelta
from datetime import datetime, timedelta




from datetime import datetime
import calendar


# add  -- increment/decrement -- date --> in python -->
# lib shud provide
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

if __name__ == '__main__':
    today = datetime.today()
    print(today)
    nextday = datetime(year=today.year+2,month=today.month,day=today.day)
    print(nextday)
'''