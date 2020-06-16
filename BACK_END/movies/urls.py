from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'movies'

urlpatterns = [
    path('search/<str:inputValue>/', views.search),
    path('<int:movie_pk>/',views.movie),
    path('<int:movie_pk>/delete/',views.movie_delete),
    #영화저장
    path('save_movie/', views.save_movie), 
    path('search_genre/<str:inputValue>/', views.search_genre),
]
