'''
임의의 한 정점에서 또 다른 임의의 한 정점까지의 거리를 계산하는 것이므로
플로이드 와샬 알고리즘을 적용하였음
'''
N, M = map(int, input().split())

routes = []
for _ in range(N):
    routes.append(list(map(int, input().split())))


'''
플로이드 와샬 알고리즘
거르는 조건 없을 때 924ms
거르는 조건을 추가하면 오히려 더 오래 걸렸음
'''
for k in range(N):
    for i in range(N):
        # if k == i: continue 1128ms
        for j in range(N):
            # if k == i or i == j or k == j: continue 980ms
            if routes[i][k] + routes[k][j] < routes[i][j]:
                routes[i][j] = routes[i][k] + routes[k][j]

for _ in range(M):
    A, B, C = map(int, input().split())
    punctual = True if routes[A-1][B-1] <= C else False
    print("Enjoy other party") if punctual else print("Stay here")
        