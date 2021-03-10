# Section05-3
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(3) - 로그인 처리

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 로그인 정보(개발자 도구)
login_info = {
    'redirectUrl': 'http://www.danawa.com/?src=adwords&kw=GA0000020&gclid=Cj0KCQiA1pyCBhCtARIsAHaY_5f5fwgnLp5-t_u-LmT5Iyp3vfyV1rq0E_s-WnWyL136U48-tD2SqgoaAqwqEALw_wcB',
    'loginMemberType': 'general',
    'id': 'hkseo73',
    'password': 'digital73@'
}

# 헤더 정보
headers = {
    'User-Agent': UserAgent().chrome,
    'referer': 'https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F%3Fsrc%3Dadwords%26kw%3DGA0000020%26gclid%3DCj0KCQiA1pyCBhCtARIsAHaY_5f5fwgnLp5-t_u-LmT5Iyp3vfyV1rq0E_s-WnWyL136U48-tD2SqgoaAqwqEALw_wcB'
}

with req.session() as s:
    # Request(로그인 시도) - 개발자도구에서 Request URL 복붙, 로그인정보, 헤더 정보 넣어주기.
    res = s.post('https://auth.danawa.com/login', login_info, headers=headers)

# 로그인 시도 실패 시 예외
if res.status_code != 200:
    raise Exception("Login failed")

# print(res.content.decode())

# 로그인 성공 후 ***세션 정보를 가지고 페이지 이동
res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

# 페이지 이동 후 수신 데이터 확인
# print(res.text)

# bs4 초기화
soup = BeautifulSoup(res.text, "html.parser")

# print(str(soup.find('title')))
# 로그인 확인
if '주문/배송' not in str(soup.find('title')):
    raise Exception('Login failed')


# 선택자 사용
info_list = soup.select('div.my_info > div.sub_info > ul.info_list > li')
print(info_list)

print()
print('********My Info**********')
# 필요한 텍스트 추출
for v in info_list:
    proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
    print(proc, val)