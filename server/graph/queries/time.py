from ariadne import ObjectType
import datetime

time = ObjectType("Time")

@time.field("current")
def resolve_current(*_):
    return str(datetime.datetime.now().time())
