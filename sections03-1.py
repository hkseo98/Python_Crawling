# Section03-1
# 기본 스크랩핑 실습
# GET 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러 정보
print('type: {}'.format(type(mem)))
print('get url: {}'.format(mem.geturl()))
print('status: {}'.format(mem.status))
print('header: {}'.format(mem.getheaders()))
print('get code: {}'.format(mem.getcode()))
print('read: {}'.format(mem.read(100).decode('utf-8').strip()))  # read()의 인자로는 읽어올 바이트 수가 들어간다.
print('parse: {}'.format(urlparse('http://www.encar.co.kr?test=test').query))


# 기본 요청2(ipify - api 테스트용 사이트)
API = "https://api.ipify.org"

# GET 방식 Parameter
values = {
    'format': 'jsonp'
}

print('before param: {}'.format(values))
param = urllib.parse.urlencode(values)
print('after param: {}'.format(param))

# 요청 URL 생성
URL = API + "?" + param
print("요청 URL = {}".format(URL))

values2 = {
    'format': 'text'
}
param2 = urllib.parse.urlencode(values2)
URL2 = API + '?' + param2
print("요청 URL2 = {}".format(URL2))  # 포멧에 따라 나타나는 ip 주소 형태가 달라짐.

data = urllib.request.urlopen(URL).read()

text = data.decode('UTF-8')
print('response: {}'.format(text))

# format = json, text, jsonp 등등 다양하게 실험해보기.
# 스크랩핑 - 요청하고 수신해서 원하는 데이터가 왔는지 확인하는 것.