from config import spacex_api_url
import requests
from django.http import JsonResponse


def allLaunches(request):
    if request.method == 'GET':
        response = requests.get(spacex_api_url + 'launches/')

        return JsonResponse({'data': response.json()})
