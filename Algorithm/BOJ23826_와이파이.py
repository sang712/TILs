"""
2차원 평면에 한 개의 소학습실이라는 공간과 여러개의 방이라는 공간이 있고
주인공이 방이라는 공간에서 공용와이파이를 사용하고자 한다.
따라서 핫스팟이 크지 않으면서 공용와이파이의 영역안에 드는 방을 찾는 문제

입력을 받아서 방에 공용 와이파이의 영향을 계산해 넣었고
반복문을 돌면서 핫스팟의 영향을 계산한 뒤에 결과를 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
x0, y0, E0 = map(int, input().split())

hot_spots = []
rooms = []
for _ in range(N):
    x, y, E = map(int, input().split())
    hot_spots.append((x, y, E))
    
    wifi_speed = max(0, E0 - abs(x - x0) - abs(y - y0))
    rooms.append([x, y, wifi_speed])
    
for idx, room in enumerate(rooms):
    x2, y2, E2 = room
    for x, y, E in hot_spots:
        E2 = rooms[idx][2]
        if E2:
            rooms[idx][2] = max(0, E2 - max(0, E - abs(x - x2) - abs(y - y2)))
        else:
            break
        
speed = list(map(lambda x: x[2], rooms))
max_speed = max(speed)

print(max_speed if max_speed else 'IMPOSSIBLE')