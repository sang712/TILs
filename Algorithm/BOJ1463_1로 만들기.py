'''
이렇게 해당 수에 2나 3을 곱해서 그 수를 찾는 것 보다
수를 하나하나 올라가며 나눠지는지 확인하고
그 전 수에 해당하는 것에 1을 더해 비교하는 것이 300ms 더 빠름
지금은 924ms 나옴
'''

N = int(input())

dp = [-1 for _ in range(N+1)]
dp[1] = 0
for num in range(1, N+1):
    times = dp[num] + 1
    X1 = num * 3
    if X1 <= N:
        dp[X1] = times if dp[X1] == -1 else min(times, dp[X1])
    X2 = num * 2
    if X2 <= N:
        dp[X2] = times if dp[X2] == -1 else min(times, dp[X2])
    X3 = num + 1
    if X3 <= N:
        dp[X3] = times if dp[X3] == -1 else min(times, dp[X3])
print(dp[N])