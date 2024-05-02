"""
입력의 크기가 100*100으로 크지 않아 그냥 2차원 리스트에 표시하고
그래프 탐색 방식으로 답을 구하는 방법을 이용하였음
"""
import sys
sys.setrecursionlimit(100_000)
M, N, K = map(int, input().split())

area = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            area[r][c] = 1
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(r, c):
    cnt = 1
    area[r][c] = 1
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and area[nr][nc] == 0:
            cnt += dfs(nr, nc)
    return cnt

ans = []
for i in range(M):
    for j in range(N):
        if area[i][j]:
            continue
        ans.append(dfs(i, j))
print(len(ans))
print(*sorted(ans))