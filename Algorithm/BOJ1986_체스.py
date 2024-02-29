"""
zip 함수를 이용해 각 말들의 좌표를 정리했고
각 좌표를 담은 blocked 변수와 방문체크를 하는 visited 변수를 추가하였음
둘로 나눈 이유는 blocked에 도달하면 멈춰야 하고, visited를 만나도 다음으로 이동하는 queen의 이동 방식때문임
그러고 퀸과 나이트를 움직이면서 조건에 맞게 카운팅하였음
"""
n, m = map(int, input().split())
queens = list(map(int, input().split()))
pos_queen = set(zip(queens[1::2], queens[2::2]))
knights = list(map(int, input().split()))
pos_knight = set(zip(knights[1::2], knights[2::2]))
pawns = list(map(int, input().split()))
pos_pawns = set(zip(pawns[1::2], pawns[2::2]))

safe_space = n*m - queens[0] - knights[0] - pawns[0]
d_knight = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
d_queen = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

blocked = pos_queen.union(pos_knight).union(pos_pawns)
visited = set()
for r, c in pos_queen:
    for dr, dc in d_queen:
        nr, nc = r+dr,  c+dc
        while 1 <= nr <= n and 1 <= nc <= m:
            if (nr, nc) in blocked:
                break
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                safe_space -= 1
            nr, nc = nr+dr, nc+dc

for r, c in pos_knight:
    for dr, dc in d_knight:
        nr, nc = r+dr, c+dc
        if 1 <= nr <= n and 1 <= nc <= m and (nr, nc) not in blocked and (nr, nc) not in visited:
            visited.add((nr, nc))
            safe_space -= 1
print(safe_space)