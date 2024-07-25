"""
dfs방식에 두 지점간의 높이차를 확인하는 구문을 추가해 구현하였음
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        cnt += 1
        visited[i][j] = 1
        q = [(i, j)]
        while q:
            r, c = q.pop()
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and abs(room[r][c] - room[nr][nc]) <= K:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
print(cnt)