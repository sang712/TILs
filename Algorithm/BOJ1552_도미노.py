"""
우선 입력되는 값이 0~9, A~I로 이를 파싱할 수 있도록 딕셔너리를 만들었음

그리고 같은 행, 같은 열에서 하나씩만 선택해야하기 때문에 굳이 2중 for문을 사용하지 않고
행마다 하나를 선택하고 넘어가고 하는 방식으로 구현했고
선택한 열이 중복되지 않도록 선택한 열의 번호를 저장하는 selected 변수를 사용했음
선택이 다 됐다면 어쨌든 사이클로만 이루어졌을 것이므로
해당 선택된 조합을 순차적으로 돌면서 사이클의 개수가 몇개인지 판단하는 동시에
각각의 도미노가 가진 수를 곱하였음
마지막에는 사이클에 개수에 따라 -1을 곱하거나 아니거나 해서 최대 점수와 최소 점수를 구하였음

꽤나 오랜 시간이 걸린 문제라 이런 조합을 구하는 문제를 빠르게 구현하고 익숙해지도록 해야겠음
"""

N = int(input())
str_to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': -1, 'B': -2, 'C': -3, 'D': -4, 'E': -5, 'F': -6, 'G': -7, 'H': -8, 'I': -9}
board = [list(map(lambda x: str_to_int[x], input())) for _ in range(N)]

cycle_sets = []

def find_cycle(n, comb):
    if n >= N:
        cycle_sets.append(comb)
        return
    for i in range(N):
        if selected[i]:
            continue
        selected[i] = 1
        find_cycle(n+1, comb + [(n, i)])
        selected[i] = 0
selected = [0] * N
find_cycle(0, [])

def check_cycle(domino):
    left, right = domino
    if not checked[left]:
        checked[left] = 1
        check_cycle(cycle_set[right])
    return
            
max_point, min_point = -9**6, 9**6
for cycle_set in cycle_sets:
    cycles = 0
    checked = [0] * N
    points = 1
    for domino in cycle_set:
        left, right = domino
        if not checked[left]:
            check_cycle(domino)
            cycles += 1
        points *= board[left][right]
    parity = 1 if cycles % 2 else -1
    points *= parity
    max_point = max(max_point, points)
    min_point = min(min_point, points)
print(min_point, max_point, sep='\n')