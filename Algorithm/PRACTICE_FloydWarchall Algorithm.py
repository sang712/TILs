'''
플로이드 와샬 알고리즘 구현하기

각 정점에서 각 정점으로까지의 최단 거리 구하기

정점은 다음과 같이 생김
[[0, 5, X, 8],
[7, 0, 9, X],
[2, X, 0, 4],
[X, X, 3, 0]]

'''
X = 
nodes = [[0, 5, X, 8],
[7, 0, 9, X],
[2, X, 0, 4],
[X, X, 3, 0]]
size = 4
def floydWarshall():
    distance = []

    for i in range(size):
        for j in range(size):
