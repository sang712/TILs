"""
입력에서 중복되는 숫자를 사용하는 경우를 거르지 않는 다는 것을 간과하고 
그냥 문제풀이를 하여 틀렸었음
그냥 마방진이 되기 위해 N이 3일 때 모두 5로 입력이 들어오는 경우도 있음
"""
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
num_check = set(range(1, N + 1))

expected_sumation = N * (N ** 2 + 1) // 2

answer = 'TRUE'

for row in matrix:
    num_check.difference_update(row)
    if sum(row) != expected_sumation:
        answer = 'FALSE'
        break
else:
    if num_check:
        answer = 'FALSE'
    for col in zip(*matrix):
        if sum(col) != expected_sumation:
            answer = 'FALSE'
            break
    else:
        diag_rd = 0
        diag_ld = 0
        for i in range(N):
            diag_ld += matrix[i][N - 1 - i]
            diag_rd += matrix[i][i]
        if not(diag_rd == diag_ld == expected_sumation):
            answer = 'FALSE'
print(answer)
    