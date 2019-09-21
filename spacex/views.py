from config import spacex_api_url
from django.http import JsonResponse


def hello(request):
    if request.method == 'GET':
        return JsonResponse({'hello': 'world'})
