'''
n-queens 문제
2차원 리스트로 선언할만한 내용을 인덱스를 행의 넘버로 갖고 원소를 열의 인덱스로 갖는 1차원 리스트에 담는 방법으로
메모리와 시간복잡도를 줄일 수 있음

rows[r] == rows[i]는 같은 열에 있는지 확인하는 것이고 
-> (for문으로 확인하는 것보다 in으로 확인하는 것이 빠를 거 같아서 수정함)
r - i == abs(rows[r] - rows[i]) 는 대각선에 있는지 확인하는 것
abs(r - rows[r]) == abs(i - rows[i]) 로 해도 되는데 abs 연산을 하나 줄일 수 있어서 위와 같이 작성함

시간을 줄일 수 있는 방법을 아무리 적용해봐도 시간 초과가 남
통과하고 시간을 줄였다고 올린 블로그글을 적용해봐도 pypy로 올려놓고 pypy썼다는 것을 명시 안 하는 낚시글들 뿐
어떻게 하면 다른 사람들처럼 python3으로도 통과를 할 수 있을까 고민이 됨

python3으로 통과를 한 사람들의 답안을 확인해보면
N이 짝수일 때는 좌우 대칭이므로 절반만 체크해서 *2하면 된다는 글이 있는데 이게 첫번째 row만 해당하는 것인지
아니면 N*N//2 에 해당하는 행렬을 만들어 적용한다는 말인건지 잘 분간이 안 됨
(첫번째 row만 절반으로 하는 것을 시도해봤으나 시간초과)

아무튼 pypy3로 22376ms를 소요하여 정답 제출을 완료하였음
'''
N = int(input())

ans = 0
rows = [0] * N


def are_queens_checked(r: int) -> bool:
    '''
    r번째 row에 있는 queen이 다른 row에 있는 queen에 방해되는지 확인하는 함수
    '''
    if rows[r] in rows[:r]:
        return False
    for i in range(r):
        if r - i == abs(rows[r] - rows[i]):
            return False
    return True

def put_queen_at_row_number(r: int) -> None:
    '''
    r번째 row, c번째 col에 queen을 놓는 재귀 함수
    '''
    for c in range(N):
        rows[r] = c
        if are_queens_checked(r):
            if r + 1 == N:
                global ans
                ans += 1
                return
            put_queen_at_row_number(r + 1)

put_queen_at_row_number(0)
print(ans)