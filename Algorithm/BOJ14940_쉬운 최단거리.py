"""
deque를 import 하여 BFS 방식으로 풀이하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
start = None
for r in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    if not start:
        if 2 in row:
            start = (r, row.index(2))
            board[r][start[1]] = 0

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

q = deque()
q.append((*start, 0))
visited = [[0] * m for _ in range(n)]
visited[start[0]][start[1]] = 1
while q:
    r, c, dist = q.popleft()
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = 1
            if board[nr][nc] == 1:
                board[nr][nc] = dist + 1
                q.append((nr, nc, dist + 1))
                
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            board[i][j] = - 1
            
for row in board:
    print(*row)
            
                