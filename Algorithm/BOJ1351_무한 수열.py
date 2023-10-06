N, P, Q = map(int, input().split())

memo = {0: 1}

def A(n):
    if n in memo:
        return memo[n]
    memo[n] = A(n // P) + A(n // Q)
    return memo[n]

print(A(N))