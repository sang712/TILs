"""
판 위에 선을 긋는 작업은 함수를 구현하여 사용하였고
다음 위치가 유효한지 판단하여 해당 함수를 호출하도록 하였음
"""

N = int(input())
board = [['.'] * N for _ in range(N)]

move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
execution = input()

def carve(r, c, dir):
    current = board[r][c]
    if dir == 'U' or dir == 'D':
        if current == '.':
            board[r][c] = '|'
        elif current == '|':
            pass
        else:
            board[r][c] = '+'
    elif dir == 'L' or dir == 'R':
        if current == '.':
            board[r][c] = '-'
        elif current == '-':
            pass
        else:
            board[r][c] = '+'
            
r, c = 0, 0
for order in execution:
    dr, dc = move[order]
    nr, nc = r + dr, c + dc
    if 0 <= nr < N and 0 <= nc < N:
        carve(r, c, order)
        carve(nr, nc, order)
        r, c = nr, nc

for row in board:
    print(*row, sep='')
