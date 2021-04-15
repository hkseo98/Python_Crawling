# Section06-1
# Selenium
# Selenium 사용 실습(1) - 설정 및 기본 테스트
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# selenium
from selenium import webdriver

# webdriver 설정(크롬, 파이어폭스 등)
browser = webdriver.Chrome('./chromedriver')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 속성 확인
# print(dir(browser))

# 브라우저 사이즈
browser.set_window_rect(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용 출력 - 자바스크립트 언어도 실행된 상태입 - 이때까지 얻을 수 없던 정보도 포함.
# print('Page Contents: {}'.format(browser.page_source))
# print()

# 세션 값 출력
print('Session Id: {}'.format(browser.session_id))

# 타이틀 출력
print('Title: {}'.format(browser.title))

# 현재 url 출력
print('URL: {}'.format(browser.current_url))

# 현재 쿠키 정보 출력
print('Cookies: {}'.format(browser.get_cookies()))

# 검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('라쿤')

# 검색(From Submit)
element.submit()

# 스크린 샷 저장 1
browser.save_screenshot('website_ch1.png')

# 스크린 샷 저장 2
# browser.get_screenshot_as_file('website_ch2.png')

# 브라우저 종료
browser.quit()