# movies/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la API de películas")

# Asegúrate de que esta parte también esté en `movies/views.py`
from django.http import JsonResponse
from .utils import fetch_movies, group_movies_by_year_and_actor

def movies_by_year_and_actor(request):
    api_key = 'e2e3c62e'  # Clave API de OMDB
    movies = fetch_movies(api_key)
    grouped_data = group_movies_by_year_and_actor(movies)
    return JsonResponse(grouped_data)
