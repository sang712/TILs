"""
입력의 크기가 크지 않기 때문에 while문에서 비교를 할 때마다 리스트 정렬을 하여 풀이하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
dasom = int(input())

candidates = []
for _ in range(N - 1):
    candidates.append(int(input()))

bribed = 0
while candidates:
    candidates.sort()
    if dasom > candidates[-1]:
        break
    else:
        dasom += 1
        bribed += 1
        candidates[-1] -= 1
print(bribed)