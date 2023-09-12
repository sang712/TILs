"""
출발 지점의 좌표를 (0, 0)으로 두고 방문하는 모든 지점을 저장한 뒤에
해당 지점들 중 가장 작은 r, c좌표, 가장 큰 r, c좌표를 구해서
행의 크기, 열의 크기를 구하고, 좌표는 평면이동하는 방식으로 문제를 풀이하였음
"""
N = int(input())
commands = input()

delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]

r = c = dir = 0
pos = {(0, 0), }
for command in commands:
    if command == 'R':
        dir = (dir + 1) % 4
    elif command == 'L':
        dir = (dir - 1) % 4
    else:
        dr, dc = delta[dir]
        r, c = r + dr, c + dc
        pos.add((r, c))
        
rs, cs = zip(*pos)
min_r, min_c = min(rs), min(cs)
R = max(rs) - min_r + 1
C = max(cs) - min_c + 1

maze = [['#'] * C for _ in range(R)]
for pos_r, pos_c in pos:
    maze[pos_r - min_r][pos_c - min_c] = '.'
    
for row in maze:
    print(*row, sep='')