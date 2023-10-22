"""
dp 방법으로 풀긴 했는데 set 자료구조를 이용하는 게 맞는지 잘은 모르겠음
마지막 줄에 dp_P[N]이 공집합이 아닌 것이 확정이 아니라 ValueError를 냈었는데 수정하였음
"""
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp_P = [set() for _ in range(N + 1)]

dp_P[0] = {S, }
for i in range(N):
    if dp_P[i]:
        for p in list(dp_P[i]):
            if p - V[i] >= 0:
                dp_P[i + 1].add(p - V[i])
            if p + V[i] <= M:
                dp_P[i + 1].add(p + V[i])
    else:
        print(-1)
        break
else:
    print(max(list(dp_P[N])) if dp_P[N] else -1)