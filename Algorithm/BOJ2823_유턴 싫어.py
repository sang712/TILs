"""
유턴을 해야한다는 것은 연결된 칸이 1개 이하라는 뜻이므로 
그래프 탐색을 하면서 연결된 칸의 개수를 세어 1개 이하면 탈출을 하는 함수를 만들어 풀이하였음
"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
town = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def is_Uturn():
    for i in range(R):
        for j in range(C):
            if town[i][j] == '.' and not visited[i][j]:
                visited[i][j] = 1
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    cnt = 0
                    for dr, dc in delta:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and town[nr][nc] == '.':
                            cnt += 1
                            if not visited[nr][nc]:
                                visited[nr][nc] = 1
                                stack.append((nr, nc))
                    if cnt <= 1:
                        return True
    return False
if is_Uturn():
    print(1)
else:
    print(0)