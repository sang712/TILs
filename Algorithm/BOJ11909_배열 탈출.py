"""
다익스트라 알고리즘 공부하려고 해당 태그로 검색해서 푼 문제인데
파이썬만 그런지 모르겠지만 다익스트라 적용하면 heapq가 너무 무거워서 시간 초과가 나는 것 같음
그래서 검색해보니 dp로도 풀이가 가능하대서 dp로 풀이하였음

python3는 7000ms, pypy3는 980ms가 걸렸음
"""
import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

costs = [[0] * N for _ in range(N)]
Q = [(0, 0, 0)]

for i in range(1, N):
    costs[i][0] = costs[i-1][0] + max(0, array[i][0] - array[i-1][0] + 1)
    costs[0][i] = costs[0][i-1] + max(0, array[0][i] - array[0][i-1] + 1)
    
for i in range(1, N):
    for j in range(1, N):
        costs[i][j] = min(costs[i-1][j] + max(0, array[i][j] - array[i-1][j] + 1), 
                          costs[i][j-1] + max(0, array[i][j] - array[i][j-1] + 1))
print(costs[i][j])