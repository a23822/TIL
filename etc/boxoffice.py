from bs4 import BeautifulSoup
import json
import requests
import os
import datetime
import csv

key = os.getenv("KEY_MOV")
lastDay = datetime.datetime(2019, 1, 13)

period = [lastDay.strftime('%Y%m%d')] # 조회기간
for i in range(10):
    day = lastDay - datetime.timedelta(days = 7*i)
    period.append(day.strftime('%Y%m%d'))


url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=" + key
result = {}

for p in period:
    params = {
        'weekGb' : 0,
        'targetDt' : p
    }

    res = requests.get(url, params = params).text
    doc = json.loads(res)
    #print(doc)
    temp = doc['boxOfficeResult']["weeklyBoxOfficeList"]
    for j in temp:
        result[j['movieNm']] = [j['movieCd'], j['audiAcc'], p]
    #print(result)
    answer = []
    for i in result.keys():
      answer.append({
          '영화코드' : result[i][0],
          '영화이름' : i,
          '누적 관객 수' : result[i][1],
          '해당일' : result[i][2]
      })


with open('boxoffice.csv', 'w') as f:
    field = ('영화코드', '영화이름', '누적 관객 수', '해당일')
    writer = csv.DictWriter(f, fieldnames = field)
    writer.writeheader()
    for i in answer:
        writer.writerow(i)