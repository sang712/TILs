"""
정렬을 해서 3번째 값만 제외하는 방식으로 풀이하였음
각각의 값을 받아서 append도 하고 더하기도 하는 것 보다
한 번에 값을 입력받고 한번에 더하기 하는 것이 더빠름
"""
import sys
input = sys.stdin.readline

N = int(input())
costs = [int(input()) for _ in range(N)]
ans = sum(costs)
costs.sort(reverse=True)
for i in range(2, N, 3):
    ans -= costs[i]
print(ans)
