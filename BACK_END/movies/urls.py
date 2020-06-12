from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.review_list),
    path('create/', views.create_movie),
    path('<int:movie_pk>/', views.movie_detail),
]