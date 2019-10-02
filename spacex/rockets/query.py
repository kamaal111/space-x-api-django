from graphene import ObjectType, Field, String
from requests import get as get_request
from graphql import ResolveInfo

from config import spacex_api_url
from .schema import Rocket


class Query(ObjectType):
    rocket = Field(Rocket, rocketId=String(required=True))

    def resolve_rocket(self, info: ResolveInfo, rocketId):
        response = get_request(
            '{}rockets/{}'.format(spacex_api_url, rocketId)
        )

        return response.json()
