"""
heapq를 이용한 dijikstra를 구현하여 문제를 풀었음

처음에는 heapq의 사용 없이 그냥 구현하였는데 시간 초과가 났음
heapq가 아니라 BFS 방식으로 진행하게 되니까 더 확인하는 부분이 있게 되어 시간 초과가 나는 것 같음
게다가 다익스트라 자체가 시작점부터의 거리를 고려하여 우선순위를 정해야하는데
그냥 queue를 이용하면 순서를 정하는 데에도 연산이 필요하므로 heapq를 사용해야함

다익스트라에서 heapq를 사용해야한다는 것을 모른다면 풀 수 없는 문제

[문제의 이해를 돕고 다익스트라를 사용하는 방법에 대해 자세하게 다루는 글](https://www.acmicpc.net/board/view/34516)
"""
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = float('INF')
nodes = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
dist = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append((v, w))
    
dist[K] = 0
heap = []
heapq.heappush(heap, (0, K))
while heap:
    cur_dist, cur = heapq.heappop(heap)
    if visited[cur]:
        continue
    visited[cur] = 1
    for next, next_dist in nodes[cur]:
        if visited[next]:
            continue
        if dist[next] > cur_dist + next_dist:
            dist[next] = cur_dist + next_dist
            heapq.heappush(heap, (cur_dist+ next_dist, next))

for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])