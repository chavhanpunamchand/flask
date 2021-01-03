from login_rest_api_end_to_end.producer.config import db, app


class UserInfo(db.Model):
    id = db.Column('user_id', db.Integer(), primary_key=True)
    firstname = db.Column('first_name', db.String(30))
    lastname = db.Column('last_name', db.String(30))
    email = db.Column('email', db.String(50),unique=True)
    mobileno = db.Column('mobile_no', db.String(15))
    username = db.Column('user_name', db.String(30))
    password = db.Column('password', db.String(30))
    repassword = db.Column('repassword', db.String(30))


if __name__ == '__main__':
    # db.create_all()
    usinfo=UserInfo(id=100,firstname='Punamchand',lastname='Chavhan',email='chavhan@gmail.com',mobileno='7620637062',username='Punam',password='punam1234',repassword='punam1234')
    db.session.add(usinfo)
    db.session.commit()

