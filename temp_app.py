from flask import Flask
from math import isqrt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, EqualTo, number_range, Email, length


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
    pass




class SignupForm(FlaskForm):

    def dob_check(self, field):
        fds = str(field.data)
        fdsparts = fds.split("/")
        if len(fdsparts[2]) > 4:
            raise ValueError("That's not a real date idiot")
        if len(fdsparts[2]) < 4:
            raise ValueError("That's not a real date idiot")

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address',    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    dob_check(dob)
    address = StringField('Address', validators=[DataRequired()])
    telephone = StringField('Number', validators=[DataRequired(), length(min=11, max=11, message="That's not your phone number!")])
    height = IntegerField('Height in cm', validators=[DataRequired(), number_range(min=100, max=272, message="That's not possible!")])
    weight = IntegerField('Weight in lbs', validators=[DataRequired(), number_range(min=50, max=700, message="That's not possible!")])
    submit = SubmitField('Sign Up')




def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
