from ariadne import ObjectType

query = ObjectType("Query")

@query.field('hello')
def resolve_hello(*_):
    return True

@query.field('time')
def resolve_time(*_):
    return True

