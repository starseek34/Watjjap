from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.CharField(max_length=200)