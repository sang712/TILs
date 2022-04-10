'''
지뢰판과 숫자판을 따로 두고
지뢰판에는 지뢰의 위치를, 숫자판에는 지뢰의 수를 표시하였음
지뢰가 선택되면 어차피 숫자가 안 나타날 것이므로 지뢰칸에는 숫자를 따로 세진 않음
근데 보니까 지뢰판을 따로 쓰진 않으니 지뢰판에 저장한다기 보다는
한 행 한 행 받으면서 바로 지뢰 위치를 저장하는게 좋은 듯
'''
N = int(input())

d = [(-1, -1), (-1, 0), (-1, 1),
     (0, -1), (0, 1),
     (1, -1), (1, 0), (1, 1)]

mineboard = []
board = [[0 for _ in range(N)] for _ in range(N)]
mines = []

bomb = False
for i in range(N):
    row = list(input())
    # mineboard.append(row)
    for j in range(N):
        mine = row[j]
        if mine == '*':
            mines.append((i, j))
            board[i][j] = '*'
            for dr, dc in d:
                cr = dr + i
                cc = dc + j
                if cr >= 0 and cr < N and cc >= 0 and cc < N and not (board[cr][cc] == '*'):
                    board[cr][cc] += 1

for i in range(N):
    row = list(input())
    for j in range(N):
        if row[j] == 'x':
            if board[i][j] == '*':
                bomb = True
            else:
                row[j] = board[i][j]
    board[i] = row

if bomb:
    for r, c in mines:
        board[r][c] = '*'

# 이건 색다른 방법이긴 한데 시간을 12ms 더 소모함
# for row in board:
#     print(*row, sep='')

for i in range(N):
    print(''.join(list(map(str, board[i]))))