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

<<<<<<< HEAD
import json
import urllib.request
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
import re


=======
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
>>>>>>> 5a28b2b4f34c785554c5cf3e37c4e90d06609753
@api_view(['GET'])
def save_movie(request):
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
            return Response(serializer.data)
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
<<<<<<< HEAD
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_movie(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

def search_movie(request):
    client_id = 'nuEUyWsfAfE27DcyjdI3'  # api id/secret이라 나중에 숨겨야함!!
    client_secret = '9CvQpAwQ_B'
    if request.method == 'GET':

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            context = {
                'items': items,
            }
            return render(request, 'search.html', context=context)    

def create_movie(request, link):
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #줄거리
    cont = re.findall('"con_tx">(.*?)</p>',str(soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p')))
    #제목
    title = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')))
    #장르
    genre = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')))
    #개봉년
    year = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(1)')))
    #감독
    director = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')))
    #네이버평점
    rating = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_area > div.netizen_score > div > div > em')))
    #포스터1
    poster1 = re.findall('src="(.*?)"', str(soup.select('#content > div.article > div.mv_info_area > div.poster > a > img')))
    #러닝타임
    runningTime = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')))
    #배우
    actor = re.findall('>(.*?)<', str(soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p')))
    # print('=================================================')
    # 이 정보들을 DB의 Movie에 집어넣으면되는데 안된다 ㅠㅠㅠ
    print(title, cont, genre, year, director, rating, poster1, runningTime, actor)





    return redirect('movies:search_movie')
=======

def movie_delete(request, movie_pk):
    m = get_object_or_404(Movie, pk=movie_pk)
    m.delete()  
    return JsonResponse({"ok": True},safe=False)
>>>>>>> 5a28b2b4f34c785554c5cf3e37c4e90d06609753
