"""
플로이드 워셜 문제임을 파악 하고 공부한 뒤 구현하였음
플로이드 워셜은 각 정점간의 이동거리를 간선 자체로 사용하는 것이 아니라
2차원의 배열을 통해 모든 정점간의 이동거리를 표현하여 사용한다는 특징이 있음
그렇게 해서 순차적으로 하나의 정점을 선택해 
그 정점을 지나칠 때과 해당 정점을 지나치지 않았을 때를 비교하여 이동거리가 짧은 것을 택하는 방식을 취함

플로이드-워셜 알고리즘을 구현하고 제출을 하였더니 98%에서 틀렸고 
문제에서 제시한 조건을 맞추지 않아서 오답이 되었던 것임
마지막 출력에서 INF인지 확인하고 출력하도록 함
"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float('inf')

edges = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a][b] = min(edges[a][b], c)

for k in range(1, n + 1):
    edges[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])
            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(edges[i][j] if edges[i][j] < INF else 0, end=' ')
    print()
    
"""
# 첫 반례
입력
50
1 2 1
오답
0 1 inf inf inf inf ...
정답
0 1 0 0 0 0 ...
"""