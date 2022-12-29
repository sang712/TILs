'''
정점의 개수가 1000개이다보니 N * N인 2차원 간선의 정보를 저장했는데 빠르게 끝낸 코드를 확인해보니
4배까지도 빨라서 찾아봤더니 각 노드별로 해당 간선의 정보만 append방식으로 넣고 for문을 돌릴 때 sort를 하여 돌리는 방식으로 하였음
나는 sort를 N번 돌리는게 더 느릴 거 같다고 생각했는데 테스트 케이스의 크기가 그렇게 크진 않나봄 
deque를 쓰지 않아도 느리지 않은 것을 보면
생각해보니 정점의 개수가 1000개이고 간선의 개수가 10000개라서 
999000/2(양방향) 개의 가능성의 간선 중에서 최대 10000개이므로 위의 방식으로 해도 됐겠구나 싶음
200ms -> 80ms로 줄일 수 있었음
'''
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M, V = map(int, input().split())

# graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# for _ in range(M):
#     node1, node2 = map(int, input().split())
#     graph[node1][node2] = 1
#     graph[node2][node1] = 1
    
# visited = [0] * (N + 1)
# dfs_order = []
# def dfs(n):
#     if visited[n]:
#         return
#     visited[n] = 1
#     dfs_order.append(n)
#     for i in range(1, N + 1):
#         if graph[n][i]:
#             dfs(i)
# dfs(V)

# visited = [0] * (N + 1)            
# stack = deque([V])
# bfs_order = []
# def bfs():
#     while stack:
#         n = stack.popleft()
#         if visited[n]:
#             continue
#         visited[n] = 1
#         bfs_order.append(n)
#         for i in range(1, N + 1):
#             if graph[n][i]:
#                 stack.append(i)
# bfs()
# print(*dfs_order)
# print(*bfs_order)
import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
visited = [0] * (N + 1)
dfs_order = []
def dfs(n):
    if visited[n]:
        return
    visited[n] = 1
    dfs_order.append(n)
    for i in sorted(graph[n]):
        if graph[i]:
            dfs(i)
dfs(V)

visited = [0] * (N + 1)            
stack = deque([V])
bfs_order = []
def bfs():
    while stack:
        n = stack.popleft()
        if visited[n]:
            continue
        visited[n] = 1
        bfs_order.append(n)
        for i in sorted(graph[n]):
            if graph[i]:
                stack.append(i)
bfs()
print(*dfs_order)
print(*bfs_order)
