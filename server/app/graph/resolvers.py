from .queries.query import query
from .queries.hi import hi

queries = [query, hi]

mutations = []

resolvers = queries + mutations
