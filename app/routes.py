from flask import render_template, request, redirect

from app import app
from app.forms import ConvertForm
from app.utils import currencies, query_nbp_rates, convert_value
from app.models import RatesTable


@app.route("/", methods=["GET", "POST"])
def index():
    form = ConvertForm(request.form)

    if request.method == "POST" and form.validate():
        rates_table = query_nbp_rates(form.date.data)

        if rates_table is None:
            return render_template(
                "convert.html",
                form=form,
                errors=[f"No data for {form.date.data}."],
                rates_tables=RatesTable.query.all(),
            )

        output_value = convert_value(
            form.input_value.data,
            form.currency_from.data,
            form.currency_to.data,
            rates_table,
        )
        output_value = f"{output_value:.2f}"

        rates_tables = RatesTable.query.all()

        return render_template(
            "convert.html",
            form=form,
            output_value=output_value,
            output_currency=form.currency_to.data,
            rates_tables=RatesTable.query.all(),
        )

    return render_template(
        "convert.html", form=form, rates_tables=RatesTable.query.all()
    )
