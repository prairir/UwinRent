from ariadne import ObjectType

hi = ObjectType('Hi')
@hi.field('word')
def resolve_test(*_):
    return 'sup dawg'
