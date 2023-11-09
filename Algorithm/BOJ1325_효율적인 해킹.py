"""
그래프 탐색을 하면서 몇개의 그래프를 방문했는지 저장하는 방법으로 하려고 했음
대신 서로를 가리키는 그래프일 경우 무한 반복을 할 가능성이 있어 이 부분을 해결해야함

그냥 N번 반복문을 돌면서 시작점부터 끝까지 돌면서 방문하는 지점을 카운트 한 뒤에 저장하는 방식으로 풀었음

사이클이 되는 부분을 따로 저장해서 처리하려고 했는데
사이클이 여러번 중복되는 노드를 처리하기 어려워서 그냥 제출하였음
pypy3 제출 시 13000ms 소요됨
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [{} for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[j][i] = 1
    
counter = [0] * (N + 1)
is_cycle = [0] * (N + 1)

for start in range(1, N + 1):
    visited = [0] * (N + 1)
    if not visited[start]:
        visited[start] = 1
        q = [start]
        cnt = 1
        while q:
            i = q.pop()
            for j in graph[i].keys():
                if not visited[j]:
                    visited[j] = 1
                    cnt += 1
                    q.append(j)
        counter[start] = cnt
ans = []
max_value = 0
for idx, value in sorted(enumerate(counter), key=lambda x: (-x[1], x[0])):
    if value > max_value:
        ans = [idx]
        max_value = value
    elif value == max_value:
        ans.append(idx)
    else:
        break
print(*ans)