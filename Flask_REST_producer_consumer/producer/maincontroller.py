from Flask_REST_producer_consumer.producer.productcontroller import *
from Flask_REST_producer_consumer.producer.vendorcontroller import *
from Flask_REST_producer_consumer.producer.productvendorcontroller import *
from Flask_REST_producer_consumer.producer.config import db

if __name__ == '__main__':
    db.create_all()
    print('Tables created... and now service is starting..!')
    app.run(debug=True)
