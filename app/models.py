from app import db


class RatesTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    usd_rate = db.Column(db.Float)
    eur_rate = db.Column(db.Float)
    chf_rate = db.Column(db.Float)
    jpy_rate = db.Column(db.Float)

    def get_rate(self, name):
        if name == "USD":
            return self.usd_rate
        elif name == "EUR":
            return self.eur_rate
        elif name == "CHF":
            return self.chf_rate
        elif name == "JPY":
            return self.jpy_rate
        elif name == "PLN":
            return 1
        else:
            return None
