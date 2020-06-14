from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import User

# Create your views here.

#회원정보 수정하는 기능


#회원탈퇴하는 기능
#나중에 post요청을 바꿔줘야함
def remove_user(request, user_pk):
# 회원삭제기능
# url: /accounts/user/user_pk/delete
    print('here')
    user = get_object_or_404(User, pk=user_pk)
    user.delete()
    return JsonResponse({"ok": True}, safe=False)
