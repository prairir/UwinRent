from app import db
from sqlalchemy.dialects.postgresql import JSON

# Define a user model
class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(5), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    passwd = db.Column(db.String(192), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    property_of = db.relationship('properties', backref='users', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Used for queries
    def __repr__(self):
        return '<User %r>' %self.name

# Define a property model
class properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    landlord = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    price = db. Column(db.Float, nullable=False)
    description_of = db.relationship('p_descriptions', backref='properties', lazy=True)

    def __init__(self, landlord, location, price):
        self.landlord = landlord
        self.location = location
        self.price = price

    # Used for queries
    def __repr__(self):
        return '<Property %r>' %self.id

# Define a property description model
class p_descriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    pet_friendly = db.Column(db.Boolean, nullable=False)
    smoke_free = db.Column(db.Boolean, nullable=False)
    whole_house = db.Column(db.Boolean, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    furnished = db.Column(db.Boolean, nullable=False)
    utilities = db.Column(db.Boolean, nullable=False)

    def __init__(self, property_id, pet_friendly, smoke_free, whole_house, rooms, furnished, utilities):
        self.property_id = property_id
        self.pet_friendly = pet_friendly
        self.smoke_free = smoke_free
        self.whole_house = whole_house
        self.rooms = rooms
        self.furnished = furnished
        self.utilities = utilities

    # Used for queries
    def __repr__(self):
        return '<Property Description %r>' %self.id
