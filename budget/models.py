from enum import unique
import re
from budget import db,login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    inc_user = db.relationship('income', backref='user')
    userdate=db.Column(db.DateTime)
    def __init__(self,username,email,password,userdate):
        self.username=username
        self.userdate=userdate
        self.email=email
        self.password=password
        

class income(db.Model):
    inc_id=db.Column(db.Integer,primary_key=True)
    salary=db.Column(db.Integer,nullable=True)
    loan=db.Column(db.Integer,nullable=True)
    gift=db.Column(db.Integer,nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    incdate=db.Column(db.DateTime)
    def __init__(self,incdate,salary,loan,gift,user_id):
        self.salary=salary
        self.loan=loan
        self.gift=gift
        self.user_id=user_id
        self.incdate=incdate

class expense(db.Model):
    exp_id=db.Column(db.Integer,primary_key=True)
    rent=db.Column(db.Integer,nullable=True)
    electricity=db.Column(db.Integer,nullable=True)
    water=db.Column(db.Integer,nullable=True)
    food=db.Column(db.Integer,nullable=True)
    gift=db.Column(db.Integer,nullable=True)
    travel=db.Column(db.Integer,nullable=True)
    expuser_id=db.Column(db.Integer)
    expdate=db.Column(db.DateTime)
    def __init__(self,expdate,rent,electricity,water,food,gift,travel,expuser_id):
        self.rent=rent
        self.electricity=electricity
        self.water=water
        self.food=food
        self.gift=gift
        self.travel=travel
        self.expuser_id=expuser_id
        self.expdate=expdate

class Test(db.Model):
    did=db.Column(db.Integer,primary_key=True)
    tester=db.Column(db.DateTime)
    
    def __init__(self,tester):
        self.tester=tester
