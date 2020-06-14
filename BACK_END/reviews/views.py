from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer, CommentListSerializer
from .models import Review, Comment


@api_view(['GET'])
def reviews(request,movie_pk): 
# 해당 영화에 대한 리뷰리스트
# url: /movies/movie_pk/reviews
    reviews = Review.objects.filter(movie=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review(request, movie_pk, review_pk):
# 해당 영화 리뷰리스트 중 특정리뷰
# url: /movies/movie_pk/reviews/review_pk    
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_review(request, movie_pk): 
# 해당 영화에 대한 새 리뷰
# url: /movies/movie_pk/new_review/
    serializer = ReviewSerializer(data=request.data)
    #reqeust.data에서 영화pk까지 같이 넘겨줘야함
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

def remove_review(request, movie_pk, review_pk):
# 리뷰삭제기능
# url: /movies/movie_pk/reviews/review_pk/delete
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return JsonResponse({"ok": True}, safe=False)

@api_view(['GET'])
def comments(request, movie_pk, review_pk):
# 해당 리뷰에 대한 댓글리스트
# url: /movies/movie_pk/reviews/review_pk/comments
    comments = Comment.objects.filter(review=review_pk)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_comment(request,movie_pk,review_pk):
# 새 댓글
# url: /movies/movie_pk/reviews/review_pk/new_comment
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

def remove_comment(request,movie_pk,review_pk,comment_pk):
# 댓글삭제
# url: /movies/movie_pk/reviews/review_pk/comments/comment_pk/delete
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return JsonResponse({"ok": True}, safe=False)

    
