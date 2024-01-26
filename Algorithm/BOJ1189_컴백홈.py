R, C, K = map(int, input().split())

board = [input() for _ in range(R)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0] * C for _ in range(R)]
ans = 0

def dfs(i, j, k):
    if k == K:
        if i == 0 and j == C-1:
            global ans
            ans += 1
        return
    
    visited[i][j] = 1
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and board[ni][nj] != 'T':
            dfs(ni, nj, k+1)
    visited[i][j] = 0

dfs(R-1, 0, 1)
print(ans)