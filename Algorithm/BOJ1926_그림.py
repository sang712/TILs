import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
num_picture = 0
max_size = 0

def paint(i, j):
    q = [(i, j)]
    visited[i][j] = 1
    size = 1
    while q:
        r, c = q.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and paper[nr][nc] == 1:
                q.append((nr, nc))
                visited[nr][nc] = 1
                size += 1
    return size

for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            size = paint(i, j)
            if size:
                num_picture += 1
                max_size = max(size, max_size)
                
print(num_picture, max_size, sep='\n')
                
