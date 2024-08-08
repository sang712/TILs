N, K = map(int, input().split())

sumation = K*(K+1)//2
if N < sumation:
    print(-1)
else:
    N -= sumation
    if N % K:
        print(K)
    else:
        print(K-1)