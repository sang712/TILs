"""
문제에서 재귀라고 힌트를 주고 있어서 dp 문제임을 알 수 있었고
양 옆에 둘 수가 0일 때부터 n//2일 때까지의 경우의 수를 모두 더해서 답을 구했음
"""
import sys
input = sys.stdin.readline

dp = [1, 1]
cases = [int(input()) for _ in range(int(input()))]
for i in range(2, max(cases)+1):
    dp.append(sum(dp[:i//2+1]))
print(*map(lambda x: dp[x], cases), sep='\n')