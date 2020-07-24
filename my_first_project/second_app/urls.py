from django.urls import path
from .views import homescreen

urlpatterns = [
    path("home/",homescreen,name="home"),
]