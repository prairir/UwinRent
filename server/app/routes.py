from app import app, db

from flask import request, jsonify
from flask_cors import cross_origin

from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType, gql
from ariadne.constants import PLAYGROUND_HTML



# resolvers
from app.graph.resolvers import resolvers

type_def = gql(load_schema_from_path("app/graph/schema/"))
SCHEMA = make_executable_schema(type_def, resolvers, snake_case_fallback_resolvers)

# get method means playground
@app.route('/graphql', methods=['GET'])
def graphql_playground():
    # the access to graphql playground
    # also known as GraphiQL
    return PLAYGROUND_HTML, 200

# post means interact with graphql server
@app.route('/graphql', methods=['POST'])
# @cross_origin(origin='*')
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        SCHEMA,
        data,
        context_value=request,
        debug=app.debug
    )

    status = 200 if success else 400
    return jsonify(result), status

@app.route('/')
def hi():
    return 'something'
