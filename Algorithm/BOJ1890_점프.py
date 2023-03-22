"""
오른쪽과 아래쪽으로만 이동하므로 delta 없이 이중 for문으로 진행구현하였고
조건에 맞을 때만 dp에 값을 저장하면서 필요없는 경우는 카운트되지 않도록 하였음
그리고 마지막 0에 도달했을 때는 멈추도록 하여 의미없이 중복되어 카운트 되지 않도록 하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            continue
        jump = board[i][j]
        if not jump:
            continue
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]
            
print(dp[N - 1][N - 1])
