from wtforms import Form, StringField, PasswordField, validators
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    
    def validate_email(form, field):
        if not validators.email(field.data):
            raise validators.ValidationError('Invalid email address.')
        
    def validate_username(form, field):
        if not field.data.strip():
            raise validators.ValidationError('Username cannot be empty.')
        
    def validate_password(form, field):
        if len(field.data) < 6:
            raise validators.ValidationError('Password must be at least 6 characters long.')
    
    def validate_username(form, field):
        if not field.data.strip():
            raise validators.ValidationError('Username cannot be empty.')
        
    def validate_email(form, field):
        if not validators.email(field.data):
            raise validators.ValidationError('Invalid email address.')
        
    
class EditUserForm(UserForm):
    password = PasswordField('Password', [validators.Optional()])
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    
    def validate_email(form, field):
        if not validators.email(field.data):
            raise validators.ValidationError('Invalid email address.')
