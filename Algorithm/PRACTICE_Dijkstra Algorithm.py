'''
다익스트라 알고리즘
한 정점에서 시작하여 각 정점까지의 최단 거리를 구하는 알고리즘
간선의 값이 음수이면 안 됨

예시 인풋
5 10
1
1 3 8
2 4 1
4 1 1
1 5 5
3 2 1
3 4 5
4 5 10
5 3 2
1 4 1
1 2 11
'''
# N = 노드의 개수, M = 간선의 개수
INF = int(1e9)
N, M = map(int, input().split())
start = int(input()) # 시작 간선

# 구현의 편의를 위해 N+1 길이의 리스트로 만듦
graph = [[] for _ in range(N+1)] # 2차원 리스트 초기화, 안에 튜플이 들어갈 예정
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C)) # (도착점, 거리) 로 이루어진 튜플이 들어감

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1): # 도착 정점을 돌면서 distance가 최소인 정점을 반환
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    # 시작 노드의 인접한 노드 정보를 거리 리스트에 저장
    for arrive, dist in graph[start]:
        distance[arrive] = dist

    for _ in range(N-1):
        now = get_smallest_node() # now 노드는 가장 가까운(비용이 적은) 노드
        visited[now] = True

        for next, dist in graph[now]:
            cost = distance[now] + dist
            # 시작 노드에서 now 노드를 거쳐 next 노드를 가는 비용이 next 노드로 바로 가는 것 보다 저렴하면 갱신
            if cost < distance[next]: 
                distance[next] = cost

dijkstra(start)

print(*distance[1:])