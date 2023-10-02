"""
조합을 계산하는 문제
그냥 조합을 구현하였음
"""
import sys
input = sys.stdin.readline

ans = []
for t in range(int(input())):
    N, M = map(int, input().split())
    
    num = 1
    for i in range(max(N, M - N) + 1, M + 1):
        num *= i
    for j in range(1, min(N, M - N) + 1):
        num //= j
    ans.append(num)

print(*ans)