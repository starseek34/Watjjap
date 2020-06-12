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

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Review(models.Model):
    #Movie랑 1:n관계
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #user랑 1:n관계
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    #Review랑 1:n관계
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
