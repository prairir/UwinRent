from app import app, db, schema

from flask import request, jsonify
from flask_cors import cross_origin

from flask_graphql import GraphQLView


# graphql route
# `view_func` is graphql playground stuff
app.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view( # graphql playground view function
        'graphql',
        schema=schema,
        graphiql=True
    )
)

# test route
# returns "TEST PASSED" if successfully returned
@app.route('/test')
def test():
    return 'TEST PASSED'
