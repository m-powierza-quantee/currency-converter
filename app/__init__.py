from flask import Flask

from app.config import Config


__version__ = '0.1.0'

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(Config)


from app import routes
