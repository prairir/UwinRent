from . import db

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
    landlord = db.Collumn(db.String(128), nullable = False, ForeignKey('users.id'))
    location = db.Collumn(db.String(500), nullable = False)
    price = db. Collumn(db.Float, nullable = False)

    def __init__(self, landlord, location, price):
        self.landlord = landlord
        self.location = location
        self.price = price

# Define a property description model
class p_descriptions(db.Model):
    id = db.Collumn(db.Integer, primary_key = True)
    property_id = db.Collumn(db.Integer, ForeignKey('properties.id'))
    pet_friendly = db.Collumn(db.Boolean, nullable = False)
    smoke_free = db.Collumn(db.Boolean, nullable = False)
    whole_house = db.Collumn(db.Boolean, nullable = False)
    rooms = db.Collumn(db.Integer, nullable = False)
    furnished = db.Collumn(db.Boolean, nullable = False)
    utilities = db.Collumn(db.Boolean, nullable = False)

    def __init__(self, property_id, pet_friendly, smoke_free, whole_house, rooms, furnished, utilities):
        self.property_id = property_id
        self.pet_friendly = pet_friendly
        self.smoke_free = smoke_free
        self.whole_house = whole_house
        self.rooms = rooms
        self.furnished = furnished
        self.utilities = utilities
