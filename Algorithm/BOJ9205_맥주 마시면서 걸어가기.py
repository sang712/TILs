"""
페스티벌 장소까지 도달하는지 여부만 출력하면 되므로
접근 순서나 방문 횟수와 같이 다른 건 신경쓰지 않고 도달하는지 여부만 확인 하였음
visited 리스트를 따로 두지 않고 list내의 값을 지워나가는 방식으로 구현하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    convenience = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    
    q = deque()
    q.append(home)
    while q:
        from_x, from_y = q.popleft()
        if abs(festival[0] - from_x) + abs(festival[1] - from_y) <= 1000:
            print('happy')
            break
        for to_x, to_y in convenience:
            if abs(to_x - from_x) + abs(to_y - from_y) <= 1000:
                q.append((to_x, to_y))
                convenience.remove([to_x, to_y])
    else:
        print('sad')