import graphene
from .query import Query

Schema = graphene.Schema(query=Query)
