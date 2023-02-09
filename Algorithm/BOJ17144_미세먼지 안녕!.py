"""
구현, 시뮬레이션 문제답게 문제에서 요구하는 대로 구현하였음

먼지를 퍼뜨리는 과정은 stack에 퍼뜨릴 먼지를 담은 뒤에
한 번에 처리하도록 하였고(이 과정에서 연산이 2배가 된 듯함)

공기를 정화하는 과정에서는 위 아래를 한 번에 구현하려고 하다가
그냥 하드하게 둘로 나눠서 진행하도록 하였음

마지막에 따로 카운팅을 하지 않게 처음에 카운팅을 하고
거기에서 정화된 먼지의 양을 빼서 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

purifier = []
total_dust = 2
for r in range(R):
    total_dust += sum(room[r])
    if room[r][0] == -1:
        purifier.append(r)

purifier_up = [(0, 1), (-1, 0), (0, -1), (1, 0)]
purifier_down = [(0, 1), (1, 0), (0, -1), (-1, 0)]
delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def diffuse() -> None:
    dusts = []
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                dust = room[r][c] // 5
                ways = 0
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] >= 0:
                        dusts.append((nr, nc, dust))
                        ways += 1
                room[r][c] -= dust * ways
    while dusts:
        r, c, dust = dusts.pop()
        room[r][c] += dust

def purify() -> int:
    filtered = 0
    
    r, c = purifier[0], 1
    room[r][c], temp = 0, room[r][c]
    dir = 0
    dr, dc = purifier_up[dir]
    while r != purifier[0] - 1 or c != 0:
        nr, nc = r + dr, c + dc
        if not 0 <= nr <= purifier[0] or not 0 <= nc < C:
            dir += 1
            dr, dc = purifier_up[dir]
            nr, nc = r + dr, c + dc
        room[nr][nc], temp = temp, room[nr][nc]
        r, c = nr, nc
    filtered += temp
        
    r, c = purifier[1], 1
    room[r][c], temp = 0, room[r][c]
    dir = 0
    dr, dc = purifier_down[dir]
    while r != purifier[1] + 1 or c != 0:
        nr, nc = r + dr, c + dc
        if not purifier[1] <= nr < R or not 0 <= nc < C:
            dir += 1
            dr, dc = purifier_down[dir]
            nr, nc = r + dr, c + dc
        room[nr][nc], temp = temp, room[nr][nc]
        r, c = nr, nc
        
    filtered += temp
    return filtered

for t in range(T):
    diffuse()
    total_dust -= purify()
    
print(total_dust)