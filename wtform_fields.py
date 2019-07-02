from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class RegistartionForm(FlaskForm):
    """ Registartion Form """

    username = StringField('username_lable')
    email = StringField('email_lable')
    password = PasswordField('password_lable')
    confirm_pswd = PasswordField('confirm_pswd_lable')
