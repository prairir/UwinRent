from flask import Flask, request, jsonify

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run()
