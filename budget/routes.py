from re import I
from flask import Flask,render_template,redirect,flash
from flask.helpers import url_for
from sqlalchemy.sql.expression import false
from wtforms import form
from budget.forms import LoginForm,Calculator,Exp_Calculator,RegisterForm
from budget import app,db
from budget.models import income,expense,User
from sqlalchemy import func
from datetime import datetime
from flask_login import login_user,logout_user,current_user,login_required

@app.route('/')
def intro():
     return redirect(url_for('main'))

@app.route('/main',methods=['GET','POST'])  
def main():
    form=LoginForm()  
    regform=RegisterForm()


    if regform.validate_on_submit():
        user=User.query.filter_by(email=regform.remail.data).first()
        if user:
             flash(f'Email already exists ',category='danger')
        else:
         u=User(username=regform.rusername.data,email=regform.remail.data,password=regform.rconfirm_password.data,userdate=datetime(datetime.today().year,datetime.today().month,datetime.today().day))
         db.session.add(u)
         db.session.commit()
         flash(f'Account Registered ',category='success')
         return redirect(url_for('main'))

    if form.validate_on_submit():
        print(form.email.data)
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            if(user.email==form.email.data and user.password==form.password.data):
             login_user(user,remember=True)
             flash(f'Logged in',category='success')
             return redirect(url_for('main'))  
            else:
             flash(f'Incorrect Password!',category='danger')
        else:
            flash(f'Email cannot be found ',category='danger')
           

   


    return render_template('main_page.html',form=form,regform=regform)
    
    
@app.route('/saving')
@login_required
def saving():
    sum_income=[0,0,0]
    sum_expense=[0,0,0,0,0,0]
    inc_query=income.query.filter_by(user_id=current_user.id).all()
    max=len(inc_query)
    for i in range(0,max):
      sum_income[0]=sum_income[0]+inc_query[i].salary
      sum_income[1]=sum_income[1]+inc_query[i].loan
      sum_income[2]=sum_income[2]+inc_query[i].gift
    
    exp_query=expense.query.filter_by(expuser_id=current_user.id).all()
    max=len(exp_query)
    for i in range(0,max):
      sum_expense[0]=sum_expense[0]+exp_query[i].rent
      sum_expense[1]=sum_expense[1]+exp_query[i].electricity
      sum_expense[2]=sum_expense[2]+exp_query[i].water
      sum_expense[3]=sum_expense[3]+exp_query[i].food
      sum_expense[4]=sum_expense[4]+exp_query[i].gift
      sum_expense[5]=sum_expense[5]+exp_query[i].travel
   
    return render_template('saving_page.html',s=sum_income,ss=sum_expense)
    
@app.route('/saving/today')
@login_required
def savingtoday():
    sum_income=[0,0,0]
    sum_expense=[0,0,0,0,0,0]
    inc_query=income.query.filter_by(user_id=current_user.id,incdate=datetime(datetime.today().year,datetime.today().month,datetime.today().day)).all()
    max=len(inc_query)
    for i in range(0,max):
      sum_income[0]=sum_income[0]+inc_query[i].salary
      sum_income[1]=sum_income[1]+inc_query[i].loan
      sum_income[2]=sum_income[2]+inc_query[i].gift
    
    exp_query=expense.query.filter_by(expuser_id=current_user.id,expdate=datetime(datetime.today().year,datetime.today().month,datetime.today().day)).all()
    max=len(exp_query)
    for i in range(0,max):
      sum_expense[0]=sum_expense[0]+exp_query[i].rent
      sum_expense[1]=sum_expense[1]+exp_query[i].electricity
      sum_expense[2]=sum_expense[2]+exp_query[i].water
      sum_expense[3]=sum_expense[3]+exp_query[i].food
      sum_expense[4]=sum_expense[4]+exp_query[i].gift
      sum_expense[5]=sum_expense[5]+exp_query[i].travel
   
    return render_template('saving_page.html',s=sum_income,ss=sum_expense)



@app.route('/saving/month/<month>')
@login_required
def savingmonth(month=None,methods=['GET','POST']):
    sum_income=[0,0,0]
    sum_expense=[0,0,0,0,0,0]
    months={"January":[1,31],"February":[2,28],"March":[3,31],"April":[4,30],"May":[5,31],"June":[6,30],"July":[7,31],"August":[8,31],"September":[9,30],"October":[10,31],"November":[11,30],"December":[12,31]}
    print(months[month])
    for x in range(1,months[month][1]):
      inc_query=income.query.filter_by(user_id=current_user.id,incdate=datetime(2021,months[month][0],x)).all()
      max=len(inc_query)
      for i in range(0,max):
        sum_income[0]=sum_income[0]+inc_query[i].salary
        sum_income[1]=sum_income[1]+inc_query[i].loan
        sum_income[2]=sum_income[2]+inc_query[i].gift
     
      
      exp_query=expense.query.filter_by(expuser_id=current_user.id,expdate=datetime(2021,months[month][0],x)).all()
      max=len(exp_query)
      for i in range(0,max):
        sum_expense[0]=sum_expense[0]+exp_query[i].rent
        sum_expense[1]=sum_expense[1]+exp_query[i].electricity
        sum_expense[2]=sum_expense[2]+exp_query[i].water
        sum_expense[3]=sum_expense[3]+exp_query[i].food
        sum_expense[4]=sum_expense[4]+exp_query[i].gift
        sum_expense[5]=sum_expense[5]+exp_query[i].travel
   
    return render_template('saving_page.html',s=sum_income,ss=sum_expense)

@app.route('/budget',methods=['GET','POST'])
@login_required
def budget():
    inc_form=Calculator()
    exp_form=Exp_Calculator()
    income_dic={"Salary":[0],"Loan":[0],"Gift":[0]}
    expense_dic={'Rent':[0],'Electricity':[0],'Water':[0],'Food':[0],'Gift':[0],'Travel':[0]}
    
    if inc_form.validate_on_submit():
        
        income_dic[inc_form.selector.data].append(inc_form.amount.data)
        income_dic[inc_form.selector1.data].append(inc_form.amount1.data)
        income_dic[inc_form.selector2.data].append(inc_form.amount2.data)
        income_dic[inc_form.selector3.data].append(inc_form.amount3.data)
        income_dic[inc_form.selector4.data].append(inc_form.amount4.data)

        inc=income(salary=sum(income_dic['Salary']),loan=sum(income_dic['Loan']),gift=sum(income_dic['Gift']),
        user_id=current_user.id,
        incdate=datetime(datetime.today().year,datetime.today().month,datetime.today().day))
        db.session.add(inc)
        db.session.commit()    
        flash(f' Data Saved ',category='success')
        return redirect(url_for('budget'))
   
       

        
       
    if exp_form.validate_on_submit():
        print('hi')
        expense_dic[exp_form.exp_selector.data].append(exp_form.exp_amount.data)
        expense_dic[exp_form.exp_selector1.data].append(exp_form.exp_amount1.data)
        expense_dic[exp_form.exp_selector2.data].append(exp_form.exp_amount2.data)
        expense_dic[exp_form.exp_selector3.data].append(exp_form.exp_amount3.data)
        expense_dic[exp_form.exp_selector4.data].append(exp_form.exp_amount4.data)

        exp=expense(
        rent=sum(expense_dic['Rent']),electricity=sum(expense_dic['Electricity']),
        water=sum(expense_dic['Water']),food=sum(expense_dic['Food']),
        gift=sum(expense_dic['Gift']),travel=sum(expense_dic['Travel']),
        expuser_id=current_user.id,
        expdate=datetime(datetime.today().year,datetime.today().month,datetime.today().day)
        )
        db.session.add(exp)
        db.session.commit() 
        flash(f' Data Saved ',category='success')
        return redirect(url_for('budget'))


    return render_template('budget_tracker.html',form=inc_form,exp_form=exp_form)


@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('main'))

