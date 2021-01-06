from flask import Flask
from flask_expects_json import expects_json


app = Flask(__name__)


schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string',  "minLength": 4, "maxLength": 15},
        'mobile': {'type': 'string', "pattern": "^[1-9]{1}[0-9]{9}$"},
        'email': {'type': 'string', "pattern": "[^@]+@[^@]+\.[^@]"},
        'password': {'type': 'string', "pattern": "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).*$"}
    },
    'required': ['name', 'mobile', 'email', 'password']
}


@app.route('/', methods=['POST'])
@expects_json(schema)
def index():
    values = request.get_json()
    print(values)
    return values