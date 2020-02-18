from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os
from flaskblog import env

app = Flask(__name__)
app.config['SECRET_KEY'] = "d53f305771bff1ab035b303277b03436"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORRT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = env.user
app.config['MAIL_PASSWORD'] = env.password
mail = Mail(app)

from flaskblog.users.routes import users

app.register_blueprint(users)

from flaskblog.posts.routes import posts

app.register_blueprint(posts)

from flaskblog.main.routes import main

app.register_blueprint(main)