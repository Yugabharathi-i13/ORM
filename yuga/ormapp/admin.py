from django.contrib import admin
from .models import Ratings, Ratingsdisplay
admin.site.register(Ratings, Ratingsdisplay)
