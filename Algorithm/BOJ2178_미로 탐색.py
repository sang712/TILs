"""
bfs를 구현하여 해결하였음
bfs에 사용하는 큐에는 칸을 몇 번 이동하였는지 정보를 담았고
마지막 위치에 도달했다면 해당 값을 리턴하도록 하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs():
    q = [(0, 0, 1)]
    visited = {(0, 0),}
    while q:
        r, c, cnt = q.pop(0)
        if r == N - 1 and c == M - 1:
            return cnt
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == '1' and not (nr, nc) in visited:
                visited.add((nr, nc))
                q.append((nr, nc, cnt + 1))
                
print(bfs())