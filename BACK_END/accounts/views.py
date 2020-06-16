from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
import json
import requests

@api_view(['POST'])
def mypage(request):
    res = json.loads(request.body)
    print(res['id'])
    myid = res['id']
    user = get_object_or_404(User, username=myid)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#회원정보 수정하는 기능


#회원탈퇴하는 기능
#나중에 post요청을 바꿔줘야함
def remove_user(request, user_pk):
# 회원삭제기능
# url: /accounts/user/user_pk/delete
    user = get_object_or_404(User, pk=user_pk)
    user.delete()
    return JsonResponse({"ok": True}, safe=False)
