"""
처음에는 dfs로 풀려고 하다가 구현 중에 dp로 푸는 것임을 알아채서
dp로 수정하여 구현하였음
이렇게 구현하니 훨씬 더 간결하고 깔끔하게 구현할 수 있었음
2차원 배열에다 해당 좌표에 파이프의 끝이 도달하는 경우의 수를 저장하도록 하였고
시작은 dp[0][1]에 [1, 0, 0]으로 시작하도록 하였음
그리고 반복문에서 열을 반복하는 for문은 1부터 시작하도록 하였음

그림을 그려보니 가로로 끝나는 경우는 직전이 가로나 대각선으로 끝났을 때,
세로로 끝나는 경우는 직전이 세로나 대각선으로 끝났을 때,
대각선으로 끝나는 경우는 직전이 아무거나여도 상관없으므로
각각의 경우에 따라 더해주도록 구현하였음

물론 dp문제임을 알아채는데에는 시간이 걸렸지만
dp가 익숙해지니 골드5 문제가 쉽게 느껴짐
"""
N = int(input())
walls = [input().split() for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1] = [1, 0, 0]
for i in range(N):
    for j in range(1, N):
        flag = 0
        if j + 1 < N and walls[i][j + 1] == '0':
            dp[i][j + 1][0] = dp[i][j][0] + dp[i][j][2]
            flag += 1
        if i + 1 < N and walls[i + 1][j] == '0':
            dp[i + 1][j][1] = dp[i][j][1] + dp[i][j][2]
            flag += 1
        if flag == 2 and walls[i + 1][j + 1] == '0':
            dp[i + 1][j + 1][2] = sum(dp[i][j])
            
# print(*dp, sep='\n')
print(sum(dp[N-1][N-1]))