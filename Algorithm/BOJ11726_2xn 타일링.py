N = int(input())

dp = [[1, 0]]

for i in range(1, N):
    dp.append([(dp[i-1][0]+dp[i-1][1])%10007, dp[i-1][0]])
print(sum(dp[N-1])%10007)