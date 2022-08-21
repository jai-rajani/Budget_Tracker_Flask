from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app=Flask(__name__)
app.config['SECRET_KEY']='jai'
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///database/budgetdata.db'
db=SQLAlchemy(app)
login_manager=LoginManager(app)

from budget import routes
from budget import models