"""
메모이제이션 한다고 memo를 정의해놓고 전혀 쓰질 않아서 시간초과로 틀렸었음
memo[n]을 초기화 하는 라인을 하나 추가함으로써 통과할 수 있었음
"""
N, P, Q = map(int, input().split())

memo = {0: 1}

def A(n):
    if n in memo:
        return memo[n]
    memo[n] = A(n // P) + A(n // Q)
    return memo[n]

print(A(N))