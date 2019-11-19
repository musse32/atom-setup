import os
import pytz
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

login_manager = LoginManager()
utc_now = pytz.utc.localize(datetime.datetime.utcnow())
est_now = utc_now.astimezone(pytz.timezone("US/Eastern"))
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey' #Secret key for the forms

#######################################################
############# SQL DATABASE SECTION ##################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'

#########################
###Register the views
