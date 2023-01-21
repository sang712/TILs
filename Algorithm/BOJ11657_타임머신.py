"""
어제 학습한 벨만 포드 알고리즘을 이용하여 문제를 풀었음
어제의 문제와는 달리 벨만 포드 알고리즘을 변형하지 않고 그대로 적용하는 문제라 크게 어렵지는 않았음

벨만 포드 알고리즘을 구현한 함수를 만들었고 결과를 반환할 때 
음수 간선이 포함된 사이클이 존재했다면 2번 idx의 값이 -1인 리스트를 반환하여 
답을 print 할 때 일반화가 잘 되도록 작성하였음
"""
N, M = map(int, input().split())

MAXIMUM = 5_000_001
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
    
def bellman_ford(N, edges):
    dists = [MAXIMUM for _ in range(N + 1)]
    dists[1] = 0
    for _ in range(N-1):
        updated = False
        for cur_node, next_node, cost in edges:
            if dists[cur_node] != MAXIMUM and dists[next_node] > dists[cur_node] + cost:
                dists[next_node] = dists[cur_node] + cost
                updated = True
        if not updated:
            return dists
                
    for cur_node, next_node, cost in edges:
        if dists[cur_node] != MAXIMUM and dists[next_node] > dists[cur_node] + cost:
            return [MAXIMUM, 0, -1]

    return dists

for dist in bellman_ford(N, edges)[2:]:
    print(dist if dist != MAXIMUM else -1)