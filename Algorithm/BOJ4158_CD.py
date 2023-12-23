import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    cd_sg = set([int(input()) for _ in range(N)])
    ans = 0
    for _ in range(M):
        cd = int(input())
        if cd in cd_sg:
            ans += 1

    print(ans)