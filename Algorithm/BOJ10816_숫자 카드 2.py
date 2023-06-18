'''
주어진 카드를 딕셔너리에 넣어 카운트하여 풀었음
카드를 호출할 때 없는 카드를 고려하여 setdefault 함수를 추가하였음

재채점으로 시간 초과가 나서
답을 출력하는 부분에서 str을 주르륵 더해 출력하는 대신
리스트에 넣어 언패킹하면서 출력하는 방식으로 수정하였음

파이썬에서 스트링 연산이 오래 걸린다는 사실을 잘 알고 있어서 왠만하면 그렇게 풀지 않지만
7달전에 제출했음을 확인하고는 왜 이렇게 풀었었나 이해하게 되었음

문제 이름도 "숫자 카드"에서 "숫자 카드 2"로 수정함
'''
N = int(input())
cards = list(map(int, input().split()))

cardnumbers = dict()
for number in cards:
  cardnumbers.setdefault(number, 0)
  cardnumbers[number] += 1

M = int(input())
cases = list(map(int, input().split()))
ans = []
for case in cases:
  cardnumbers.setdefault(case, 0)
  ans.append(cardnumbers[case])
print(*ans)