"""
문제에서 요구하는대로 구현을 한다고 했지만 고려하지 않은 부분이 있어 다음과 같이 수정하였음

시작하자마자 틀리는 경우는 갈 수 있는 범위를 시작층부터 끝층으로 두어서 그렇고
30% 쯤에서 틀리는 경우는 시작층과 도착층이 같을 경우를 고려하지 않아서 그렇고
70% 쯤에서 틀리는 경우는 범위를 0층 부터 고려해서 그렇기 때문에 해당 부분을 수정하였음
"""
from collections import deque
F, S, G, U, D = map(int, input().split())

def move_with_elevator():
    while q:
        floor, num_clicks = q.popleft()
        if floor == G:
            break
        
        if floor + U <= F and not visited[floor + U]:
            visited[floor + U] = num_clicks + 1
            q.append((floor + U, num_clicks + 1))
            
        if floor - D >= 1 and not visited[floor - D]:
            visited[floor - D] = num_clicks + 1
            q.append((floor - D, num_clicks + 1))

    print(visited[G] if visited[G] else 'use the stairs')
    
if S == G:
    print(0)
else:
    q = deque()
    visited = [0] * (F + 1)
    q.append((S, 0))
    visited[S] = -1
    move_with_elevator()