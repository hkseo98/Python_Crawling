# Section04-2
# Requests
# Requests 사용 스크랩핑(2) - JSON

import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청
r = s.get('https://httpbin.org/stream/100', stream=True)

# 수식 확인
# print(r.text)

# Encoding 확인
if r.encoding is None:
    r.encoding = 'UTF-8'
# print('Encoding: {}'.format(r.encoding))

# 라인별 출력, decode_unicode=True는 혹시 모를 캐릭터 세트에 의해 텍스트가 깨지는 걸 방지하기 위함
for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    # JSON(Dict) 변환 후 타입 확인
    b = json.loads(line) # str -> dict
    # print(b)
    # print(type(b))

    # 정보 내용 출력
    # for k, v in b.items():
    #     print('key: {}, value: {}'.format(k, v))
    #
    # print()
    # print()

s.close()

# https://jsonplaceholder.typicode.com/를 통한 실습
r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# 헤더 정보 -> json 형식 확인
# print(r.headers)
#
# # 본문 정보
# print(r.text)
#
# # json 변환
# print(r.json())
#
# # key 반환
# print(r.json().keys())
#
# # 값 반환
# print(r.json().values())
#
# print(r.encoding)
#
# # 바이너리 정보
# print(r.content)
s.close()

r1 = s.get('https://jsonplaceholder.typicode.com/posts', stream=True)
b = json.loads(r1.text)
for line in b:
    for k, v in line.items():
        print('key: {}, value: {}'.format(k, v))
    print()
    print()