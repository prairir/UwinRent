import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import PropertyModel

# base object
class Query(graphene.ObjectType):
    # a test 
    query_test = graphene.String()
    
    properties = graphene.List(Property)

    # resolving test
    def resolve_test(root, info):
        return f'TEST PASSED'

    def resolve_properties(root, info):
        query = Property.get_query(info)
        return query.all()

schema = graphene.Schema(query=Query)
