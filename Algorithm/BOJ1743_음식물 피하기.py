"""
주어진 음식물끼리 붙어있는지만 확인하면 되므로 좌표를 저장하는 그리드를 따로 선언하지 않았음
"""
import sys
sys.setrecursionlimit(10**6)
N, M, K = map(int, input().split())

foods = set([tuple(map(int, input().split())) for _ in range(K)])

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def connect_foods(r, c):
    size = 1
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if (nr, nc) in foods:
            foods.discard((nr, nc))
            size += connect_foods(nr, nc)
    return size

ans = 0
while foods:
    r, c = foods.pop()
    size = connect_foods(r, c)
    ans = max(ans, size)
print(ans)
