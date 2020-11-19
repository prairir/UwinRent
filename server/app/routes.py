from app import app

from flask import request, jsonify

from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
# graphql playground
from ariadne.constants import PLAYGROUND_HTML

# resolvers
from app.graph.resolvers import resolvers

type_def = gql(load_schema_from_path("app/graph/schema/"))
SCHEMA = make_executable_schema(type_def, resolvers)

# get method means playground
@app.route('/graphql', methods=['GET'])
def graphql_playground():
    # the access to graphql playground
    # also known as GraphiQL
    return PLAYGROUND_HTML, 200

# post means interact with graphql server
@app.route('/graphql', methods=['POST'])
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
    return 'hi'
