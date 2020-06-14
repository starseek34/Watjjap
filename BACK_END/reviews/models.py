from django.db import models
from django.conf import settings
from faker import Faker
from accounts.models import User
from movies.models import Movie

f = Faker()
class Review(models.Model):
    #Movie랑 1:n관계
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #user랑 1:n관계
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @classmethod
    def dummy(cls, n):
        from accounts.models import User
        for _ in range(n):
            cls.objects.create(
                movie = Movie.objects.get(pk=48),
                user = User.objects.get(pk=2),
                title = f.name(),
                content = f.name()
            )

class Comment(models.Model):
    #Review랑 1:n관계
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
