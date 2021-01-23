'''
import all controller for sync runnning

'''
from itemkart.producer.cartcontroller import *
from itemkart.producer.config import db
from itemkart.producer.logincontroller import *


if __name__ == '__main__':
    db.create_all()
    print('Tables created... and now service is starting..!')
    app.run(debug=True)
