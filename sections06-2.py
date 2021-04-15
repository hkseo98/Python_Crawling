# Section06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# selenium
from selenium import webdriver
import time
# By = 언제까지 기다릴 때
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 크롭 브라우저를 실행하지 않고 내부적으로 실행하도록 하는 방법!
chrome_options = Options()
chrome_options.add_argument("--headless") # 헤드리스 모드! 리소스 절약에 매우 유용

# webdriver 설정(chrome 등) - Headless 모드
browser = webdriver.Chrome('./chromedriver', options=chrome_options)

# webdriver 설정(chrome 등) - 일반 모드
# browser = webdriver.Chrome('./chromedriver')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(500)

# 브라우저 사이즈
browser.set_window_size(1300, 1000)

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 제조사별 더보기 클릭
# Explicitly wait

# 모든 요소가 자기 자리를 찾을 때까지 기다려라! 그리고 그 전에 나타나면 클릭해라!
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭2
# implicitly wait
# time.sleep(2) # 무조건 2초 기다려야 됨 - 위에 것을 더 많이 씀.!
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label'))).click()

# 페이지 내용 확인
# print(browser.page_source)

time.sleep(1)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 소스 코드 정리
# print(soup.prettify())

# 메인 상품 리스트 선택
pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

# 상품 리스트 확인
# print(pro_list)

# 필요 정보 추출
for v in pro_list:
    # print(v)
    print('\n\n')
    if not v.find('div', class_='ad_header'):
        # 상품명, 이미지, 가격
        if 'APPLE' in v.select('p.prod_name > a')[0].text.strip():
            print(v.select('p.prod_name > a')[0].text.strip())
            temp = str(v.select_one('a.thumb_link > img')).split('al="')
            for i in temp:
                if 'jpg?' in i:
                    temp2 = i.split('src="')
                    for j in temp2:
                        if 'jpg?' in j:
                            print('http:' + j)
            print(v.select('p.price_sect > a')[0].text.strip())

        print()



