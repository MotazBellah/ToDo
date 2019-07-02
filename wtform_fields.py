from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class RegistartionForm(FlaskForm):
    """ Registartion Form """

    username = StringField('username_lable',
                            validators=[InputRequired(message="Username Required"),
                                        Length(min=4, max=25, message="Username must be between 4 and 25 charachters")])
    email = StringField('email_lable',
                        validators=[InputRequired(message="Email Required"), Email(message="This field requires a valid email address")])
    password = PasswordField('password_lable',
                             validators=[InputRequired(message="Password Required"),
                                        Length(min=4, max=25, message="Username must be between 4 and 25 charachters")])
    confirm_pswd = PasswordField('confirm_pswd_lable',
                                 validators=[InputRequired(message="Password confirmation Required"),
                                            EqualTo('password', message="Password must match!"))])

    submit_button = SubmitField("Create")
