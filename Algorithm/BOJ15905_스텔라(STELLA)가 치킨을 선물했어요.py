"""
정렬을 하여 인덱스가 5이상인 참가자 중에 문제를 맞춘 수가 
인덱스가 4인 참가자와 같은 경우만 카운트하여 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

candidates = []
for _ in range(N):
    candidates.append(tuple(map(int, input().split())))
candidates.sort(key=lambda x: (-x[0], x[1]))

ans = 0
for i in range(5, N):
    if candidates[i][0] == candidates[4][0]:
        ans += 1
    else:
        break
print(ans)