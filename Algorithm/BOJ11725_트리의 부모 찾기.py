'''
오래전에 풀었지만 기록에 남지 않은 문제를 풀었다
당시에는 bfs를 이용하여 풀었는데 많은 시간을 소요하는 pop(0)를 사용하고 있어서 시간 초과가 났고, 
pypy3로 제출하여 통과를 하였다
해당 코드의 input을 readline으로 받고, deque의 popleft를 사용하도록 수정하고 제출하니 
python3에서도 348ms정도로 적은 시간이 소요되었다
근데 str()로 저장하고 '\n'.join()으로 출력을 하면 빠를 줄 알았는데 그게 아닌가 보다
356ms로 약 8ms가 더 소요되었다

dfs는 312ms가 소요되었다
str()로 저장하고 '\n'.join()으로 출력을 하는 방법을 사용하였더니 324ms가 소요되었다

문제를 반복해서 풀 수록 상대적으로 오랜 시간이 걸리는 문제가 있나보다?
'''
# bfs 풀이
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
my_gragh = [[] for _ in range(N+1)]

# 서로 연결되어 있는 노드로 그래프를 구성함
for _ in range(N-1):
    N1, N2 = list(map(int, input().split()))
    my_gragh[N1].append(N2)
    my_gragh[N2].append(N1)


ans = [0]*(N+1)
visited = [0 for _ in range(N+1)]

# 큐에 담아서 bfs로 부모 노드 파악
q = deque([1])
while q:
    parent = q.popleft()
    for i in my_gragh[parent]:
        if not visited[i]:
            ans[i] = parent
            q.append(i)
            visited[i] = 1

# 부모노드 출력
for i in range(2, N+1):
    print(ans[i])

'''
# dfs 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
edges = [[] for _ in range(N+1)]
parent = [0] * (N+1)
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

def dfs(parent_node):
    for node in edges[parent_node]:
        if not parent[node]:
            parent[node] = str(parent_node)
            dfs(node)
dfs(1)
print('\n'.join(parent[2:]))
'''