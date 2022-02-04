dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def recursion(sel, _po_idx): # 포가 이동한 횟수, 포가 이동한 위치
    if sel == 3: # 이동횟수가 3번이면 리턴
        return
    for d in range(4): # 4방향으로 탐색함
        nr = _po_idx[0] + dr[d]
        nc = _po_idx[1] + dc[d]

        # 뛰어 넘는 부분
        while 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
            # 보드를 벗어나지 않으며 장기알을 만나지 않으면 계속 진행
            nr += dr[d]
            nc += dc[d]
        # 탈출을 하게되면 포는 그 알을 뛰어 넘어야 하기 때문에 한 칸 더 이동
        nr += dr[d]
        nc += dc[d]

        # 알을 잡는 부분
        while 0 <= nr < N and 0 <= nc < N: # 보드를 벗어 나지 않고
            if board[nr][nc]: # 뛰어 넘은 곳에 장기알이 놓여 있으면
                board[nr][nc] = 0 # 장기알을 잡고
                visited.add((nr, nc)) # 해당 위치를 visited에 추가
                recursion(sel + 1, (nr, nc)) # 그 위치에서 또 뛰어 넘기 실행
                board[nr][nc] = 1 # 잡은 장기알을 되돌림
                break # 알을 잡은 순간 그 자리에서 다시 뛰어 넘어야 되므로 반복문 종료
            else: # 빈 공간으로 뛰어 넘은 경우
                recursion(sel + 1, (nr, nc))

            # 다음 칸으로 뛰어 넘었다고 생각하고 반복문 진행
            nr += dr[d]
            nc += dc[d]


for tc in range(int(input())):
    N = int(input()) # 보드의 사이즈
    po_idx = 0 # 포의 위치
    board = [] # 장기말판
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 2: # 포의 위치를 찾으면
                tmp[j] = 0 # 포의 위치를 0으로 두고
                po_idx = (i, j) # 포의 위치 인덱스를 튜플로 받음
        board.append(tmp)

    visited = set() # 중복되는 값을 피하기 위해 set으로 정함
    recursion(0, po_idx) # 재귀를 통해 풀기

    print("#{} {}".format(tc + 1, len(visited)))