# Section04-1
# Requests
# Requests 사용 스크랩핑(1) - Session

import requests
import fake_useragent
# 세션 활성화
s = requests.session()
# 쿠키 Return
r = s.get('https://httpbin.org/cookies', cookies={'name': 'Seo'})

# 수신 데이터
# 전송한 쿠키 정보를 서버가 받아서 그대로 리턴해줌.
# print(r.text)

# 수신 상태
# print('Status Code: {}'.format(r.status_code))
# print('Ok?: {}'.format(r.ok)) # ok 구문은 주로 조건문에서 사용

# 쿠키 set
r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'Seo2'})
# print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent': str(fake_useragent.UserAgent), 'cookie': 'Seo2'}

# 헤더 정보 전송
# r3 = s.get(url, headers=headers)
# print(r3.text)





# 세션 비활성화
s.close()

# with문 사용 권장! -> 파일, DB, HTTP
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)
