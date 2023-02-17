"""
각 노드에서 다른 노드까지의 최소거리를 계산해야 하므로
다익스트라보다는 플로이드 워셜이 맞다고 판단하여 해당 방법으로 구현하였음
시작점과 도착점을 인덱스로 갖고 거리를 값으로 갖는 2차원의 그래프를 만들었고
플로이드 워셜 알고리즘을 적용해 최단거리를 구하였음

그 후에 2차원 그래프의 행을 기준으로 m보다 값이 작으면
해당 도착지에 맞는 아이템의 개수를 누적하였고
누적된 아이템의 개수 중 가장 높은 값을 찾도록 하였음
"""
n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

INF = float('inf')
field = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    field[a][b] = l
    field[b][a] = l
    
for k in range(1, n + 1):
    field[k][k] = 0
    for i in range(1, n + 1):
        if k == i:
            continue
        for j in range(1, n + 1):
            if j == k:
                continue
            if field[i][k] + field[k][j] < field[i][j]:
                field[i][j] = field[i][k] + field[k][j]

max_num_items = 0
for i in range(1, n + 1):
    num_items = 0
    for j in range(1, n + 1):
        if field[i][j] <= m:
            num_items +=  t[j]
    max_num_items = max(max_num_items, num_items)
print(max_num_items)