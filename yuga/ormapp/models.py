from django.db import models
from django.contrib import admin
class Ratings(models.Model):
    moviename = models.CharField(max_length=50)
    release_year = models.IntegerField()
    director = models.CharField()
    genre = models.CharField()
    average_rating = models.FloatField()
class Ratingsdisplay(admin.ModelAdmin):
    list_display = ('moviename','release_year','director','genre','average_rating')