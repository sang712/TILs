N = int(input())
grid = [[0] * 20 for _ in range(20)]

def cnt_stone(curr, dir, color):
    r, c = curr
    dr, dc = dir
    cnt = 0
    while True:
        r += dr
        c += dc
        if 0 < r < 20 and 0 < c < 20 and grid[r][c] == color:
            cnt += 1
            continue
        return cnt

move = [list(map(int, input().split())) for _ in range(N)]

for i, pos in enumerate(move):
    color = i % 2 + 1
    grid[pos[0]][pos[1]] = color
    horizontal, vertical, diagonal1, diagonal2 = 1, 1, 1, 1
    horizontal += cnt_stone(pos, (0, -1), color)
    horizontal += cnt_stone(pos, (0, 1), color)
    vertical += cnt_stone(pos, (-1, 0), color)
    vertical += cnt_stone(pos, (1, 0), color)
    diagonal1 += cnt_stone(pos, (1, 1), color)
    diagonal1 += cnt_stone(pos, (-1, -1), color)
    diagonal2 += cnt_stone(pos, (-1, 1), color)
    diagonal2 += cnt_stone(pos, (1, -1), color)

    if horizontal == 5 or vertical == 5 or diagonal1 == 5 or diagonal2 == 5:
        print(i + 1)
        break
else:
    print(-1)
    
print(*grid, sep='\n')