'''
bfs를 이용하여 그룹화 하여 풀었음
cnt를 인자로 받지 않고 풀 수 있지 않을까하여 해당 방식으로 구현하였음
'''
N, M = map(int, input().split())

battlefield = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(r, c, color):
    cnt = 0
    if visited[r][c]:
        return 0
    else:
        if battlefield[r][c] == color:
            cnt += 1
            visited[r][c] = 1
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                    cnt += bfs(nr, nc, color)
        return cnt

force = {'W': 0, 'B': 0}
for i in range(M):
    for j in range(N):
        color = battlefield[i][j]
        force[color] += bfs(i, j, color)**2

print(force['W'], force['B'])