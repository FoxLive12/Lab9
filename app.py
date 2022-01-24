from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
admin = Admin(app)