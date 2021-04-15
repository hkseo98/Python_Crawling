# section02-4
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)
# pip install lxml, requests, cssselect
# session 이용하기
# xpath 이용하기
# 신문사 이름과 신문사 링크 딕셔너리로 크롤링

import requests
from lxml.html import fromstring, tostring


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get("https://www.naver.com")  # api에 맞게 get도 있고 post도 있다. 보안이 필요한 곳에는 post 써주기.

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for name, url in urls.items():
        print(name, url)


def scrape_news_list_page(response):
    # url 딕셔너 선언
    urls = {}

    # 태그 정보 문자열 저장
    root = fromstring(response.content)  # content = 바이너리 파일 로드

    for a in root.xpath('//div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'):
        name, url = extract_contents(a)
        urls[name] = url
    return urls


def extract_contents(dom):
    # 링크 주소
    # ./는 ~의 현재 넘어온 태그의 자식 태그라는 의미
    link = dom.xpath('./div[@class="popup_wrap"]/a[@class="btn_popup"]')[0].get('href')
    # 신문사 명
    name = dom.xpath('./a[@class="thumb"]/img[@class="news_logo"]')[0].get('alt')
    return name, link


if __name__ == '__main__':
    main()


