from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import app.config

app = Flask(__name__)

print(f'ENV is: {app.config["ENV"]}')

# choosing which config to load
if app.config["ENV"] == "production":
    app.config.from_object(config.ProductionConfig)
elif app.config["ENV"] == "testing":
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

print(f'SQLALCHEMY URI is: {app.config["SQLALCHEMY_DATABASE_URI"]}')

# CORS stuff for graphql, origin stuff is weird
cors = CORS(app, resources={r"/graphql": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app import routes

if __name__ == '__main__':
    db.create_all()
    app.run()
