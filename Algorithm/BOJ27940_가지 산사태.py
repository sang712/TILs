"""
첫 층은 모든 비를 맞기 때문에 무조건 첫 층부터 무너질 수밖에 없음
따라서 굳이 구획할 필요없이 한 변수에 강수량을 모두 더해 조건을 판단하였음
입력을 끝까지 다 안 받으면 1032ms가 걸리고
입력을 중간에 안 받으면 800ms가 걸림
그런데 입력을 다 받지 않는 다는 것은 코드가 종료된 이후에 문제가 발생할 여지가 있다고 생각함
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
# floors = [0] * (N+1)
# rains = [tuple(map(int, input().split())) for _ in range(M)]
precipitation = 0
for i in range(M):
    _, rain = map(int, input().split())
    precipitation += rain
    if precipitation > K:
        print(i+1, 1)
        break
else:
    print(-1)
