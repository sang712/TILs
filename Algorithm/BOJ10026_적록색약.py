'''
BFS를 구현하여 문제를 해결하였음
비적록색약의 경우는 그림의 색을 1:1 비교하였고
적록색약의 경우는 빨강과 초록의 경우에만 둘 중 하나로 취급하도록 함수를 만들어 처리하였음
'''
import sys
input = sys.stdin.readline

N = int(input())

picture = [list(input().strip()) for _ in range(N)]


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

group_check = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
stack = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = picture[i][j]
            visited[i][j] = 1
            stack.append((i, j))
            group_check += 1
            while stack:
                r, c = stack.pop(0)
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if picture[nr][nc] == color:
                            visited[nr][nc] = 1
                            stack.append((nr, nc))

def color_weak_sees(color: str, as_color: str) -> bool:
    if color == 'R' or color == 'G':
        return 'R' == as_color or 'G' == as_color
    else:
        return color == as_color


color_weak_group_check = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
stack = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = picture[i][j]
            visited[i][j] = 1
            stack.append((i, j))
            color_weak_group_check += 1
            while stack:
                r, c = stack.pop(0)
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if color_weak_sees(picture[nr][nc], color):
                            visited[nr][nc] = 1
                            stack.append((nr, nc))
print(group_check, color_weak_group_check)