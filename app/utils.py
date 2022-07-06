import requests
from bs4 import BeautifulSoup
import re

from app import db
from app.models import RatesTable


currencies = {
    "PLN": 1,
    "USD": 1,
    "EUR": 1,
    "CHF": 1,
    "JPY": 100,
}


def query_nbp_rates(date):
    # First, see if the table for this date is cached.
    cached = RatesTable.query.filter_by(date=date).first()

    if cached is not None:
        return cached
    else:
        # Otherwise, scrape the NBP page.
        rates = scrape_nbp_rates(date)

        if rates is None:
            return None

        # Add the new table to the database.
        rates_table = RatesTable(
            date=date,
            usd_rate=rates["USD"],
            eur_rate=rates["EUR"],
            chf_rate=rates["CHF"],
            jpy_rate=rates["JPY"],
        )
        db.session.add(rates_table)
        db.session.commit()

        return rates_table


def scrape_nbp_rates(date):
    # Convert the date to the proper format.
    year = f"{date.year:02}"[-2:]
    month = f"{date.month:02}"[-2:]
    day = f"{date.day:02}"[-2:]

    # Request the NBP monthly table.
    month_table_url = "https://www.nbp.pl/transfer.aspx?c=/ascx/ListABCH.ascx&Typ=a&p=rok;mies&navid=archa"
    month_table_response = requests.post(
        month_table_url, data={"mies": month, "rok": year}
    )

    # Find the link to the table for selected date.
    html = BeautifulSoup(month_table_response.text, "html.parser")
    date = f"20{year}-{month}-{day}"
    b = html.find("ul", class_="archl").find(text=date)

    if b is None:
        return None

    href = b.parent.parent["href"]

    # Request the page with the table for selected date.
    day_table_url = "https://www.nbp.pl" + href
    day_table_response = requests.get(day_table_url)

    # Find the exchange rates of the needed currencies.
    html = BeautifulSoup(day_table_response.text, "html.parser")
    nbptable = html.find("table", class_="nbptable")

    def get_rate(nbptable, currency):
        return float(
            nbptable.find(text=f"{currencies[currency]}\u00a0{currency}")
            .parent.findNext("td")
            .string.replace(",", ".")
        )

    rates = {
        currency: get_rate(nbptable, currency)
        for currency in currencies
        if currency != "PLN"
    }

    return rates


def convert_value(value, currency_from, currency_to, table):
    return (
        float(value)
        * (table.get_rate(currency_from) / currencies[currency_from])
        / (table.get_rate(currency_to) / currencies[currency_to])
    )
