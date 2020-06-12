from rest_framework import serializers
from .models import Review
from accounts.serializers import UserSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'
