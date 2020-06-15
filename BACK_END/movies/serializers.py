from rest_framework import serializers
from .models import Movie
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



