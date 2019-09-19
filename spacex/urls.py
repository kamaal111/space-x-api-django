from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    path('v1/launches', views.allLaunches, name='allLaunches'),
]
