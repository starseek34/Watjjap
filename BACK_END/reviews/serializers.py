from rest_framework import serializers
from .models import Review, Comment
from accounts.serializers import UserSerializer

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
        fields= ['id','user','movie','title','content','created_at','updated_at']
#comment
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user','content','created_at']

class CommentSerializer(serializers.ModelSerializer):
    user =  UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ['user','content','created_at','review']

