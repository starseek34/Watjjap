from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Review

import json
import urllib.request
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
import re


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    review = get_object_or_404(Review, pk=movie_pk)
    serializer = ReviewSerializer(movie)
    return Response(serializer.data)
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