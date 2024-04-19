"""
전형적인 dp문제로 초기값을 지정해주고 반복문을 통해 풀이하였음
"""
N = int(input())

dp = [1, 1]
for _ in range(N):
    dp.append((dp[-1] + dp[-2]) % 15746)
print(dp[N])