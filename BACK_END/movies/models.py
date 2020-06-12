from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=200)
    pubDate =models.DateTimeField()
    country = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    userRating = models.IntegerField()
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    poster1 = models.CharField(max_length=200)
    poster2 = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    runningTime = models.IntegerField()

class Review(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)