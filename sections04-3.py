# Section04-3
# Requests
# Requests 사용 스크랩핑(3) - REST API

# REST API : GET, POST, DELETE, PUT(update), REPLACE(FETCH : UPDATE, MODIFY)
# 중요: URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET:  ...../movies: 영화를 전부 조회
# GET: ...../movies/:id : 아이디인 영화를 조회
# POST: ...../movies/ : 영화를 생성
# PUT: ...../movies/ : 영화를 수정
# DELETE: ...../movies/ : 영화를 삭제


import requests
from requests import cookies

# 세션 활성화
s = requests.session()

# 예제 1
r = s.get('https://api.github.com/events')

# 수신 상태 체크 -r.raise_for_status() - 에러 발생하면 종료
r.raise_for_status()

# print(r.text)

# 예제2
# 쿠키 설정(정석) jar 사용
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입
jar.set('name', 'niceman', domain="httpbin.org", path='/cookies')

# 요청
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
# print(r.text)

# 예제 3
r = s.get('https://github.com', timeout=5000000)
# 출력
# print(r.text)

# 예제 4 - Post
r = s.post('http://httpbin.org/post', data={'id': 'test77', 'pw': '111'}, cookies=jar)
# print(r.text)
# print(r.headers) # connection이 keep-alive인 이유 - 세션을 사용했고 쿠키도 보냈기 때문에 연결이 유지된다.

# 예제 5
# 요청(POST)
payload1 = {'id': 'test77', 'pw': '111'}
payload2 = (('id', 'test77455'), ('pw', '1434t11')) # 튜플 형태로도 가능

# r = s.post('http://httpbin.org/post', data=payload2)
# print(r.text)

# 예제 6(PUT)
# r = s.put('http://httpbin.org/put', data=payload1)
# print(r.text)

# 예제 7(DELETE)
# r = s.delete('http://httpbin.org/delete', data={'id': 1}) # id가 1인 자료를 삭제해 달라는 의미.
# print(r.text)

# 예제 8(DELETE)
r = s.delete('https://jsonplaceholder.typicode.com/posts/1') # post1 삭제
print(r.ok)
print(r.text)
print(r.headers)
s.close()