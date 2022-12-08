'''
이전에 풀었던 동명의 문제 BOJ7576과 같은 방법으로 풀었음
둘 다 시간복잡도가 100만으로 동일함

우선 H, N, M 순으로 인덱스를 갖는 3차원 리스트에 입력을 저장하고
H, N, M 순으로 for문을 돌면서 이미 익은 토마토의 위치를 따로 저장함
다음 일을 하는 함수를 새로 만듦
익은 토마토의 주변을 델타를 이용해 탐색하고 익지 않은 토마토가 있다면 set에 저장함
set에 저장한 익지 않은 토마토의 위치는 익은 토마토의 위치를 저장한(현재는 빈) 리스트에 저장하고
set의 값을 하나씩 꺼내면서 익지 않은 토마토를 익도록 변환함

그 후에 while문에서 추가로 익어야 하는 토마토가 있는지 확인하면서 위의 함수를 호출하고 카운팅함
추가로 익어야 하는 토마토가 없을 때 멈춤
다시 토마토들을 확인하면서 0이 남아있는지 체크하고 만약 남아있다면 -1을 출력함
그 외의 경우는 cnt를 출력함
마지막으로 익은 토마토를 기준으로 확인하기 때문에 cnt가 1번 더 더해져서 cnt에 -1을 하여 출력함
2352ms 소요됨
BOJ7576과 비교했을 때 4ms 빠름
'''
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

ripe_tomatoes = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                ripe_tomatoes.append((h, n, m))

delta = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
def ripen_tomatoes():
    global ripe_tomatoes
    next_tomato = set()
    while ripe_tomatoes:
        h, r, c = ripe_tomatoes.pop()
        for d in delta:
            nh, nr, nc = h+d[0], r + d[1], c + d[2]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tomatoes[nh][nr][nc] == 0:
                next_tomato.add((nh, nr, nc))
    ripe_tomatoes = list(next_tomato)
    while next_tomato:
        nh, nr, nc = next_tomato.pop()
        tomatoes[nh][nr][nc] = 1

def check_all_ripe():
    cnt = 0
    while ripe_tomatoes:
        cnt += 1        
        ripen_tomatoes()

    for h in range(H):
        for n in range(N):
            if tomatoes[h][n].count(0):
                print(-1)
                return
    # 마지막에 변한 토마토를 기준으로 한 번 더 탐색하므로 -1하고 출력
    print(cnt-1)
check_all_ripe()