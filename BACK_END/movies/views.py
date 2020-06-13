from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Review, Movie


#해당영화리스트가 나와야함.


@api_view(['GET'])
def review_list(request,movie_pk): 
# 해당 영화에 대한 리뷰리스트
# url: /movies/movie_pk/reviews
    reviews = Review.objects.filter(movie=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail(request, movie_pk, review_pk):
#해당 영화 리뷰리스트 중 특정리뷰
# url: /movies/movie_pk/reviews/review_pk    
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk): 
#해당 영화에 대한 새 리뷰
# url: /movies/movie_pk/create/
    serializer = ReviewSerializer(data=request.data)
    #reqeust.data에서 영화pk까지 같이 넘겨줘야함
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)
