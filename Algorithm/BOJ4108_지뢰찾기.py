import sys
input = sys.stdin.readline

delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

R, C = map(int, input().split())
while R and C:
    mine_field = [list(input().strip()) for _ in range(R)]
    mine_checked_field = []
    for r in range(R):
        mine_checked_row = []
        for c in range(C):
            if mine_field[r][c] == '*':
                mine_checked_row.append('*')
                continue
            mines = 0
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and mine_field[nr][nc] == '*':
                    mines += 1
            mine_checked_row.append(mines)
        mine_checked_field.append(mine_checked_row)
    for row in mine_checked_field:
        print(*row, sep='')
    R, C = map(int, input().split())