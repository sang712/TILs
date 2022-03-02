'''
다른 답(1)
파이썬에는 정규 표현식을 사용할 수 있게 변환해주는 모듈 re 가 있다
import re
pattern = re.compile('[a-z]+')
와 같이 정의하여 사용할 수 있다
'''
'''
다른 답(2)
혹은 startswith, endswith 함수를 사용하여 비교할 수도 있다.
'''

N = int(input())
former, latter = input().split('*')
for _ in range(N):
    output = "DA"
    word = input()
    if len(word) < len(former) + len(latter):
        output = "NE"
    if output == "NE":
        print(output)
        continue

    for i in range(len(former)):
        if word[i] == former[i]:
            continue
        else:
            output = "NE"
            break
    if output == "NE":
        print(output)
        continue

    for i in range(len(latter)):
        if word[len(word) -1 -i] == latter[len(latter) -1 -i]:
            continue
        else:
            output = "NE"
            break
    if output == "NE":
        print(output)
        continue
    print(output)