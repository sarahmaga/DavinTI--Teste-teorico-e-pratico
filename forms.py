from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired, Length

# Contact form
class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    phone = StringField('Telefone', validators=[DataRequired(),Length(min=-1, max=20, message='You cannot have more than 20 characters')])
    phone2 = StringField('Telefone alternativo')
    age = IntegerField ('Idade')