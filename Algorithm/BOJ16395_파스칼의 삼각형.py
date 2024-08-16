"""
파스칼의 삼각형은 이항계수, C, 조합으로 나타낼 수 있어서
해당 방법으로 구하였음
단 힌트에서 나온 것 처럼 C(n-1, k-1)로 -1씩해서 적용해야 함
"""
N, K = map(int, input().split())

ans = 1
for i in range(N-K+1, N):
    ans *= i
    
for i in range(1, K):
    ans //= i

print(ans)