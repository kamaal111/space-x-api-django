from graphene import ObjectType, Schema
from spacex.launches.query import Query as Launches_Query
from spacex.rockets.query import Query as Rocket_Query


class RootQuery(Launches_Query, Rocket_Query, ObjectType):
    pass


schema = Schema(query=RootQuery)
