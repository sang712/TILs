"""
까다로운 구현문제

구현하면서 시행착오를 겪었던 부분을 적어보자면 다음과 같음
1. 가로, 세로는 당연히 검사하고 대각선을 검사하는데 대각선 하나만 하는 것이 아니라 두 방향 모두 해야함
2. 대각선을 검사할 때 좌하향 방향으로 검사하게 되면 가장 좌측에 있는 돌을 반환하기 어려워짐
3. 검사를 할 때 진행 방향의 직전에 같은 색상의 돌이 존재하는지 확인하면 6목에서 다음 걸 검사하면서 나오는 가짜 5목을 무시할 수 있음
4. 검사를 할 때 비슷한 작업을 반복하므로 delta와 같은 것을 선언하여 사용하면 코드 재사용 가능하면서 길이를 줄일 수 있고 
비슷한 코드들을 헷갈릴 필요가 없어져 실수를 줄일 수 있음

"""
board = [list(input().split()) for _ in range(19)]

delta = [(0, 1), (1, 0), (1, 1), (-1, 1)]
def check_5_in_a_row(r, c, color):
    for dr, dc in delta:
        if not (0 <= r - dr < 19 and 0 <= c - dc < 19) or board[r-dr][c-dc] != color:
            nr, nc = r, c
            for _ in range(1, 5):
                nr, nc = nr + dr, nc + dc
                if not (0 <= nr < 19 and nc < 19 and board[nr][nc] == color):
                    break
            else:
                nr, nc = nr + dr, nc + dc
                if not (0 <= nr < 19 and 0 <= nc < 19) or board[nr][nc] != color:
                    return r, c, color
    return r, c, ''

def solve():
    for i in range(19):
        for j in range(19):
            if board[i][j] != '0':
                r, c, color = check_5_in_a_row(i, j, board[i][j])
                if color:
                    print(color)
                    print(r + 1, c + 1)
                    return
    print('0')
    return
solve()