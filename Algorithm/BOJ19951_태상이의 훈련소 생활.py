N, M = map(int, input().split())

ground = list(map(int, input().split()))
orders = [0] * (N+1)

for case in range(M):
    a, b, H = map(int, input().split())
    # 시작점과 끝 점만 저장해서 14번 라인에서 직전 항을 계속 더하는 방식을 사용
    orders[a-1] += H
    orders[b] -= H

for i in range(N):
    if i > 0:
        orders[i] += orders[i-1]

    ground[i] += orders[i]
    if i == N-1:
        print(ground[i])
    else:
        print(ground[i], end=" ")