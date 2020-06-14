from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'movies'

urlpatterns = [
    path('search/<str:inputValue>', views.search),
    path('<int:movie_pk>/',views.movie),
<<<<<<< HEAD
    path('<int:movie_pk>/delete/',views.movie_delete),
    path('save_movie/', views.save_movie),
=======
    path('<int:movie_pk>/delete/',views.movie_delete),   
    #영화저장
    path('save_movie/', views.save_movie), 
>>>>>>> 1a837cbaf8dbfebd24af197aec39cb786310ed6e
]