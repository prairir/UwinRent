from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
# graphql playground
from ariadne.constants import PLAYGROUND_HTML

from flask_sqlalchemy import SQLAlchemy
from models import *

# resolvers
from graph.resolvers import resolvers

type_def = gql(load_schema_from_path("graph/schema/"))
SCHEMA = make_executable_schema(type_def, resolvers)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'   #The database URI that should be used for the connection
db = SQLAlchemy(app)

"""
    ADD ENTRY TO DATABASE:
    usr = users("Kanye", "Kanyefor2024@gmail.com")      creates user object
    db.session.add(usr)                                 add user to database's transaction
    db.session.commit()                                 commit transaction

    QUERY DATABASE:
    found_user = users.query.filter_by(name = "Kanye").first()

    .first() makes it so that it gets the first entry with the name "Kanye"
    and it returns none if no one in the database by that name is found
"""

# get method means playground
@app.route('/graphql', methods=['GET'])
def graphql_playground():
    # the access to graphql playground
    # also known as GraphiQL
    return PLAYGROUND_HTML, 200

# post means interact with graphql server
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        SCHEMA,
        data,
        context_value = request,
        debug = app.debug
    )

    status = 200 if success else 400
    return jsonify(result), status

@app.route('/')
if __name__ == '__main__':
    db.create_all()         # create sql tables for data models
    app.run()
