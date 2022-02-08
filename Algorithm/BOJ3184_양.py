# dfs로 풀었으며 recursion error가 발생(1000회 이상 깊이)
# 따라서 setrecursionlimit을 늘려줌으로써 해당 에러를 해결함
import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

animals = []
yard = []
wolves = 0
lambs = 0
for i in range(R):
    row = list(input())
    yard.append(list(row))
    for j in range(C):
        if row[j] == 'v':
            animals.append((i, j))
            wolves += 1
        elif row[j] == 'o':
            animals.append((i, j))
            lambs += 1

def recursion(r, c):
    global wolf, lamb
    if visited[r][c]:
        return
    else:
        visited[r][c] = 1

    if yard[r][c] == 'v':
        wolf += 1
    elif yard[r][c] == 'o':
        lamb += 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and not (yard[nr][nc] == '#') and visited[nr][nc] == 0:
            recursion(nr, nc)

visited = [[0 for _ in range(C)] for _ in range(R)]

wolf = 0
lamb = 0
while animals:
    r, c = animals.pop()

    recursion(r, c)

    if wolf >= lamb:
        lambs -= lamb
    else:
        wolves -= wolf
    wolf = 0
    lamb = 0

print(lambs, wolves)