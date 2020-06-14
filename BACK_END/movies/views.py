import json
import requests

from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie


# 네이버 api에 영화검색 요청
def search(request,inputValue):
    client_id = '1U3YNsKrnM93padDO18r'
    client_secret = '7RbHN9amGw'
    url = "https://openapi.naver.com/v1/search/movie?query=" + inputValue  # json 결과
    header = {
        "X-Naver-Client-Id":client_id,
        "X-Naver-Client-secret":client_secret
    }
    res = json.loads(requests.get(url,headers=header).text)
    # result에 영화정보들이 담겨있다.
    print(res)
    return JsonResponse(res['items'],safe=False)

# 해당영화클릭하는순간, 저장되는
def save_movie():
    # 저장하는곳.
    # link비교해서 존재안하면, 저장함.
    # 그뒤에 movie 함수 실행시켜줌.
    pass

@api_view(['GET'])
def movie(request, movie_pk):
    #해당영화 정보를 보여준다.
    # url: /movies/movie_pk/
    
    #지금 현재는 검색을하면 데이터만 넘겨주는방식이고, db에 영화가 저장되어있지않다.
    # movie_pk는 영화가 저장되어있을때만, 꺼올수있고,
    # 저장안된영화라면, 저장하고서 정보를 넘겨주면된다.
        #링크가 이미 존재하는거라면 저장안하면됨.

    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

def movie_delete(request, movie_pk):
    m = get_object_or_404(Movie, pk=movie_pk)
    m.delete()  
    return JsonResponse({"ok": True},safe=False)