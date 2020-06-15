from rest_framework import serializers
<<<<<<< HEAD
from .models import Review, Movie, Comment
=======
from .models import Movie
>>>>>>> 5a28b2b4f34c785554c5cf3e37c4e90d06609753
from accounts.serializers import UserSerializer

#movie
class MovieSerializer(serializers.ModelSerializer):
   class Meta:
        pubDate=serializers.CharField(required=False)
        userRating=serializers.CharField(required=False)
       
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title','link','image','subtitle','pubDate','director','actor','userRating']



