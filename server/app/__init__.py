from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/graphql": {"origins": "*"}})

from app import routes

if __name__ == '__main__':
    app.run()
