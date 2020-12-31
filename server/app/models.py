from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    passwd = db.Column(db.String(192), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    property_of = db.relationship('Property', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "email": self.email,
            "passwd": self.passwd,
            "phone": self.phone,
            "property_of": str(self.property_of)
        }

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    landlord = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description_of = db.relationship("P_descriptions", backref="properties", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "landlord": self.landlord,
            "location": self.location,
            "address": self.address,
            "price": self.price,
            "description_of": self.description_of
        }

class P_descriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    pet_friendly = db.Column(db.Boolean, nullable=False)
    smoke_free = db.Column(db.Boolean, nullable=False)
    whole_house = db.Column(db.Boolean, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    furnished = db.Column(db.Boolean, nullable=False)
    utilities = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "property_id": self.property_id,
            "pet_friendly": self.pet_friendly,
            "smoke_free": self.smoke_free,
            "whole_house": self.whole_house,
            "rooms": self.rooms,
            "funished": self.furnished,
            "utilities": self.utilities
        }
