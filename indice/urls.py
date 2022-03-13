import imp
from django.urls import path
from .views import inicio, otra_vista

urlpatterns = [
    path('otra/', otra_vista),
    path('', inicio),
]    