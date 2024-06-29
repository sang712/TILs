"""
답은 1부터 N-1까지 다 더한 수와 같음
N*(N-1)//2 출력해도 무방함

다만 문제에서 요구한 대로 구현하였음
"""
N = int(input())
memo = {0: 0, 1: 0}


def scatter(n):
    if n <= 1: return 0
    if n in memo: return memo[n]
    
    b = n//2
    if n % 2 == 0:
        memo[n] = 2 * scatter(b) + b ** 2
    else:
        c = n-b
        memo[n]  = b*c + scatter(b) + scatter(c)
    return memo[n]

scatter(N)
print(memo[N])