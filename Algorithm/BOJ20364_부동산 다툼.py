import sys

N, Q = map(int, input().split())
owned = [0]*(N+1)
for _ in range(Q):
    duck = int(sys.stdin.readline()) # sys.stdin.readline()을 쓰지않으면 시간초과가 남
    path = duck
    reachable = True
    encounter = -1
    while path:
        if owned[path]:
            reachable = False
            encounter = path
        path //= 2
    if reachable:
        owned[duck] += 1
        print(0)
    else:
        print(encounter)