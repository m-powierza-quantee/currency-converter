from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, SelectField, DecimalField
# from wtforms.validators import DataRequired


class ConvertForm(FlaskForm):
  date = DateField()
  currency_from = SelectField(u'From', choices=[('PLN', 'PLN'), ('USD', 'USD'), ('EUR', 'EUR'), ('CHF', 'CHF'), ('JPY', 'JPY')])
  currency_to = SelectField(u'To', choices=[('PLN', 'PLN'), ('USD', 'USD'), ('EUR', 'EUR'), ('CHF', 'CHF'), ('JPY', 'JPY')])
  input_value = DecimalField(places=2)
  submit = SubmitField('Convert')
