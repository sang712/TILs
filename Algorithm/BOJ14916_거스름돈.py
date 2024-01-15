"""
DP로 풀었음 80ms 걸림
규칙이 있고 몇가지 안 되는 경우의 수라서 하드 코딩하면 더 빠르게 답을 구할 수 있음
"""
N = int(input())
INF = 100_000
dp = [INF, INF, 1, INF, 2, 1]

for i in range(6, N + 1):
    dp.append(min(dp[i-2] + 1, dp[i-5] + 1))
print(dp[N] if dp[N] < 100000 else -1)