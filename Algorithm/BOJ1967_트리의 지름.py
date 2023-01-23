"""
처음 접하는 내용이다보니 검색을 통해 개념과 구현하는 방법을 찾아봄
임의의 한 노드에서 시작하여 가장 먼 노드를 찾고
그 노드로부터 가장 먼 다른 노드를 찾으면 이 두 노드가 지름의 양 끝 점이라고 함

BFS로 가장 먼 노드를 찾도록 구현하였음
DFS를 써도 되지만 어차피 어느 부분이 가장 먼 노드인지 알기 위해선 완전탐색을 해야하기 때문에 별 차이가 없다고 생각했고
DFS를 사용하면 RecursionError가 날 수 있다고 생각했기 때문에 안전하게 BFS를 선택함

BFS는 가장 먼 노드와 해당 노드까지의 거리를 반환하도록 구현하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))
    
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    furthest = (start, 0)
    while q:
        curr, cost = q.popleft()
        if cost > furthest[1]:
            furthest = (curr, cost)
        for next, next_cost in tree[curr]:
            if not visited[next]:
                q.append((next, cost + next_cost))
                visited[next] = 1
    return furthest

one_end, _ = bfs(1)
other_end, diameter = bfs(one_end)
print(diameter)
