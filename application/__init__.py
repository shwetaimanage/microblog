from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# ask flask to read from config file
app.config.from_object(Config)

# initialize db instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes, models