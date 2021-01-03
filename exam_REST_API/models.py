from exam_REST_API.config import db


#UserInfo(fullname,username,password)
class adminUserInfo(db.Model):
    fullname = db.Column('fullname', db.String(40))
    username = db.Column('username', db.String(40), primary_key=True)
    password = db.Column('password', db.String(256))
    token = db.Column('user_token', db.String(256),unique=True,nullable=True)
    active = db.Column('active',db.String(10),default='Y')
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class UserInfo(db.Model):
    fullname = db.Column('fullname', db.String(40))
    username = db.Column('username', db.String(40), primary_key=True)
    password = db.Column('password', db.String(256))
    token = db.Column('user_token', db.String(256),unique=True,nullable=True)
    active = db.Column('active',db.String(10),default='Y')
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())



# if __name__ == '__main__':
    # db.create_all()
    # db.session.commit()
