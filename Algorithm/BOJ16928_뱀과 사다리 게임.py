"""
다 풀고나선 이게 골드5? 라는 생각을 했는데
이어진 생각을 하고나니 이렇게 생각한 이유에 의문이 들었음
BFS로 풀어서 쉽게 구현이 가능했지만
과연 내가 BFS로 풀어야겠다고 생각해서 그렇게 풀었는지
분류를 보고 그렇게 생각했는지는 기억이 나지 않음

아무튼 1~6칸 앞선 부분의 칸을 탐색하고 
만약 해당 부분에 사다리나 뱀이 있다면 그것을 타고 이동하도록 구현하였음
그리고 혹시 몰라 94~99에 해당한다면 도중에 끝내도록 하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladders_n_snakes = dict()

for _ in range(N):
    x, y = map(int, input().split())
    ladders_n_snakes[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    ladders_n_snakes[u] = v

def snakes_n_ladder_game():
    q = deque()
    q.append((1, 0))
    visited = [0] * 101
    while q:
        pos, times = q.popleft()
        if visited[pos]:
           continue
        visited[pos] = 1
        for i in range(1, 7):
            next_pos = pos + i
            if next_pos in ladders_n_snakes:
                next_pos = ladders_n_snakes[next_pos]
            if next_pos >= 94:
                return times + 2
            elif next_pos < 100:
                q.append((next_pos, times + 1))
print(snakes_n_ladder_game())