"""
게임의 종류에 따라 필요한 인원들을 임스를 제외하고 dict형태로 저장해 두었고
set 자료구조에 게임을 신청한 명단을 넣은 뒤에
개수를 게임에 필요한 인원수로 나누어 출력하도록 하였음
"""

import sys
input = sys.stdin.readline

games = {'Y': 1, 'F': 2, 'O': 3}

N, G = input().split()
players = set()
for _ in range(int(N)):
    players.add(input().strip())

print(len(players)//games[G])