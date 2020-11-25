from ariadne import ObjectType

query = ObjectType("Query")

@query.field('hello')
def resolve_hello(*_):
    return True

@query.field('time')
def resolve_time(*_):
    return True

@query.field('properties')
def resolve_properties(*_):
    return [{"location": {"address": "539 Askin Ave", "latLong": "42.305780,-83.063020"}, "price": "550"},
            {"location": {"address": "401 Sunset Ave", "latLong": "42.305740,-83.065262"}, "price": "300"},
            {"location": {"address": "210 California Ave", "latLong": "42.310330,-83.066540"}, "price": "950"},
            {"location": {"address": "351 Randolf Ave", "latLong": "42.308877,-83.063144"}, "price": "650"},
            {"location": {"address": "2904 Donnelly St", "latLong": "42.303920,-83.069914"}, "price": "700"},
            {"location": {"address": "377 Rosedale Ave", "latLong": "42.305473,-83.072196"}, "price": "450"},
            {"location": {"address": "343 Askin Ave", "latLong": "42.308782,-83.064569"}, "price": "750"},
            {"location": {"address": "221 Askin Ave", "latLong": "42.310439,-83.065882"}, "price": "600"},
            ]

