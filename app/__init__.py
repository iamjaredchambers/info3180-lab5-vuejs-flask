from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


csrf = CSRFProtect(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from app import views 