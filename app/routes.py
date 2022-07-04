from flask import render_template
import requests
from bs4 import BeautifulSoup
import re

from app import app
from app.forms import ConvertForm


@app.route('/')
def index():
  form = ConvertForm()

  return render_template('convert.html', form=form)


@app.route('/test')
def test():
  # nbp_url = 'https://www.nbp.pl/transfer.aspx?c=/ascx/ListABCH.ascx&Typ=a&p=rok;mies&navid=archa'
  year = '22'
  month = '06'
  day = '01'
  # nbp_url = f'https://www.nbp.pl/kursy/xml/a127z220704.xml'
  month_table_url = 'https://www.nbp.pl/transfer.aspx?c=/ascx/ListABCH.ascx&Typ=a&p=rok;mies&navid=archa'
  # nbp_url = f'https://www.nbp.pl/kursy/xml/a127z{year}{month}{day}.xml'
  res = requests.post(month_table_url, data={ 'mies': month, 'rok': year })
  html = BeautifulSoup(res.text, 'html.parser')

  ul = html.find("ul", class_="archl").find(string=re.compile(f'z dnia 20{year}-{month}-{day}'))

  return ''.join(str(link) for link in ul)
