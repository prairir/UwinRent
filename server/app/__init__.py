from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
cors = CORS(app, resources={r"/graphql": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:UWinRent-633710@localhost/UWinRent' # postgresql URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app import routes

if __name__ == '__main__':
    db.create_all()
    app.run()
