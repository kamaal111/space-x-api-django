from django.http import JsonResponse, HttpRequest

# Create your views here.


def index(request):
    if request.method == 'GET':
        context = {'hello': 'hello'}

        return JsonResponse(context)
