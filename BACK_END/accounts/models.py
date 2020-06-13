from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=200, null=True, blank=True)
#    email = models.EmailField()
    image = models.CharField(max_length=200,null=True, blank=True)

# {
#     "username": "sam",
#     "email": "sam@naver.com",
#     "nickname":"sami",
#     "image":"img.png",
#     "password1": "test1234!!",
#     "password2": "test1234!!"
# }