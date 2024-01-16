"""
힙 자료 구조를 사용하는 다익스트라 알고리즘을 이용해서 풀이하였음
X로 가는 경우는 그래프를 거꾸로 그려서 다익스트라 알고리즘을 적용했고(거꾸로된 그래프에서 X에서 출발)
X에서 오는 경우는 주어진 그래프에 다익스트라 알고리즘을 적용했음
그 후에 나온 결과를 각각 더해서 가장 큰 수를 출력하였음
"""
import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph_coming = {}
graph_going = {}
for _ in range(M):
    s, e, t = map(int, input().split())
    graph_coming.setdefault(s, [])
    graph_coming[s].append((e, t))
    graph_going.setdefault(e, [])
    graph_going[e].append((s, t))
    
Q = [(0, X)]
dist_coming = {}
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist_coming:
        dist_coming[node] = time
        for e, t in graph_coming[node]:
            alt = time + t
            heapq.heappush(Q, (alt, e))
Q = [(0, X)]
dist_going = {}
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist_going:
        dist_going[node] = time
        for s, t in graph_going[node]:
            alt = time + t
            heapq.heappush(Q, (alt, s))
            
print(max([dist_going[i] + dist_coming[i] for i in range(1, N+1)]))