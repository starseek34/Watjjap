from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user/<int:user_pk>/delete/', views.remove_user), #해당 유저 탈퇴,삭제

]
