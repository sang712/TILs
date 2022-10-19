'''
dfs로 풀었더니 최대 재귀 깊이가 1000을 초과해 RecursionError가 발생하였음
sys.setrecursionlimit을 1만(10**5)으로 하여 통과하였음
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(r, c):
    field[r][c] = 0
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1:
            dfs(nr, nc)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    worms = []
    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1
        worms.append((r, c))
    cnt = 0
    for r, c in worms:
        if field[r][c] == 1:
            cnt += 1
            dfs(r, c)
    print(cnt)