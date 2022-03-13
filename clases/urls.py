import imp
from django.urls import path
from .views import nuevos_cursos


urlpatterns = [
    path('nuevo-curso/', nuevos_cursos, name= 'nuevo curso')
]    