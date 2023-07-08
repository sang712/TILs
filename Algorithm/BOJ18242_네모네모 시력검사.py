"""
입력을 받아 주어진 문양을 stack을 활용한 DFS로 탐색하였고
탐색하면서 이동방향에 해당하는 델타 값을 총합해
탐색 시작 위치에서 탐색이 어느 방향으로 진행되는지의 경향성을 파악하였고
그 값에따라 답을 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

start = None
for i in range(N):
    row = input()
    if not start:
        if '#' in row:
            start = (i, row.index('#'))
    board.append(list(row))

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
stack = [start]
visited = set()
total_r, total_c = 0, 0
while stack:
    r, c = stack.pop()
    visited.add((r, c))
    num_next = 0
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '#' and not (nr, nc) in visited:
            visited.add((nr, nc))
            stack.append((nr, nc))
            total_r += dr
            total_c += dc

if total_r == 0:
    print('UP')
elif total_c == 0:
    print('LEFT')
elif total_r > total_c:
    print('DOWN')
else:
    print('RIGHT')