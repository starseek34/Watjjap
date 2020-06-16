import json
import requests

from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

from bs4 import BeautifulSoup
import re

# TEST GIT

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

@api_view(['GET'])
def search_genre(request, inputValue):
    genre_dict = {
        '드라마' : '1', '판타지' : '2', '서부' : '3', '공포': '4', '로맨스': '5', '모험': '6', '스릴러': '7', '느와르': '8', '컬트': '9',
        '다큐멘터리': '10', '코미디': '11', '가족': '12', '미스터리': '13', '전쟁': '14', '애니메이션': '15', '범죄': '16', '뮤지컬': '17',
        'SF': '18', '액션': '19', '무협': '20', '에로': '21', '서스펜스': '22', '서사': '23', '블랙코미디': '24', '실험': '25',
        '영화카툰': '26', '영화음악': '27', '영화패러디포스터': '28'
    }
    # print("genrecode :::", genre_dict[inputValue])
    client_id = '1U3YNsKrnM93padDO18r'
    client_secret = '7RbHN9amGw'
    url = "https://openapi.naver.com/v1/search/movie?query=e&display=6&genre="+genre_dict[inputValue]  # json 결과
    header = {
        "X-Naver-Client-Id":client_id,
        "X-Naver-Client-secret":client_secret
    }
    res = json.loads(requests.get(url,headers=header).text)
    # result에 영화정보들이 담겨있다.
    return JsonResponse(res['items'],safe=False)

# 해당영화클릭하는순간, 저장되는
@api_view(['POST'])
def save_movie(request):
    print(request.data)
    link = request.data['link']
    try:
        movie = Movie.objects.get(link=link)
    except Movie.DoesNotExist:
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        #줄거리
        plot = re.findall('"con_tx">(.*?)</p>',str(soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p')))[0]
        #장르
        genres = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')))
        genre = ""
        for i in range(len(genres)):
            if genres[i]:
                if len(genres) == 1:
                    genre = genres[i]
                elif i == len(genres) - 1:
                    genre += genres[i]
                else:
                    genre += genres[i] + "/"
        #포스터2
        image2 = re.findall('src="(.*?)"', str(soup.select('#_MainPhotoArea > div.viewer > div > img')))[0]
        #러닝타임
        runningTime = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')))[0]
        #국가
        country = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')))[0]

        print(plot, genre, image2, runningTime, country)
        
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(plot=plot, genre=genre, image2=image2, runningTime=runningTime, country=country)
            print("hihi")
            return Response(serializer.data)
    print("hello")
    return Response(MovieSerializer(movie).data)

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
