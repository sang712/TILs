'''
주어진 카드를 딕셔너리에 넣어 카운트하여 풀었음
카드를 호출할 때 없는 카드를 고려하여 setdefault 함수를 추가하였음
'''
N = int(input())
cards = list(map(int, input().split()))

cardnumbers = dict()
for number in cards:
  cardnumbers.setdefault(number, 0)
  cardnumbers[number] += 1

M = int(input())
cases = list(map(int, input().split()))
ans = ''
for case in cases:
  cardnumbers.setdefault(case, 0)
  ans += str(cardnumbers[case]) + ' '
print(ans.strip())
