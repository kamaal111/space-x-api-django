import graphene
import spacex.schema


class RootQuery(spacex.schema.RootQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery)
