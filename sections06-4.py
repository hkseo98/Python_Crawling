# Section06-4
# Selenium
# Selenium 사용 실습(4) - 실습 프로젝트(3) -엑셀 저장
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
# 엑셀 처리 임포트
import xlsxwriter
# 이미지 바이트 처리
from io import BytesIO
import urllib.request as req
from fake_useragent import UserAgent

# 엑셀 처리 선언
workbook = xlsxwriter.Workbook('./macbook_crawling.xlsx')

# 워크 시트
worksheet = workbook.add_worksheet()

# 크롭 브라우저를 실행하지 않고 내부적으로 실행하도록 하는 방법!
chrome_options = Options()
# chrome_options.add_argument("--headless") # 헤드리스 모드! 리소스 절약에 매우 유용
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
chrome_options.add_argument("referer=http://prod.danawa.com/list/?cate=112758&15main_11_02")

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

time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링 페이지 수
target_crawl_num = 5

# 엑셀 행 수
ins_cnt = 1

while cur_page <= target_crawl_num:
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스 코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('************************** Current Page: {}'.format(cur_page), '*****************************')
    print()

    # 필요 정보 추출
    for v in pro_list:
        if not v.find('div', class_='ad_header'):
            # 상품명, 이미지, 가격
            if 'APPLE' in v.select('p.prod_name > a')[0].text.strip():
                prod_name = v.select('p.prod_name > a')[0].text.strip()
                temp = str(v.select_one('a.thumb_link > img')).split('al="')
                for i in temp:
                    if 'jpg?' in i:
                        temp2 = i.split('src="')
                        for j in temp2:
                            if 'jpg?' in j:
                                prod_image = 'http:' + j.split('"')[0]
                                break
                prod_price = v.select('p.price_sect > a')[0].text.strip()

                # 엑셀 저장(텍스트)
                worksheet.write('A%s'%ins_cnt, prod_name)
                worksheet.write('B%s'%ins_cnt, prod_price)
                worksheet.write('C%s'%ins_cnt, prod_image)


                # 엑셀 저장(이미지) -  두 번째 매개변수로 이미지의 이름을 받는다. - 403에러로 인해 실패.. 이미지 url이 오픈이 안된다..
                # worksheet.insert_image('C%s'%ins_cnt, {'image_data': img_data})

                ins_cnt += 1




    # 페이지 별 스크린 샷 저장
    browser.save_screenshot('./target_page{}.png'.format(cur_page))

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawlung Succeed')
        break

    # 페이지 이동 클릭
    WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # BeutifulSoup 인스턴스 삭제
    del soup

    # 3초간 대기
    time.sleep(3)

browser.close()

# 엑셀 파일 닫기 - 이래야 저장이 됨
workbook.close()

