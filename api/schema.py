import graphene
import spacex.query


class RootQuery(spacex.query.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery)
