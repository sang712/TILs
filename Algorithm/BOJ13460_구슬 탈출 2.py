'''
N과 M을 받고 board도 받음
bfs를 사용할 것이니 delta를 정하고
방문리스트도 만들기, 방문 리스트는 빨간공, 파란공 좌표로 4차원 리스트를 사용
bfs니 큐를 사용하고, 큐대신 더 효율적인 데크를 사용
보드를 돌면서 빨간 공과 파란공의 위치 확인
데크에 빨간공, 파란공, 반복회수를 넣어 저장
큐를 와일문으로 돌고, 내부에서 팝으로 하나씩 꺼냄
꺼내서 델타 적용시켜서 상하좌우로 움직임
상하좌우로 움직이는 것은 따로 함수를 만들어 빨간공 파란공 상관없이 적용할 수 있도록
움직이는 함수는 이동 칸수를 계산하여 서로 겹쳤을 때 한 칸 뒤로 무르도록 만들기
파란공이 빠지면 무시하고 빨간공이 들어가면 리턴으로 반복회수 반환
만약 둘 다 조건에 걸리지 않으면 방문했는지 확인하고 방문 안 했으면 큐에 추가
'''
from collections import deque

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 방문 리스트 [빨r][빨c][파r][파c]
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque()

# 구슬 좌표 확보
def init():
    rr, rc, br, bc = [0] * 4
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rr, rc = i, j
            elif board[i][j] == 'B':
                br, bc = i, j
    # 빨간 공 좌표, 파란공 좌표, 반복 횟수
    q.append((rr, rc, br, bc, 1)) # 카운트는 1부터 적용
    visited[rr][rc][br][bc] = 1
    
# 구슬 움직이기 
def move(r, c, dr, dc):
    moving = 0
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        moving += 1
    return r, c, moving

# bfs 문제 풀이
def solve():
    init()
    while q: # bfs 큐를 돌기 때문에 while을 사용
        rr, rc, br, bc, count = q.popleft()
        # 10회 이상 반복하면 -1 반환
        if count > 10:
            return -1 
        for dr, dc in delta:
            nrr, nrc, rmoving = move(rr, rc, dr, dc)
            nbr, nbc, bmoving = move(br, bc, dr, dc)
            if board[nbr][nbc] != 'O': # 파란 구슬이 구멍에 빠지면 무시
                if board[nrr][nrc] == 'O': # 빨간 구슬이 구멍에 빠지면
                    return count # 카운트 반환
                # 둘의 위치가 겹치면 더 멀리 간 공을 한 칸 뒤로 물림
                if nrr == nbr and nrc == nbc:
                    if rmoving > bmoving:
                        nrr, nrc = nrr-dr, nrc-dc
                    else:
                        nbr, nbc = nbr-dr, nbc-dc
                # 방문하지 않았을 때만 q에 추가
                if not visited[nrr][nrc][nbr][nbc]:
                    visited[nrr][nrc][nbr][nbc] = 1
                    q.append((nrr, nrc, nbr, nbc, count+1))
    # while문이 그냥 끝나면 -1 반환
    return -1
print(solve())