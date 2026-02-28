from wtforms import Form, StringField, PasswordField, validators
from flask_wtf import FlaskForm


from wtforms import Form, StringField, PasswordField, validators
from flask_wtf import FlaskForm

class ContactForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
   
    phone_number = StringField('Phone Number', [validators.DataRequired()])
    
    def validate_phone_number(form, field):
        if not field.data.isdigit():
            raise validators.ValidationError('Phone number must contain only digits.')
        
    def validate_name(form, field):
        if not field.data.strip():
            raise validators.ValidationError('Name cannot be empty.')
        
        
class EditContactForm(ContactForm):
    pass
