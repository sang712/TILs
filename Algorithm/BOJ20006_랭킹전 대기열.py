"""
문제에서 설명하는 대로 순서대로 구형하였음
먼저 플레이어 정보를 하나하나 받으면서
방이 없으면 방을 만들고
만들어진 방을 탐색하면서 해당 방에 들어갈 수 있으면 들어가고 아니면 다음 방을 확인하였음
모든 플레이어가 배정이 되었으면 각 방의 인원 수에 따라
게임이 시작된 방인지 아직 대기하는 방인지를 출력하고
플레이어의 닉네임으로 정렬된 순서로 해당 방에 참여한 플레이어를 출력하였음
"""
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
game = []
for _ in range(p):
    lev, player = input().split()
    lev = int(lev)
    for room in game:
        if len(room) < m and abs(lev - room[0][0]) <= 10:
            room.append((lev, player))
            break
    else:
        game.append([(lev, player)])
for room in game:
    print('Started!' if len(room) == m else 'Waiting!')
    print('\n'.join(map(lambda x: ' '.join((str(x[0]), x[1])), sorted(room, key=lambda x: x[1]))))