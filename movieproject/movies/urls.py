# movies/urls.py
from django.urls import path
from .views import home, movies_by_year_and_actor

urlpatterns = [
    path('', home, name='home'),
    path('movies/', movies_by_year_and_actor, name='movies_by_year_and_actor'),
]
