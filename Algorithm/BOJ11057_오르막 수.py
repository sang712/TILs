N = int(input())

dp = [1 for _ in range(10)]

for i in range(1, N):
    for j in range(10):
        dp[j] = sum(dp[j:]) % 10007
print(sum(dp)%10007)