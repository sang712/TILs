board = [list(input().split()) for _ in range(19)]

delta = [(0, 1), (1, 0), (1, 1), (-1, 1)]
def check_5_in_a_row(r, c, color):
    for dr, dc in delta:
        nr, nc = r, c
        for _ in range(1, 5):
            nr, nc = nr + dr, nc + dc
            if not (0 <= nr < 19 and nc < 19 and board[nr][nc] == color):
                break
        else:
            nr, nc = nr + dr, nc + dc
            if not (0 <= r - dr < 19 and 0 <= c - dc < 19) or board[r-dr][c-dc] != color:
                if not (0 <= nr < 19 and 0 <= nc < 19) or board[nr][nc] != color:
                    return r, c, color
    return r, c, ''

def solve():
    for i in range(19):
        for j in range(19):
            if board[i][j] != '0':
                r, c, color = check_5_in_a_row(i, j, board[i][j])
                if color:
                    print(color)
                    print(r + 1, c + 1)
                    return
    print('0')
    return
solve()