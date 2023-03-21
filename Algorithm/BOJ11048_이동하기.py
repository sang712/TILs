"""
이동이 가능한 방향은 오른쪽, 아래, 오른쪽 아래 대각선 3가지이지만
오른쪽이나 아래쪽으로 이동하여 한 칸이라도 더 들렸다 가는 것이 이득이므로
대각선 방향은 고려하지 않았음
이 방법을 이용해 dp로 문제를 풀었음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + maze[i][0]

for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + maze[0][j]
    
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + maze[i][j]
        
print(dp[N - 1][M - 1])