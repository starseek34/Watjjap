from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    #해당 영화 리스트
    #path('<int:movie_pk>/', views.movie_list),
    path('<int:movie_pk>/reviews/', views.review_list), #해당 영화에 대한 리뷰리스트
    path('<int:movie_pk>/create/', views.create_review), #해당 영화에 대한 새 리뷰
    path('<int:movie_pk>/reviews/<int:review_pk>', views.review_detail), #해당 영화 리뷰리스트 중 해당 리뷰
]