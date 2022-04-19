'''
플로이드 와샬 알고리즘 구현하기

각 정점에서 각 정점으로까지의 최단 거리 구하기

정점의 그래프는 다음과 같이 생김
[[0, 5, X, 8],
[7, 0, 9, X],
[2, X, 0, 4],
[X, X, 3, 0]]

'''
from math import dist


X = float('inf')
# 정점의 그래프
nodes = [[0, 8, 5, 1],
[X, 0, X, X],
[X, 2, 0, X],
[X, X, 1, 0]]
size = 4
def floydWarshall():

    # 결과 그래프 초기화
    distance = [[] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            distance[i].append(nodes[i][j])

    for k in range(size): # k = 거쳐가는 노드
        for i in range(size): # i = 시작 노드
            for j in range(size): # j = 도착 노드
                # k를 거쳐가는 것이 더 저렴한 비용이라면
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    # k를 거쳐가는 비용으로 초기화
                    distance[i][j] = distance[i][k] + distance[k][j]
    print(distance)

floydWarshall()
