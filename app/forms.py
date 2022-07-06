from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, SelectField, DecimalField

from app.utils import currencies


class ConvertForm(FlaskForm):
    date = DateField()
    choices = [(currency, currency) for currency in currencies]
    currency_from = SelectField("From", choices=choices)
    currency_to = SelectField("To", choices=choices)
    input_value = DecimalField(places=2)
    submit = SubmitField("Convert")
