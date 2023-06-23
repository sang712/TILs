"""
U+M+D와 L+N+R을 범위로하는 2중 포문을 이용하여 문제를 풀었음
이 때 loop가 U보다 크면서 U+M보다 작고, L보다 크면서 L+N보다 작을 때는
크로스 워드를, 아닐 경우는 홀수, 짝수를 판별하여 각각 '.', '#'를 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

crosswords = [input().strip() for _ in range(M)]

for i in range(U + M + D):
    row = []
    for j in range(L + N + R):
        if U <= i < U + M and L <= j < L + N:
            row.append(crosswords[i - U][j - L])
        elif (i + j) % 2: 
            row.append('.')
        else: 
            row.append('#')
    print(*row, sep='')
