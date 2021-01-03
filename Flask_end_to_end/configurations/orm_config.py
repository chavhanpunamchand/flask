
#sqlalchemy configuration
from Flask_end_to_end.configurations.app_config import app
from Flask_end_to_end.helper.app_queries import *
from flask_sqlalchemy import SQLAlchemy
# mysql://username:password@server/db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SQLALCHEMY_ECHO']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOST,DB_NAME)
db=SQLAlchemy(app)