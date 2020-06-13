from rest_framework import serializers
from .models import Review, Movie, Comment
from accounts.serializers import UserSerializer

#movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
#review
class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = ['user','movie','id', 'title', 'content' ,'created_at','updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields= ['user','movie','title','content','created_at','updated_at']
#comment
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content','created_at']

