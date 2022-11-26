'''
BFS 방식을 이용하여 진행하였고 어차피 한 번에 익게 해야하기 때문에
큐를 사용하든 스택을 사용하든 상관 없어서 그냥 list를 사용하였음
입력을 받고 순회를 하면서 익은 토마토를 list에 저장하였고
list의 값을 pop으로 꺼내면서 상하좌우의 값이 안 익은 토마토이면 set에 저장하였음
set의 값을 사용하기 전에 이 값을 아까의 그 list에 얕은 복사하여 저장하고
set의 값을 이용해서 한 번에 토마토를 익게 함
이 과정을 반복하여 list에 남는 것이 없을 때까지 진행하고
다시 토마토 배열을 순회하여 0이 있으면 -1 아니면 cnt를 반환하도록 함
마지막에 변한 토마토도 list에 추가되기 때문에 cnt에 -1을 하였음
----
내 코드는 2300ms대, 1등 코드는 900ms대라 확인해봤는데
마지막의 순회를 하지 않으려고 처음에 안 익은 토마토의 개수를 세서
익힐 때마다 1씩 빼주는 방법을 사용하였고 0일 때 cnt를 반환하고 
그게 아니라면 -1을 반환하는 방식으로 되어있음
----
위 방식으로 해도 시간이 오래 걸림
다시 해당 코드를 살펴보니 2차원 배열이 아닌 
1차원 배열로 펼쳐서 사용하였기 때문에 빨라진 듯

근데 백준도 LeetCode처럼 시간대별로 측정시간이 달라지는 문제가 있어보임
'''
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

ripe_tomatoes = []
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            ripe_tomatoes.append((i, j))

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]            
def ripen_tomatoes():
    global ripe_tomatoes
    next_tomato = set()
    while ripe_tomatoes:
        r, c = ripe_tomatoes.pop()
        for d in delta:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] == 0:
                next_tomato.add((nr, nc))
    ripe_tomatoes = list(next_tomato)
    while next_tomato:
        nr, nc = next_tomato.pop()
        tomatoes[nr][nc] = 1

cnt = 0
while ripe_tomatoes:
    cnt += 1        
    ripen_tomatoes()

for i in range(N):
    if tomatoes[i].count(0):
        print(-1)
        break
else:
    # 마지막에 변한 토마토를 기준으로 한 번 더 탐색하므로 -1하고 출력
    print(cnt-1)
            
