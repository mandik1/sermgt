from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name="home"),
    path('service/add', addservice, name="addservice"),
    path('appointement/create', create_apt, name="create_apt"),
    path('appointements', apts, name="apts")
]