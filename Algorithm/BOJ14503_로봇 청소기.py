'''
로봇 청소기가 바라보는 방향의 왼쪽으로 이동하기 때문에 
델타를 d를 인덱스로 갖으면서 d방향의 왼쪽을 가리키게끔 설정하였음
이렇게 되면 for문으로 range(4)를 돌리게 되면 시계 방향으로 판단하기 때문에 
range(4, 0, -1)로 돌려서 적용하였고
for-else 구문으로 청소가 되지 않은 공간이 있으면 for에서 탈출 하는 조건을 설정하여
else에서는 후진을 하는 부분으로 처리하였음
queue를 굳이 쓰지 않고도 재귀로 풀 수 있는 문제라 queue없이 구현해보기
'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 좌상우하 (북동남서의 왼쪽)

space = [list(map(int, input().split())) for _ in range(N)]

q = [(r, c, d)]
space[r][c] = 2

def solve():
    while q:
        r, c, d = q.pop(0)
        for i in range(4, 0, -1):
            dr, dc = delta[(d+i)%4]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if space[nr][nc] == 0:
                    space[nr][nc] = 2
                    q.append((nr, nc, (d+i-1)%4))
                    break
        else:
            dr, dc = delta[(d+3)%4]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not space[nr][nc] == 1:
                    q.append((nr, nc, d))
        # print(r, c, d)
        # for row in space:
        #     print(row)

solve()
cnt = 0
for row in space:
    cnt += row.count(2)                 
    # print(row)
print(cnt)