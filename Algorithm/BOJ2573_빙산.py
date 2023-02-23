"""
구현과 BFS가 섞인 문제로 문제에서 요구하는 대로 구현하였음
우선 빙산이 녹는 것을 melt라는 하나의 함수로 구현하였고
녹을 부분들을 다 계산하여 deque에 집어넣어 마지막에 한번에 처리하도록 하였음

그 후에 두 덩이로 나뉘었는지 확인하는 함수를 count_iceburg 함수로 구현하였음
의미없는 반복작업을 줄이기 위해 melt 함수에서 확실하게 자리 잡혀있는 빙산의 인덱스를 반환하도록 하였고
반환된 빙산의 인덱스를 이용해 count_iceburg 함수에서 해당 부분부터 BFS를 진행하도록 하였음
BFS를 마친 뒤에는 방문 리스트를 2중 for문으로 돌면서 방문 되지 않으면서 남아있는 빙산을 확인하도록 하였음

빙산이 모두 녹아버렸을 경우에는 count_iceburg 함수가 호출되지 않도록
처음에 빙산이 있는 칸의 수를 체크했었고
melt 함수에서 추가로 현재년도에 녹은 빙산의 수를 반환하도록 하였음

다른 사람들과 비슷하게 3000ms대인 3700ms가 나왔고
2000ms대로 진입하기 위해서 조금 더 고민해봐야겠음
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]

num_iceburg = 0
for i in range(N):
    for j in range(M):
        if ocean[i][j]:
            num_iceburg += 1

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def melt():
    """
    Returns:
        starting_i (int): -1 ~ N, row index of the first iceburg array elements that still frozen
        starting_j (int): -1 ~ M, column index of the first iceburg array elements that still frozen
        melted_off (int): number of melted iceburg array elements this year
    """
    melting_list = deque()
    for i in range(N):
        for j in range(M):
            if ocean[i][j]:
                seawater = 0
                for dr, dc in delta:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < M and not ocean[nr][nc]:
                        seawater += 1
                iceburg = ocean[i][j] - seawater
                if iceburg < 0:
                    iceburg = 0
                melting_list.append((i, j, iceburg))
    
    melted_off = 0
    starting_i, starting_j = -1, -1
    while melting_list:
        i, j, iceburg = melting_list.popleft()
        ocean[i][j] = iceburg
        if not iceburg:
            melted_off += 1
        else:
            starting_i, starting_j = i, j
    return starting_i, starting_j, melted_off

def count_iceburg(starting_i, starting_j):
    """
    Args:
        starting_i (int): 0 ~ N, row index of the first iceburg array elements that still frozen
        starting_j (int): 0 ~ N, column index of the first iceburg array elements that still frozen
    Returns:
        is_more_than_two_junks (bool): whether the iceburg is devided to 2 or not
    """
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((starting_i, starting_j))
    visited[starting_i][starting_j] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = 1
                if ocean[nr][nc]:
                    q.append((nr, nc))
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if ocean[i][j]:
                    return True
    return False
            

year = 1
while True:
    starting_i, starting_j, melted_off = melt()
    num_iceburg -= melted_off
    if num_iceburg <= 0:
        print(0)
        break
    elif count_iceburg(starting_i, starting_j):
        print(year)
        break
    # print('>>>>>>>>', year)
    # print(*ocean, sep='\n')
    # print('<<<<<<<<')
    year += 1
    
    