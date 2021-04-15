# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
    <title>yoyoyoyoyoo</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>yoyoyoyoyo!!!!</b></p>
        <p class="story">yoyoooyoooooyoooyoo
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-test="test" data-io="link3" href="http://example.com/elsie" class="brother" id="link3">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>


"""

# 예제 1(bs4기초)

soup = BeautifulSoup(html, 'html.parser')
# 타입 확인
print('soup', type(soup))
# 예쁘게 출력
print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# body 안에 p 태그가 3개가 있는데 맨 처음 것을 갖고 온다는 것을 확인할 수 있다.
p1 = soup.html.body.p
print('p1', p1)

# 다음 태그
# next_sibling.next_sibling - 다음 p 태그 나옴.
# next_sibling.next_sibling() 괄호 붙이면 리스트 안에 담아서 줌, 안붙이면 그냥 그대로 나옴.
# next_sibling을 두번 호출한 이유는 한번 호출하면 첫 번째 p태그 안에 있는 b태그가 나오는데, 이건 그냥 텍스트임 - 텍스트는 출력 안 함. 그냥 한 칸 이동하려면 두번 호출 해야 됨
p2 = p1.next_sibling.next_sibling
print('p2', p2)

p3 = p1.next_sibling.next_sibling.next_sibling.next_sibling # 별로 효율적인 코드는 아님..
print('p3', p3)

# 텍스트 출력1 - string - 태그 안에 있는 텍스트만 출력해줌.
print('h1 >>', h1.string)
# 텍스트 출력2 - b 태그 무시함.
print('p>>', p1.string)

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element))

# 반복 출력 확인
# for v in p2.next_element:
    # print(v)


# 예제2(Find, Find_all)
soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
link1 = soup.find_all('a', limit=3)  # limit 옵션으로 가져올 개수 제한 가능
# print(type(link1))
print(link1)

# 중요! - 태그 이외의 속성, 태그 하위의 스트링 문자열로도 자료를 가져울 수 있다.
link2 = soup.find_all('a', string=["Elsie", "Title"]) # id='link2', string='title', class_='sister', 리스트로 여러개 갖고 오는 것도 가능
print(link2)

for t in link2:
    print(t)

# 처음 발견한 a 태그 선택 - fine() - 맨 처음 발견한 1개만 가져옴.
link3 = soup.find('a')
print()
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건
link4 = soup.find('a', {'class': 'brother', 'data-io': 'link3'})
print()
print(link4)
print(link4.string)
print(link4.text)

# 예제3(select, select_one)
# 가장 많이 나오는 질문! 언제 select를 쓰고 언제 find를 써요?
# CSS 선택자 : select, select_one
# 태그로 접근 : find, find_all

# 태그 + 클래스 + 자식 선택자
# . = 클래스 선택자
link5 = soup.select_one('p.title > b')
print()
print(link5.text)
print(link5.string)

# # = 아이디 선택자
link6 = soup.select_one('a#link1')
print()
print(link6.text)
print(link6.string)

# 대괄호[]로 감싸면 임의로 지정한 속성값에 대해서도 선택할 수 있다.
# . - 클래스, # - id, 이와의 것들은 모두 []로 묶어서 접근을 해야 한다.!!!!!
link7 = soup.select_one('a[data-test="test"]')
print()
print(link7.text)
print(link7.string)

# 선택자에 맞는 전체 선택 - select
link8 = soup.select('p.story > a')
print()
for v in link8:
    print(v)


link9 = soup.select('p.story > a:nth-of-type(3)') # p 태그 story 클래스 하위의 a 태그들 중에서 3번째 녀석을 가져와라.
print()
print(link9)


link10 = soup.select('p.story')
print()
print(link10)

print()
for t in link10:
    temp = t.find_all('a')
    if temp:
        for v in temp:
            print('>>>>>', v.string)
    else:
        print('-----', t.text)


