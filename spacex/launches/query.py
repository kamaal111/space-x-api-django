from requests import get as get_request
from graphql import ResolveInfo
from graphene import ObjectType, List

from config import spacex_api_url
from .schema import All_Launches


class Query(ObjectType):
    all_launches = List(All_Launches)

    def resolve_all_launches(self, info: ResolveInfo):
        response = get_request('{}launches/'.format(spacex_api_url))
        return response.json()
