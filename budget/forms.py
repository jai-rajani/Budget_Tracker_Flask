from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,FormField,FieldList,IntegerField
from wtforms.validators import DataRequired, Email, InputRequired,Length,EqualTo, NumberRange
class LoginForm(FlaskForm):
    email=StringField(label='',validators=[DataRequired(),Email()])
    password=PasswordField(label='',validators=[DataRequired(),Length(min=5)])
    login=SubmitField(label='Login in')


class RegisterForm(FlaskForm):
    rusername=StringField(label='',validators=[DataRequired()])
    remail=StringField(label='',validators=[DataRequired(),Email()])
    rpassword=PasswordField(label='',validators=[DataRequired(),Length(min=5)])
    rconfirm_password=PasswordField(label='',validators=[DataRequired(),EqualTo('rpassword'),Length(min=5)])
    rreg=SubmitField(label='Register')

class Calculator(FlaskForm):
    selector = SelectField('Select an option',validators=[DataRequired()],choices=['Salary','Loan','Gift'])
    amount=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    selector1 = SelectField('Select an option',validators=[DataRequired()],choices=['Salary','Loan','Gift'])
    amount1=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    selector2 = SelectField('Select an option',validators=[DataRequired()],choices=['Salary','Loan','Gift'])
    amount2=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    selector3 = SelectField('Select an option',validators=[DataRequired()],choices=['Salary','Loan','Gift'])
    amount3=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    selector4 = SelectField('Select an option',validators=[DataRequired()],choices=['Salary','Loan','Gift'])
    amount4=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    submitter=SubmitField(label='Submit')



class Exp_Calculator(FlaskForm):
    exp_selector = SelectField('Select an option',validators=[DataRequired()],choices=['Rent','Electricity','Water','Food','Gift','Travel'])
    exp_amount=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    exp_selector1 = SelectField('Select an option',validators=[DataRequired()],choices=['Rent','Electricity','Water','Food','Gift','Travel'])
    exp_amount1=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    exp_selector2 = SelectField('Select an option',validators=[DataRequired()],choices=['Rent','Electricity','Water','Food','Gift','Travel'])
    exp_amount2=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    exp_selector3 = SelectField('Select an option',validators=[DataRequired()],choices=['Rent','Electricity','Water','Food','Gift','Travel'])
    exp_amount3=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])
    
    exp_selector4 = SelectField('Select an option',validators=[DataRequired()],choices=['Rent','Electricity','Water','Food','Gift','Travel'])
    exp_amount4=IntegerField(label='',validators=[NumberRange(min=0,max=10000),InputRequired()])

    
    exp_submitter=SubmitField(label='Submit')
