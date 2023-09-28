from django.urls import path
from .views import *
urlpatterns = [
   path('', home, name="Home"),
   path('createtable',createDB,name="createDB")
]
    