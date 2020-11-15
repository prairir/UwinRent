# Import the database object (db) from the main application module
from database import db

# Define a base model for other database tables to inherit
class Base (db.Model):
    __abstract__ = True

    id = db.Collumn(db.integer, primary_key = True)
    date_created = db.Collumn(db.DateTime, default = db.func.current_timestamp())
    date_modified = db.Collumn(db.DateTime, default = db.func.current_timestamp()),
                                             onupdate = db.func.current_timestamp())

# Define a user model
class User(Base):

    __tablename__ = 'auth_user'

    id = db.Collumn(db.Integer, nullable = False, unique = True)
    name = db.Collumn(db.String(128), nullable = False)
    type = db.Collumn(db.String(5), nullable = False)
    email = db.Collumn(db.String(128), nullable = False, unique = True)
    passwd = db.Collumn(db.String(192), nullable = False)
    phone = db.Collumn(db.Integer, nullable = False, unique = True)

    def __init__(self, name, email, passwd):

        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

# Define a property model
class Properties(Base):

    __tablename__ = 'auth_properties'

    id = db.Collumn(db.Integer, nullable = False, unique = True)
    landlord = db.Collumn(db.String(128), nullable = False)
    location = db.Collumn(db.String(500), nullable = False)
    price = db. Collumn(db.Float, nullable = False)

    def __init__(self, location, price):

        self.location = location
        self.price = price

    def __repr__(self):
        return '<Property %r>' % (self.location)

# Define a property description model
class P_Description(Base):

    __tablename__ = 'auth_p_description'

    id = db.Collumn(db.Integer, nullable = False, unique = True)
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

    def __repr__(self):
        return '<PropertyDescription %r>' % (self.rooms)
