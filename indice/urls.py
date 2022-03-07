import imp
from django.contrib import admin
from django.urls import path
from .views import inicio

urlpatterns = [
    path('index/', inicio),
    path('admin/', admin.site.urls),
]
