"""
구현 문제라 요구사항대로 구현하였음

숫자그대로 주변에 다 더해주었고 마지막에 지뢰자리와 지뢰가 주변에 10개 이상인 경우를
찾아서 조건에 맞게 변경해주었음
"""

import sys
input = sys.stdin.readline
N = int(input())
mine_map = [input() for _ in range(N)]

mine_search_map = [[0] * N for _ in range(N)]

delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(N):
    for j in range(N):
        if mine_map[i][j] == '.':
            continue
        
        num_mine = int(mine_map[i][j])
        for dr, dc in delta:
            nr, nc = i + dr, j + dc
            if 0 <= nr < N and 0 <= nc < N:
                mine_search_map[nr][nc] += num_mine

for i in range(N):
    for j in range(N):
        if mine_search_map[i][j] > 9:
            mine_search_map[i][j] = 'M'
        
        if mine_map[i][j] != '.':
            mine_search_map[i][j] = '*'
        
for row in mine_search_map:
    print(*row, sep='')
