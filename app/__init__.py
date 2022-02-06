from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from getWeekMenu import MenuParser
from getMenu import Parser

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
foods = MenuParser().parseToday()


from app import routes, models