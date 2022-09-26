'''
함수에 리스트를 인자로 넣어도 얕은 복사다

원래 구상은 solve 함수에 building_walls 함수와 spreading 함수를 같이 넣는 거였는데
spreading 함수를 q를 이용해 구현하고, building_walls 함수를 구현하는데
building_walls에서 완성한 연구실 list를 쓰려면 building_walls 내부에서 spreading을 콜해야 돼서
solve 함수는 없애고 다음과 같이 완성하였음
spreading은 queue를 이용한 bfs
building_walls는 재귀를 이용하였음
시간 초과 나서 queue를 deque로,
2중 for문에서 1중 for문+list.count()로 바꾸었음
결국 pypy로 시도하여 해결
찾아보니 벽 세우기를 재귀로 하지 않고 조합으로 푼 사람이 있어서 해당 내용 시도 요망
'''
from collections import deque
import copy

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

starting_q = []

for r in range(N):
    for c in range(M):
        if lab[r][c] == 2:
            starting_q.append((r,c))

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상

ans = 0
def building_walls(count):
    if count == 3:        
        spreading()
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                building_walls(count+1)
                lab[i][j] = 0
                

def spreading():
    q = deque(pos for pos in starting_q)
    lab_for_test = copy.deepcopy(lab)
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            if 0 <= r + dr < N and 0 <= c + dc < M:
                if lab_for_test[r+dr][c+dc] == 0:
                    lab_for_test[r+dr][c+dc] = 2
                    q.append((r+dr, c+dc))
    safe_space = 0
    for row in lab_for_test:
        safe_space += row.count(0)
    global ans
    ans = max(ans, safe_space)
    
building_walls(0)
print(ans)