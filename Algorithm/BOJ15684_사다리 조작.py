"""
3달 전에 문제를 풀다가 시간 초과만 연속으로 떠서 포기했던 문제

구현 당시에 사다리의 발판이 놓인 곳을 set형태로 사용하였는데 시간초과가 났음
내가 생각하기로는 set이 오히려 더 낫다고 생각했는데 그게 아니었나봄
그래서 2차원 리스트로 발판 체크 배열을 만들었고
pypy3로 1000ms를 소요하면서 통과할 수 있었음

하나 하나 수정해가면서 set로 한 방식의 문제점을 찾았는데
가장 큰 문제점은 DFS 방식으로 진행할 때, 재귀를 돌 때마다 set을 새로 만드는 것이었음
그래서 해당 부분을 지우고 함수에 set 인자를 넘겨주지 않는 것으로 변경하니
pypy3에서 7000ms를 소요하면서 통과할 수 있었음

내가 생각하기에 set로 해도 그렇게 차이가 나지 않을 거라고 생각했는데 그게 아니었나봄
아마 set의 add, remove가 리스트의 값(1과 0) 할당보다 7배 정도 느린가봄

그리고 파이썬으로도 88ms로 통과한 코드를 발견했는데 
사다리의 각 열에는 짝수 개의 발판이 있어야 자기 자신으로 돌아갈 가능성이 있는데
홀수 개의 발판이 놓을 수 있는 발판보다 많으면 바로 취소하도록 하고
다른 열의 발판에 간섭을 안 받는 구간동안에는 어차피 똑같은 결과를 내므로 해당 부분을 건너뛰는 코드를 포함하고 있음

건너뛰는 코드는 어려운 것 같아서 홀수 개의 발판이 몇개인지 세도록 하여
불가능하다면 중간에 취소하는 방식을 넣었더니
pypy3에서는 168ms가 소요되었고 python3는 통과도 못하던게 184ms로 통과하게 되었음 야호! 
"""
N, M, H = map(int, input().split())
steps = [[0] * (N + 1) for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    steps[a][b] = 1

def is_cols_odd_less_than(n):
    cnt = 0
    for row in zip(*steps):
        cnt += sum(row) % 2
    return cnt <= 4 - n

def taking_ladder():
    for j in range(1, N+1):
        r, c = 0, j
        for r in range(1, H+1):
            if steps[r][c]:
                c += 1
            elif steps[r][c-1]:
                c -= 1
        if j != c:
            return False
    else:
        return True

ans = 4
def install_step(k, n):
    global ans
    if n >= ans or not is_cols_odd_less_than(n):
        return
    while k < (N-1) * H:
        i = k % H + 1
        j = k // H + 1
        if not steps[i][j] and not steps[i][j-1] and not steps[i][j+1]:
            steps[i][j] = 1
            if n < ans and taking_ladder():
                ans = min(ans, n)
            else:
                install_step(k+1, n+1)
            steps[i][j] = 0
        k += 1
if not is_cols_odd_less_than(0):
    pass
elif taking_ladder():
    ans = 0
else:            
    install_step(0, 1)  
print(ans) if ans < 4 else print(-1)

"""
import sys
input = sys.stdin.readline

N, M, H = map(int, input().rstrip().split())
ladders = [tuple(map(int, input().rstrip().split())) for _ in range(M)]

board = [[False for _ in range(N + 1)] for _ in range(H + 1)]
col_ladder_count = [0 for _ in range(N)]
for ladder in ladders:
    r, c = ladder
    board[r][c] = True
    col_ladder_count[c] += 1

answer = 4

def well_set():
    for c in range(1, N):
        col_res = c
        for r in range(1, H + 1):
            if board[r][col_res]:
                col_res += 1
            elif board[r][col_res - 1]:
                col_res -= 1
        if col_res != c:
            return False
    return True


def skip_iter(iterator, n):
    for _ in range(n):
        try:
            next(iterator)
        except StopIteration:
            break
    return


def set_ladder(ladder_count, curr_r, curr_c):
    global answer
    if ladder_count >= answer:
        return

    if well_set():
        answer = min(answer, ladder_count)
        return

    # 반드시 각 세로 구간에는 사다리가 "짝수"개가 위치해야 i -> i 도달 가능
    # == "홀수"개인 세로구간이 현재 놓을 수 있는 사다리보다 많다면 탐색할 필요 없음
    odd_ladder = sum(x & 1 for x in col_ladder_count)
    if odd_ladder <= 3 - ladder_count:
        for row in range(curr_r, H + 1):
            if row != curr_r:
                curr_c = 1
                
            # 한 번에 col을 2개 혹은 3개 스킵하기 위해서 이터레이터 구현
            col_iterator = iter(range(curr_c, N))
            for col in col_iterator:
                if board[row][col + 1]:
                    skip_iter(col_iterator, 2)
                elif board[row][col]:
                    skip_iter(col_iterator, 1)
                else:
                    board[row][col] = True
                    col_ladder_count[col] += 1
                    
                    set_ladder(ladder_count + 1, row, col + 2)
                    
                    col_ladder_count[col] -= 1
                    board[row][col] = False
    return

set_ladder(0, 1, 1)
print(answer if answer < 4 else -1)
"""