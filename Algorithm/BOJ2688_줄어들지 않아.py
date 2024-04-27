"""
전형적인 dp문제로 
각 자리수 별로 될 수 있는 수의 경우의 수를 저장하는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline

T = int(input())
dp = [[], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for t in range(T):
    n = int(input())
    for _ in range(len(dp)-1, n):
        temp = sum(dp[-1])
        next = [temp]
        for i in range(9):
            temp -= dp[-1][i]
            next.append(temp)
        dp.append(next)
    print(sum(dp[n]))
