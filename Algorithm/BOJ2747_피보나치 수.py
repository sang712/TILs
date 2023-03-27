N = int(input())
dp = [0, 1]
while len(dp) <= N:
    dp.append(dp[-1] + dp[-2])
print(dp[N])