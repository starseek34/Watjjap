from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.reviews), #해당 영화에 대한 리뷰리스트
    path('new_review/', views.new_review), #해당 영화에 대한 새 리뷰
    path('reviews/<int:review_pk>/', views.review), #해당 영화 리뷰리스트 중 해당 리뷰
    path('reviews/<int:review_pk>/delete/', views.remove_review),#특정리뷰삭제

    path('reviews/<int:review_pk>/comments/', views.comments), #댓글리스트
    path('reviews/<int:review_pk>/new_comment/', views.new_comment), #댓글생성
    path('reviews/<int:review_pk>/comment/<int:comment_pk>/delete/', views.remove_comment), #댓글삭제

]