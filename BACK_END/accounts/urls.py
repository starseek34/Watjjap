from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .models import CustomAuthToken


app_name = 'accounts'

urlpatterns = [
    path('user/<int:user_pk>/delete/', views.remove_user), #해당 유저 탈퇴,삭제
    path('user/mypage/',views.mypage),
    path('api-token-auth/',CustomAuthToken.as_view()), #해당 유저정보보기
]
