board = [input() for _ in range(7)]
new_board = [[''] * 7 for _ in range(7)]

for i in range(7):
    if i < 2 or i > 4:
        k = 2
    else:
        k = 0
    for j in range(k, 7-k):
        new_board[i][j] = board[i][j]

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
ans = 0
for i in range(7):
    if i < 2 or i > 4:
        k = 2
    else:
        k = 0
    for j in range(k, 7-k):
        if new_board[i][j] == 'o':
            for di, dj in delta:
                ni, nj, nni, nnj = i + di, j + dj, i + 2*di, j + 2*dj
                if 0 <= ni < 7 and 0 <= nj < 7 and 0 <= nni < 7 and 0 <= nnj < 7 and new_board[ni][nj] == 'o' and new_board[nni][nnj] == '.':
                    ans += 1
print(ans)