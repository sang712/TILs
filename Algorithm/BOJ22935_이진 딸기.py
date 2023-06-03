"""
문제가 요구하는 이진수가 1에서 15, 15에서 1로 돌아가는 규칙을 갖는데
이 규칙을 구현하는 방법을 찾는 도중에 고려하지 못한 부분이 생겨
중간 중간 오답을 도출하는 풀이를 하였음
해당 문제는 1에서 14 회를 주기로 수가 늘어났다 줄어들었다 하므로
1을 뺀 뒤에 28로 모듈연산을 하고 14보다 수가 커졌을 때는
28에서 해당 수를 빼는 방법으로 구하였음
"""
import sys
input = sys.stdin.readline

binary_strawberry = ['VVV딸기', 'VV딸기V', 'VV딸기딸기', 'V딸기VV',
                     'V딸기V딸기', 'V딸기딸기V', 'V딸기딸기딸기', '딸기VVV',
                     '딸기VV딸기', '딸기V딸기V', '딸기V딸기딸기', '딸기딸기VV',
                     '딸기딸기V딸기', '딸기딸기딸기V', '딸기딸기딸기딸기']

for _ in range(int(input())):
    turn = (int(input()) - 1) % 28
    if turn > 14:
        turn = 28 - turn
    print(binary_strawberry[turn])
