from ariadne import ObjectType

query = ObjectType("Query")
@query.field('hello')
def resolve_hello(*_):
    return True

hi = ObjectType('Hi')
@hi.field('word')
def resolve_test(*_):
    return 'ayo'
