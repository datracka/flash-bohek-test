
from flask_graphql import GraphQLView
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')

    def resolve_hello(self, info):
        return 'World'


class GraphQl:
    def __init__(self, app):
        schema = graphene.Schema(query=Query)
        app.add_url_rule(
            '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
