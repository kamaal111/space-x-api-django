from django.http import JsonResponse, HttpRequest
from config import spacex_api_url
import requests

# Create your views here.


def index(request):
    if request.method == 'GET':
        response = requests.get(spacex_api_url + 'launches/')

        return JsonResponse({'data': response.json()})
