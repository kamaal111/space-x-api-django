import graphene
import requests
import graphql

from config import spacex_api_url
from .schema import Launch


class Query(graphene.ObjectType):
    all_launches = graphene.List(Launch)

    def resolve_all_launches(self, info: graphql.ResolveInfo, **kwargs):
        response = requests.get(spacex_api_url + 'launches/').json()
        return response
