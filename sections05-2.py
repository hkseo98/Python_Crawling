# Section05-2
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(2) - 이미지 다운로드

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import shutil


# 헤더 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
# 헤더 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자 도구)
base = 'https://www.daum.net/?nil_profile=daum&nil_src=search'
# 검색어
quote = rep.quote_plus('호랑이')
# URL 완성
url = base

# 요청 URL 확인
print(url)

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = 'tiger'
# 폴더 비우기. - 파일 있을 때
shutil.rmtree(savePath)
# 폴더 생성 예외 처리(문제 발생 시 프로그램 종료)
try:
    # 기존에 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    print('folder creation failed')
    print('folder name: {}'.format(e.filename))
    # 런타임에러
    raise RuntimeError('System Exit!')
else:
    print('folder is created')

# bs4 초기화
soup = BeautifulSoup(res, 'html.parser')


# select 사용
img_list = soup.select('span.thumb_g > img')
# print(img_list)


for i, v in enumerate(img_list, 1):
    print(i, v)
    fileName = os.path.join(savePath, savePath + str(i) + '.png')
    temp_url = str(v).split('?fname=')[1]
    temp_url2 = temp_url.split('"')[0]
    print(temp_url2)
    req.urlretrieve(temp_url2, fileName)

