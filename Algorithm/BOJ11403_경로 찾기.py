"""
플로이드-워셜 알고리즘을 적용하면 쉽게 풀 수 있는 문제이기 때문에 해당 알고리즘을 적용하였음
그대로 적용하기엔 문제가 조금 달라서 응용을 하였음
기존의 플로이드-워셜 알고리즘대로 k - i - j 순으로 for문을 돌리되 
i -> j 가 1이면 넘어가고 0일 때만 i -> k, k -> j 가 모두 1인지 확인하도록 함
"""
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                continue
            elif graph[i][k] and graph[k][j]:
                graph[i][j] = 1
            
for row in graph:
    print(*row)
    
# 경로찾기 문제 끝나면 사다리 조작 문제 풀기