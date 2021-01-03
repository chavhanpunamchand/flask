from AcademyREST_API.producer.config import db,app


class Student(db.Model):
    id = db.Column('stud_id',db.Integer(),primary_key=True)
    fullname = db.Column('Stud_fullname',db.String(50))
    age = db.Column('stud_age', db.Integer())
    email = db.Column('stud_email', db.String(60))
    photo = db.Column('stud_photo',db.String(30),default='NA')
    courid = db.Column('course_id', db.ForeignKey('courses.course_id'),unique=False,nullable=True)

class Courses(db.Model):
    id = db.Column('course_id', db.Integer(), primary_key=True)
    name = db.Column('course_name', db.String(30))
    fees = db.Column('course_fees',db.Float())
    studrefs = db.relationship(Student,uselist=True,lazy=True,backref='coursesref')

if __name__ == '__main__':
    stud1 = Student(fullname="Shrikant Rathod",age=27,email="rathodshree@gmail.com",photo="NA")
    db.session.add(stud1)
    db.session.commit()
    course1=Courses(id=101,name="Python_fullstack",fees=40000)
    db.session.add(course1)
    db.session.commit()

    import sys
    sys.exit(0)
    db.create_all()