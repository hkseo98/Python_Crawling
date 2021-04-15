# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기
# pip install fake-useragent

import json
import urllib.request as req
from fake_useragent import UserAgent
from openpyxl import Workbook

# Fake Header 정보(가상으로 User-agent 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# 헤더 정보
headers = {
    'User-Agent': ua.ie,
    'Referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# 응답 데이터 확인(Json Data)
# print(res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']
# print(rank_json)

write = Workbook()
write1 = write.create_sheet('rank.xlsx')
for elm in rank_json:
    # print(type(elm))
    print('순위: {}, 금액: {}, 회사명: {}'.format(elm['rank'], elm.get('tradePrice'), elm['name']))
    write1.append(['순위: {}, 금액: {}, 회사명: {}'.format(elm['rank'], elm.get('tradePrice'), elm['name'])])
write.save('rank.xlsx')