import graphene
import requests
import graphql

from config import spacex_api_url


class Launch(graphene.ObjectType):
    flight_number = graphene.Int()
    mission_name = graphene.String()


class RootQuery(graphene.ObjectType):
    launches = graphene.List(Launch)

    def resolve_launches(self, info: graphql.ResolveInfo, **kwargs):
        response = requests.get(spacex_api_url + 'launches/')

        response_as_list = []

        for item in response.json():
            model = Launch(item)
            response_as_list.append(item)

        return response_as_list
