from bs4 import BeautifulSoup
import json
import requests
import os
import datetime
import csv


key = os.getenv("KEY_MOV")
data = []
with open('boxoffice.csv', newline = '') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row[0])
del data[0]

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=' + key
answer = []
for d in data:
    params = {
        'movieCd' : d
    }

    res = requests.get(url, params = params).text
    doc = json.loads(res)
    temp = doc['movieInfoResult']['movieInfo']
    genres = ""
    for i in temp['genres']:
      genres += i['genreNm'] + "/"
    actors = [""]*3
    for a in range(len(temp['actors'])):
      if a==3:
        break
      else:
        actors[a] = temp['actors'][a]['peopleNm']
 
    result = {
        '영화코드' : d,
        '영화명(국문)' : temp['movieNm'],
        '영화명(영문)' : temp['movieNmEn'],
        '영화명(원문)' : temp['movieNmOg'],
        '개봉연도': temp['prdtYear'],
        '상영시간': temp['showTm'],
        '장르' : genres[:-1],
        '감독명' : temp['directors'][0]['peopleNm'],
        '관람등급': temp['audits'][0]['watchGradeNm'],
        '배우1': actors[0],
        '배우2': actors[1],
        '배우3': actors[2]
        
    }
    answer.append(result)
# with open('lunch.csv', 'w') as f:
#     field = ('상호명', '전화번호')
#     writer = csv.DictWriter(f, fieldnames = field) #필드네임(튜플)"""
#     writer.writeheader()
#     for l in lunch2:
#         writer.writerow(l)

with open('movie.csv', 'w') as f:
    field = ('영화코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '개봉연도', '상영시간','장르','감독명','관람등급','배우1','배우2','배우3')
    writer = csv.DictWriter(f, fieldnames = field)
    writer.writeheader()
    for i in answer:
        writer.writerow(i)