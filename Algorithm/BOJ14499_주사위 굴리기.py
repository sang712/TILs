'''
주어진 값을 다 받고 계산 편하게 delta를 0번째 칸이 비워진 길이 5의 리스트로 사용,
제한 조건대로 번호와 index를 매칭하여 동서북남 순서로 설정함
주사위 가로둘레와 세로둘레로 봤을 때 4개씩 묶이며
각각 밑칸으로 시작해서 오른쪽, 아래쪽으로 펼쳐진 전개도를 생각하며 4개 길이의 리스트로 만들어 줌
이 때 각 둘레를 봤을 때 주사위의 아랫칸과 윗칸은 공유되므로
0, 3번 인덱스의 숫자는 함께 변한다는 것에 주목하였음
"그리고 지도를 지날 때 지도에 숫자가 있으면 주사위에 붙어서 지도에선 없어지고
지도에 0이 있으면 주사위의 숫자가 복사된다는 점을 조건으로 넣어 구현하였음"
위의 조건을 제대로 읽지 않아서 시간을 조금 낭비했기때문에 
다음에는 문제를 보면서 구현하는 것이 아니라
한 번 다 훑고 시작해야 되겠음
'''
N, M, x, y, K = map(int, input().split())

mapa = [list(map(int, input().split())) for _ in range(N)]

order = list(map(int, input().split()))
delta = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남
ve_dice = [0] * 4
ho_dice = [0] * 4

def move(r, c, d):
    global ve_dice, ho_dice
    dr, dc = delta[d]
    nr, nc = r + dr, c + dc
    if 0 <= nr < N and 0 <= nc < M:
        if d <= 2:
            if d == 1:
                ho_dice = ho_dice[1:] + [ho_dice[0]]
            elif d == 2:
                ho_dice = [ho_dice[-1]] + ho_dice[:-1]
            ve_dice = [ho_dice[0], ve_dice[1], ho_dice[2], ve_dice[3]]
        elif d > 2:
            if d == 4:
                ve_dice = ve_dice[1:] + [ve_dice[0]]
            elif d == 3:
                ve_dice = [ve_dice[-1]] + ve_dice[:-1]
            ho_dice = [ve_dice[0], ho_dice[1], ve_dice[2], ho_dice[3]]
        if mapa[nr][nc] > 0:
            ho_dice[0], ve_dice[0] = mapa[nr][nc], mapa[nr][nc]
            mapa[nr][nc] = 0
        else:
            mapa[nr][nc] = ho_dice[0]
        print(ho_dice[2])
        return nr, nc
    return r, c
            
def solve():
    r, c = x, y
    for d in order:
        r, c = move(r, c, d)
solve()