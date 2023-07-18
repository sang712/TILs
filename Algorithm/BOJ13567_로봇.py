"""
굳이 로봇이 걸어다닐 2차원 리스트를 두지 않고 그냥 바로 값으로 확인하도록 하였음
input을 받아 다음 공간으로 이동시킨 후 자리가 유효한지 판단하는 과정을 거침
"""
import sys
input = sys.stdin.readline

M, n = map(int, input().split())

x = y = 0
dir = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
commands = [input().split() for _ in range(n)]
for command in commands:
    order, num = command
    if order == 'TURN':
        if num == '0':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
    elif order == 'MOVE':
        dist = int(num)
        dx, dy = delta[dir]
        nx, ny = x + dx * dist, y + dy * dist
        if 0 <= nx < M and 0 <= ny < M:
            x, y = nx, ny
        else:
            print(-1)
            break
else:
    print(x, y)
