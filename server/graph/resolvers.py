from .queries.query import query
from .queries.hi import hi
from .queries.time import time

queries = [query, hi, time]

mutations = []

resolvers = queries + mutations
