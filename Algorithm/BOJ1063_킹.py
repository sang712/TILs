"""
문제에서 요구하는 대로 구현하였음
2차원 그래프 문제 풀이와 비슷하게 풀었고
가로방향이 우선이 된다는 점이 일반적인 문제와 달라 유의해야 했음
"""
import sys
input = sys.stdin.readline

pos_king, pos_stone, N = input().split()

commands = [input().strip() for _ in range(int(N))]
decode = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
          'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
def pos_to_idx(pos):
    return (ord(pos[0]) - ord('A'), int(pos[1]) - 1)
def idx_to_pos(pos):
    return (chr(pos[0] + ord('A')) + str(pos[1] + 1))

pos_king = pos_to_idx(pos_king)
pos_stone = pos_to_idx(pos_stone)

for command in commands:
    kc, kr = pos_king
    sc, sr = pos_stone
    dc, dr = decode[command]
    
    knc, knr = kc + dc, kr + dr
    if 0 <= knc < 8 and 0 <= knr < 8:
        if  knc == sc and knr == sr:
            snc, snr = sc + dc, sr + dr
            if 0 <= snc < 8 and 0 <= snr < 8:
                pos_stone = (snc, snr)
                pos_king = (knc, knr)
        else:
            pos_king = (knc, knr)
print(idx_to_pos(pos_king))
print(idx_to_pos(pos_stone))