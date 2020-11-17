from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
# graphql playground
from ariadne.constants import PLAYGROUND_HTML
from flask_sqlalchemy import SQLAlchemy
# resolvers
from graph.resolvers import resolvers

type_def = gql(load_schema_from_path("graph/schema/"))
SCHEMA = make_executable_schema(type_def, resolvers)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UWinRentdb.sqlite3'   #The database URI that should be used for the connection
db = SQLAlchemy(app)

# Define a user model
class users(db.Model):
    id = db.Collumn(db.Integer, primary_key = True)
    name = db.Collumn(db.String(128), nullable = False)
    type = db.Collumn(db.String(5), nullable = False)
    email = db.Collumn(db.String(128), nullable = False, unique = True)
    passwd = db.Collumn(db.String(192), nullable = False)
    phone = db.Collumn(db.Integer, nullable = False, unique = True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Define a property model
class properties(db.Model):
    id = db.Collumn(db.Integer, primary_key = True)
    landlord = db.Collumn(db.String(128), nullable = False)
    location = db.Collumn(db.String(500), nullable = False)
    price = db. Collumn(db.Float, nullable = False)

    def __init__(self, landlord, location, price):
        self.landlord = landlord
        self.location = location
        self.price = price

# Define a property description model
class p_descriptions(db.Model):
    id = db.Collumn(db.Integer, primary_key = True)
    pet_friendly = db.Collumn(db.Boolean, nullable = False)
    smoke_free = db.Collumn(db.Boolean, nullable = False)
    whole_house = db.Collumn(db.Boolean, nullable = False)
    rooms = db.Collumn(db.Integer, nullable = False)
    furnished = db.Collumn(db.Boolean, nullable = False)
    utilities = db.Collumn(db.Boolean, nullable = False)

    def __init__(self, pet_friendly, smoke_free, whole_house, rooms, furnished, utilities):
        self.pet_friendly = pet_friendly
        self.smoke_free = smoke_free
        self.whole_house = whole_house
        self.rooms = rooms
        self.furnished = furnished
        self.utilities = utilities
        
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
        context_value=request,
        debug=app.debug
    )

    status = 200 if success else 400
    return jsonify(result), status

@app.route('/')
def hi():
    return 'hi'

if __name__ == '__main__':
    db.create_all()         # create sql tables for data models
    app.run()
