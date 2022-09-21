from collections import deque

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
# 방문 리스트 빨간공, 파란공 [빨r, 빨c, 파r, 파c]
visited = [[[[0]*M for b in range(N)] for rc in range(M)] for rr in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌
# bfs를 사용할 것이기 때문에 deque를 사용
q = deque()

# board를 for문으로 돌며 빨간 공과 파란 공의 위치 파악, 시작 위치 q에 추가
def init():
    rr, rc, br, rc = [0] * 4
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rr, rc = i, j
            elif board[i][j] == 'B':
                br, bc = i, j
    q.append((rr, rc, br, bc, 0))
    visited[rr][rc][br][bc] = 1

# 해당 방향으로 계속 이동하도록 하는 함수, 공의 색과 상관없이 재사용 가능하도록
def move(r, c, dr, dc):
    moving = 0
    # 다음 자리가 벽이거나 해당 자리가 구멍일 경우 좌표와 이동 횟수 반환
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        moving += 1
    return r, c, moving


def solve():
    init()
    while q:
        rr, rc, br, bc, count = q.popleft()
        if count >= 10:
            break # dfs면 continue를 쓰겠지만 bfs이므로 break
        for dr, dc in delta:
            # board를 건드릴 필요 없이 이동 후의 좌표를 받아와서 사용
            nrr, nrc, rmoving = move(rr, rc, dr, dc)
            nbr, nbc, bmoving = move(br, bc, dr, dc)
            # 파란 공이 구멍에 빠지면 다음 조건
            if board[nbr][nbc] == 'O': # 조건을 역으로 하고 하단의 코드를 하위로 넣으면 프루닝 가능
                continue
            # 빨간 공이 구멍에 빠지면 리턴
            if board[nrr][nrc] == 'O':
                print(1)
                return
            # 둘이 붙어 있는 상태에서 움직였다면 둘의 이동거리가 같을 것이고
            # 둘이 떨어져 있는 상태이더라도 뒤따라 오는 것의 이동거리가 항상 클테니까
            # 둘이 같은 좌표가 되면 좀 더 멀리 이동한 공을 한 칸 뒤로
            if nrr == nbr and nrc == nbc:
                if rmoving > bmoving:
                    nrr, nrc = nrr-dr, nrc-dc
                else:
                    nbr, nbc = nbr-dr, nbc-dc
            # 움직였지만 어느 공도 구멍에 빠지지 않았다면 다음 deque에 추가
            if not visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = 1
                q.append((nrr, nrc, nbr, nbc, count+1))
    print(0)
solve()