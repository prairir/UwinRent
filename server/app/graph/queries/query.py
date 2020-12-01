from ariadne import ObjectType, convert_kwargs_to_snake_case
from ..models import User, Property

query = ObjectType("Query")

@query.field('hello')
def resolve_hello(*_):
    return True

#------------------------------------------------------------------------------
# Resolving users
@query.field('users')
def resolve_users(*_):
    users = [user.to_dict() for user in User.query.all()]
    return users

@query.field('user')
@convert_kwargs_to_snake_case
def resolve_user(*_, user_id):
    user = User.query.get(user_id)
    return user.to_dict()

#------------------------------------------------------------------------------
# Resolving properties
@query.field('properties')
def resolve_properties(*_):
    properties = [property_var.to_dict() for property_var in Property.query.all()]
    return properties

@query.field('property')
@convert_kwargs_to_snake_case
def resolve_property(*_, prop_id):
    property_var = Property.query.get(prop_id)
    return property_var.to_dict()