'''
방향이 없는 그래프 이므로 양 방향의 정보를 담는 2차원 리스트를 만들고
visited 리스트를 이용해 체크하면서 stack을 이용하는 dfs를 구현하였음
매 연결 요소를 찾을 때 dfs 함수를 호출하였음

dfs 함수 내부에서 함수를 굳이 호출하지 않아도 될 것 같아서 시도해 봄
시도 성공 
함수 내부에서 함수를 호출할 경우 recursionlimit을 고려해야 하는데 그럴 필요도 없어졌고
868ms 에서 812ms로 줄일 수 있었음
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nodes = [[] for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    nodes[node1].append(node2)
    nodes[node2].append(node1)
    
visited = [0] * (N + 1)

def find_connected_component_from(node):
    visited[node] = 1
    stack = [] + nodes[node]
    while stack:
        next_node = stack.pop()
        if not visited[next_node]:
            # find_connected_component_from(next_node)
            visited[next_node] = 1
            stack += nodes[next_node]

cnt = 0
for node in range(1, N+1):
    if not visited[node]:
        cnt += 1
        find_connected_component_from(node)
        
print(cnt)