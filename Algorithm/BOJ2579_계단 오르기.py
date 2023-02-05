"""
dp로 푸는지 몰랐다면 풀기 어려웠을 문제

튜플에 직전 칸을 밟은 경우와 직전 칸을 건너뛰는 경우 둘로 나누어 값을 담았고
해당 튜플을 원소로 갖는 dp를 만들어 한칸씩 오르면서 확인하도록 하였음
"""
import sys

n = int(input())

steps = [int(input()) for _ in range(n)]
dp = [(0, 0), (steps[0], 0)]

for i in range(1, n):
    dp.append((max(dp[i-1]) + steps[i], dp[i][0] + steps[i]))
    
print(max(dp[n]))