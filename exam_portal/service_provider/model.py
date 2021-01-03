from exam_portal.service_provider.config import db


class Questions(db.Model):
    id = db.Column('ques_id',db.Integer(),primary_key=True)
    question = db.Column('question',db.String(255))
    option1 = db.Column('opt1',db.String(255))
    option2 = db.Column('opt2', db.String(255))
    option3 = db.Column('opt3', db.String(255))
    option4 = db.Column('opt4', db.String(255))
    answer  = db.Column('ans',db.String(255))
    username = db.Column("client_name",db.ForeignKey("login.username"),unique=False,nullable=False)
    active = db.Column('active', db.String(10), default='Y')

#Register(fullname='',email='')
class Register(db.Model):
    id = db.Column('reg_id',db.Integer(),primary_key=True)
    fullname =  db.Column('name',db.String(60))
    email =  db.Column('email',db.String(255))
    loginref = db.relationship('Login',uselist=False,lazy=True,backref="regref")


#Login(username='',password='')
class Login(db.Model):
    username = db.Column('username', db.String(30),primary_key=True)
    password = db.Column('password', db.String(255))
    token = db.Column('token', db.String(255),nullable=True)
    active = db.Column('active', db.String(10), default='Y')
    regid = db.Column('regi_id',db.ForeignKey("register.reg_id"),unique=True,nullable=True)
    roleid = db.Column('role_id', db.ForeignKey("roles.role_id"), unique=False, nullable=True)
    questions = db.relationship('Questions', uselist=True, lazy=True, backref="loginref")


#Role(id=role='')
class Roles(db.Model):
    id = db.Column('role_id', db.String(10), primary_key=True)
    role = db.Column('role_name', db.String(255))
    active = db.Column('active',db.String(10),default='Y')
    loginref = db.relationship('Login', uselist=False, lazy=True, backref="roleref")

    @staticmethod
    def get_dummy():
        return Roles(id=0,role='')

if __name__ == '__main__':
    db.create_all()