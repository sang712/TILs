"""
처음에는 현재 이동거리와 벽을 부쉈는지 안 부쉈는지를 큐에 같이 넣어서 사용하였는데
한 지점을 벽을 부수고 도달했을 때와 그냥 도달했을 때가 있을 경우에 visited로 처리하기 어려워서

벽을 안 부수고 지나갔을 때와 벽을 하나라도 부쉈을 때를 나누어 저장하는
2차원 거리 리스트를 만들어서 사용하였음

그렇게 되니 큐에 현재 이동거리를 안 넣어도 되었고 대신에 벽을 부쉈는지 안 부쉈는지 정보만 추가해서 사용하였음

그렇게 해서 기본 지도에 0일 경우는 쭉 따라가면서 
부수지 않았을 때 경우끼리, 부쉈을 때 경우끼리 거리 2차원 리스트에 넣고
만약 이번에 벽을 부수게 되었을 때는 직전의 부수지 않았을 때의 경우를 참고하여 부쉈을 때의 거리에 할당하였음

그렇게 해서 (N-1, M-1)에 해당하는 거리 리스트를 확인하면 2개의 값이 나오는데
두 개의 값 중 적은 것을 선택하여 출력하고 만약 둘다 INF라면 -1을 출력하도록 하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

INF = float('inf')

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs():
    q = deque()
    q.append((0, 0, 0))
    distants = [[[INF, INF] for _ in range(M)] for _ in range(N)]
    distants[0][0] = [1, 1]
    while q:
        r, c, have_crashed = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == '0':
                    if distants[nr][nc][have_crashed] > distants[r][c][have_crashed] + 1:
                        distants[nr][nc][have_crashed] = distants[r][c][have_crashed] + 1
                        q.append((nr, nc, have_crashed))
                elif not have_crashed:
                    if distants[nr][nc][1] > distants[r][c][0] + 1:
                        distants[nr][nc][1] = distants[r][c][0] + 1
                        q.append((nr, nc, have_crashed + 1))
    # for row in distants:
    #     print(*row)
    return distants[N-1][M-1]

min_dist = bfs()
print(-1 if min_dist[0] == min_dist[1] == INF else min(min_dist))

"""
첫번째 반례
입력
2 4
0111
0010
출력
-1
정답
5
"""