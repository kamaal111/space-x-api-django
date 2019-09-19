from django.http import JsonResponse
import requests

from config import spacex_api_url


def allLaunches(request):
    if request.method == 'GET':
        response = requests.get(spacex_api_url + 'launches/')

        return JsonResponse({'data': response.json()})
