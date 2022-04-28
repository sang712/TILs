# dp로 푸는 문제였음
# dp를 사용하지 않아도 재귀로 풀어도 됨
'''
이상적인 코드
H, Y = map(int, input().split())

def solve(H, Y):
	if Y < 0: return -1
	if Y == 0: return H
	
	return max(
		solve(int(H * 1.05), Y - 1),
		solve(int(H * 1.2), Y - 3),
		solve(int(H * 1.35), Y - 5)
	)
	
print(solve(H, Y))
'''

H, Y = map(int, input().split())
dp = [0 for i in range(Y + 1)]
dp[0] = H

for i in range(1, Y+1):
    if i >= 5:
        dp[i] = max(dp[i - 1]*1.05, dp[i - 3]*1.2, dp[i - 5]*1.35)
    elif i >= 3:
        dp[i] = max(dp[i - 1]*1.05, dp[i - 3]*1.2)
    else:
        dp[i] = dp[i - 1]*1.05
    dp[i] = int(dp[i])
print(dp[Y])