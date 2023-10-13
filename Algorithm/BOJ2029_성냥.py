"""
마지막 가장 큰 정사각형을 카운팅할 때 성냥의 개수가 12개여야 하는데
9개와 비교하는 실수와
i + di, i + dj를 하는 실수가 있었음
"""
matches = [input() for _ in range(10)]

grid = [[0] * 7 for _ in range(7)]

omitted_matches = 24
r = 0
for i in range(0, 10, 3):
    c = 1
    for j in range(1, 10, 3):
        if matches[i][j] == '-':
            grid[r][c] = 1
            omitted_matches -= 1
        if matches[j][i] == '|':
            grid[c][r] = 1
            omitted_matches -= 1
        c += 2
    r += 2

squares = 0
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(1, 7, 2):
    for j in range(1, 7, 2):
        cnt = 0
        for di, dj in delta:
            if grid[i + di][j + dj]:
                cnt += 1
        if cnt == 4:
           squares += 1

delta_square4 = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]
for i in range(2, 5, 2):
    for j in range(2, 5, 2):
        cnt = 0
        for di, dj in delta_square4:
            if grid[i + di][j + dj]:
                cnt += 1
        if cnt == 8:
            squares += 1

cnt = 0
for i in range(1, 7, 2):
    cnt += grid[0][i] + grid[i][0] + grid[6][i] + grid[i][6]
if cnt == 12:
    squares += 1
print(omitted_matches, squares)