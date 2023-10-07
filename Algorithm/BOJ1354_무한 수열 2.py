"""
BOJ1351 무한 수열과 같은 유형의 문제라 바로 풀었음
"""
N, P, Q, X, Y = map(int, input().split())

memo = {0: 1}
def A(n):
    if n <= 0:
        return memo[0]
    if n in memo:
        return memo[n]
    memo[n] = A(n // P - X) + A(n // Q - Y)
    return memo[n]

print(A(N))