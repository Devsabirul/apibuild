from django.urls import path
from .views import *
urlpatterns = [
   path('', home, name="Home"),
   path('createtable',createDB,name="createDB"),
   path('loading',loading,name="loading"),
   path('showtable',showtable,name="showtable"),
]
    