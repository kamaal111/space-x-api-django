from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    path('', views.index, name='index'),
]
