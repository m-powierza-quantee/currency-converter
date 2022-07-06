from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config


__version__ = "0.1.0"

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
