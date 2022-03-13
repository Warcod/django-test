import imp
from django.urls import path
from .views import crear_hermanos


urlpatterns = [
    path('hermanos/', crear_hermanos)
]    