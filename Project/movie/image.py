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
with open('movie_naver.csv', newline = '') as f:
    reader = csv.reader(f)
    for row in reader:
        data[row[0]] = row[1]
del data['영화코드']
print(data)

for img in data:
    with open('images/{}.jpg'.format(img), 'wb') as f3:
        imgdata = requests.get(data[img]).content
        f3.write(imgdata)

