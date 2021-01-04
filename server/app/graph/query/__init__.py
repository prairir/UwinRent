import graphene
from .property import PropertySchema

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
