from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Review

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    review = get_object_or_404(Review, pk=movie_pk)
    serializer = ReviewSerializer(movie)
    return Response(serializer.data)
@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)