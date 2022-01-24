from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    product = StringField('Product name', validators=[DataRequired()])
    expire_date = DateField('Expire date', validators=[DataRequired()])
    submit = SubmitField('Add product')
