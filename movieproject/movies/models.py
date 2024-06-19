# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    actors = models.TextField()
