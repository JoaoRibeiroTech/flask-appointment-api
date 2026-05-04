from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agendamento.db'
app.config['SECRET_KEY'] = '491f88c0ef73b6144e56992d69e70c723b6d2ef8'
app.config['JWT_SECRET_KEY'] = 'ADMIN'

jwt = JWTManager(app)
database = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users'