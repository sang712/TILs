"""
x좌표 y좌표가 차례로 끝 값, 첫 값을 반복한다는 것을 발견해서
해당 방식을 그대로 구현하였음 pop()과 pop(0)를 해야하기 때문에 deque를 사용하였음
어느 한 쪽의 deque가 비게 되면 while문을 탈출하도록 하였음
"""
from collections import deque

N, M = map(int, input().split())
horizontal = deque(range(N))
vertical = deque(range(1, M))

x, y = 0, 0
left_right = 1
up_down = 1
while True:
    if horizontal:
        if left_right == 1:
            x = horizontal.pop()
        else:
            x = horizontal.popleft()
        left_right *= -1
    else:
        break
    
    if vertical:
        if up_down == 1:
            y = vertical.pop()
        else:
            y = vertical.popleft()
        up_down *= -1
    else:
        break
print(x, y)