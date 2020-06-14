from django.shortcuts import render

# Create your views here.

#회원정보 수정하는 기능
def remove_review(request, movie_pk, review_pk):
    # 리뷰삭제기능
# url: /movies/movie_pk/reviews/review_pk/delete
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return JsonResponse({"ok": True}, safe=False)
#회원탈퇴하는 기능