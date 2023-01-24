"""
어제 풀었던 동명의 문제 1967번 트리의 지름 문제와 같은 문제
다른 점은 문제의 입력 방식이 다르다는 것

처음에는 list자료 구조를 이용하여 for문으로 들어오는 순서대로 입력을 받아 저장했는데
정점이 번호 순서대로 입력이 된다는 보장이 없기 때문에 이 사실을 인지하지 못 해 여러번 틀렸음

해당 사실을 알고 list를 dict자료구조로 수정하였고 몇 번 더 틀린 뒤에
for문에서 받았던 정점 번호를 무시하고 입력으로 받은 값을 사용하도록 수정한 뒤에야 정답을 받을 수 있었음
"""

import sys
from collections import deque
input = sys.stdin.readline

V = int(input())

edges = dict()
for _ in range(V):
    edge_info = list(map(int, input().split()))
    idx = 1
    while True:
        start = edge_info[0]
        try:
            end, cost = edge_info[idx:idx+2]
            edges.setdefault(start, [])
            edges[start].append((end, cost))
            idx += 2
        except ValueError:
            break

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0 for _ in range(V + 1)]
    visited[start] = 1
    furthest = (start, 0)
    while q:
        curr, cost = q.popleft()
        if cost > furthest[1]:
            furthest = (curr, cost)
        for next, next_cost in edges[curr]:
            if not visited[next]:
                q.append((next, next_cost + cost))
                visited[next] = 1
    return furthest

one_end, _ = bfs(V//2)
other_end, diameter = bfs(one_end)
print(diameter)