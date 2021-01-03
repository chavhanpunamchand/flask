from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#from flask_end_to_end_weekdays.configurations.app_config import app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('root','root','localhost','flaskdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=False
db = SQLAlchemy(app)

example = "1-1 MAPPING EXAMPLE"


