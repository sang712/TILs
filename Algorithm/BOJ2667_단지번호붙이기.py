'''
방문체크 리스트를 두고 이중 for문을 돌면서 bfs를 사용하여 방문체크를 하면서 구역을 확인하였음
'''
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
map = [list(map(int, list(input()))) for _ in range(N)]

num_of_families_in_complex = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        visited[i][j] = 1
        stack = []
        cnt = 0
        if map[i][j] == 1:
            stack.append((i, j))
        while stack:
            r, c = stack.pop(0)
            cnt += 1
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and map[nr][nc]:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))
        if cnt:
            num_of_families_in_complex.append(cnt)
        
print(len(num_of_families_in_complex), *sorted(num_of_families_in_complex), sep='\n')