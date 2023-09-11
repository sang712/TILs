"""
리스트의 원소별로 불러올 때 계산하기 편하게 enumerate를 이용하였음
"""
import sys
input = sys.stdin.readline

group = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    print(f'Group {group}')
    
    children = [input().split() for _ in range(n)]
    nasty = []
    for i, child in enumerate(children):
        name, *messages = child
        for j, message in enumerate(messages):
            if message == 'N':
                nasty.append(f'{children[(i-j-1)%n][0]} was nasty about {name}')
    if nasty:
        print(*nasty, sep='\n')
    else:
        print('Nobody was nasty')
    print()
    group += 1
    