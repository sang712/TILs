"""
시간을 줄이기 위해 최소 높이를 검색하여 진행하도록 하였음
count_area 함수에서는 BFS를 이용하여 연결된 구역들의 수를 반환하도록 하였고
반복문을 통해 최소 높이부터 100까지 count_area 함수를 반복해서 호출하도록 하였음

시간을 더 줄이는 방법으로는 최소 높이를 찾는 것 보다
Collections의 Counter를 이용하여 모든 높이를 찾고
해당 높이가 존재할 때만 bfs로 검사를 하는 것이라고 생각함
그렇게 되면 해당 높이가 존재하지 않을 땐 건너뛸 수도 있고
기존에 내가 구현한 최소 높이부터 시작할 수도 있기 때문
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]

min_height = 101
for i in range(N):
    temp_min = min(region[i])
    if min_height > temp_min:
        min_height = temp_min
        
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def count_area(height):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or region[i][j] <= height:
                continue
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            cnt += 1
            while q:
                r, c = q.popleft()
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        if region[nr][nc] > height:
                            q.append((nr, nc))
    return cnt           

max_area = 1
for height in range(min_height, 101):
    cnt = count_area(height)
    max_area = max(max_area , cnt)
    if cnt == 0:
        break
print(max_area)