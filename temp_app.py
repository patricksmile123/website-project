from flask import Flask
from math import isqrt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
    pass


class SignupForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email Address')
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
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
