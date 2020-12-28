from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# choosing which config to load
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print(f'ENV is: {app.config["ENV"]}')

# CORS stuff for graphql, origin stuff is weird
cors = CORS(app, resources={r"/graphql": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.graph import models
from app.schema import schema
from app.routes import routes

if __name__ == '__main__':
    db.create_all()
    app.run()
