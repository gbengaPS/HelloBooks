import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# local import
from instance.config import app_config

# initialize sql-alchemy
DB = SQLAlchemy()
current_app = Flask(__name__)
bcrypt = Bcrypt(current_app)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET')
    app.config['BUNDLE_ERRORS'] = True
    DB.init_app(app)
    JWTManager(app)

    return app
