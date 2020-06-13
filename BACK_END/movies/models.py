from django.db import models
from django.conf import settings
from faker import Faker
from accounts.models import User

f = Faker()
class Movie(models.Model):
    title = models.CharField(max_length=200,default='')
    link = models.CharField(max_length=200,default='',blank=True,null=True,)
    image = models.CharField(max_length=200, null=True, blank=True,default='')
    image2 = models.CharField(max_length=200, null=True, blank=True,default='')
    subtitle = models.CharField(max_length=200,default='',blank=True,null=True)
    pubDate =models.CharField(max_length=10,default='',blank=True,null=True)
    director = models.CharField(max_length=200,default='',blank=True,null=True)
    actor = models.CharField(max_length=200,default='',blank=True,null=True)
    userRating = models.CharField(max_length=10,default='',blank=True,null=True)
    
    country = models.CharField(max_length=200, null=True, blank=True,default='')
    genre = models.CharField(max_length=200, null=True, blank=True,default='')
    runningTime = models.CharField(max_length=10, null=True, blank=True,default='')
    # user와 n:m관계
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                title = f.name(),
                pubDate = '2020-6-09',
                country = 'us',
                genre = 'horror',
                userRating = 4,
                actor = 'stone',
                director = 'emma',
                poster1 = 'poster1',
                poster2 = 'poster2',
                link = 'linklink',
                runningTime = 3,
            )

