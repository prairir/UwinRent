import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Property

class PropertySchema(SQLAlchemyObjectType):
    class Meta:
        model = Property

# base object
class Query(graphene.ObjectType):
    # a test 
    query_test = graphene.String()
    
    properties = graphene.List(PropertySchema)

    # resolving test
    def resolve_query_test(root, info):
        return f'TEST PASSED'

    def resolve_properties(root, info):
        query = PropertySchema.get_query(info)
        return query.all()

Schema = graphene.Schema(query=Query)
