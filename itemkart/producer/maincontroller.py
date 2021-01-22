from itemkart.producer.cartcontroller import *
from itemkart.producer.config import db

if __name__ == '__main__':
    db.create_all()
    print('Tables created... and now service is starting..!')
    app.run(debug=True)
