from bs4 import BeautifulSoup
import json
import requests
import os
import datetime
import csv
import sys

client_secret = os.getenv("KEY_NAVER")
client_id = os.getenv("ID_NAVER")

header = {
    'X-Naver-Client-Id' : client_id,
    'X-Naver-Client-Secret' : client_secret
}

data = {}
with open('movie.csv', newline = '') as f:
    reader = csv.reader(f)
    for row in reader:
        data[row[1]] = row[0]
del data['영화명(국문)']
#print(data)

answer = []
result = {}

for n in data: #key
    url = 'https://openapi.naver.com/v1/search/movie.json?'
    search = 'query={}'.format(n)
    res = requests.get(url + search, headers = header)
    doc = res.json().get('items')
    #result = [data[n], doc[0].get('image'), doc[0].get('link'), doc[0].get('userRating')]
    result = {
        '영화코드': data[n],
        '썸네일URL': doc[0].get('image'),
        '링크URL': doc[0].get('link'),
        '평점': doc[0].get('userRating')
    }
    answer.append(result)

    
with open('movie_naver.csv', 'w') as f:
    field = ('영화코드', '썸네일URL', '링크URL', '평점')
    writer = csv.DictWriter(f, fieldnames = field)
    writer.writeheader()
    for a in answer:
        writer.writerow(a)

"""
영화별로 다음과 같은 내용을 저장합니다. 영진위 영화 대표코드 , 영화 썸네일 이미지의 URL , 하
이퍼텍스트 link , 유저 평점
해당 결과를 movie_naver.csv에 저장합니다.
"""


        

# image	string	검색 결과 영화의 썸네일 이미지의 URL이다. 이미지가 있는 경우만 나타난다.
# link	string	검색 결과 영화의 하이퍼텍스트 link를 나타낸다.
# userRating	integer	검색 결과 영화에 대한 유저들의 평점이다.