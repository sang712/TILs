"""
dfs로 문제를 풀이하였음
"""
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
banner = [input().split() for _ in range(M)]
visited = [[0]*N for _ in range(M)]

def dfs(r, c):
    q = [(r, c)]
    while q:
        r, c = q.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N and banner[nr][nc] == '1' and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

cnt = 0
delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(M):
    for j in range(N):
        if not visited[i][j] and banner[i][j] == '1':
            cnt += 1
            dfs(i, j)
        visited[i][j] = 1
print(cnt)