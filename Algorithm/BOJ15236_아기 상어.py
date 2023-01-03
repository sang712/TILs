'''
접근 방식을 물고기의 위치를 받아와서 크기 별로 담아 놓고 
상어의 크기가 커질 때마다 먹을 수 있는 무리에 추가하는 방식으로 하려고 했는데
이 방식은 시간 초과가 나서
상어에서 bfs로 탐색해서 하나하나 먹는 방식으로 구현하도록 하겠음
굉장히 깔끔하게 구현했던 것 같은데 슬프네

처음에 문제의 조건을 하나 빠뜨린 것 때문에 문제를 처음부터 다시 풀게 되었고
문제의 조건을 잘 확인하여 빠뜨리지 않도록 하는 것이 중요하다는 것을 깨달았음

그리고 다음 위치를 큐에 추가할 때 중복될 수 있다는 점을 간과한 채 그냥 사용한 결과 시간초과가 나오게 되었음
'''
from collections import deque
N = int(input())

ocean = [list(map(int, input().split())) for _ in range(N)]

# 상어의 초기 위치 저장
shark_r, shark_c = 0, 0
for i in range(N):
    if 9 in ocean[i]:
        shark_r, shark_c = i, ocean[i].index(9)
        ocean[shark_r][shark_c] = 0

time = 0
size = 2
fish_eaten = 0

# 상어가 먹을 수 있는 물고기를 찾을 때 까지 반복
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while True:
    # 가장 가까운 거리의 물고기까지만 찾을 테니 메모리를 아끼기 위해 visited를 set으로 구현하였음
    visited = set()
    # 큐에는 위치 좌표와 거리를 튜플로 넣도록 하였음
    q = deque()
    # deque에는 첫 값을 튜플이나 리스트로 초기화가 불가능하여 append로 따로 넣어 주었음
    q.append((shark_r, shark_c, 0))
    min_dist = 100000
    bite_sized_fish = []
    # bfs 시작
    while q:
        r, c, dist = q.popleft()
        fish = ocean[r][c]
        # 원래는 여기에만 추가했었는데 큐에 삽입할 때 위치가 중복될 수 있다는 것을 간과하고 큐에 append하는 부분에도 추가하였음
        # 하단에 추가하고 나니 여기에는 더이상 필요없어서 삭제하여 4ms 단축하였음, 
        # 상어의 시작점을 1번 더 확인하는 것이 매 while문 마다 해당 구문을 실행하는 것보다 빠르다
        # visited.add((r, c)) 
        if 0 < fish < size: # 먹을 수 있는 물고기 발견하면
            if min_dist >= dist: # 해당 물고기까지의 거리를 저장하고
                bite_sized_fish.append((r, c)) # 해당 거리의 물고기의 위치를 따로 저장
                min_dist = dist
            continue # 여기서 다음 위치까지 더 나아가지 않도록 스킵
        if dist < min_dist: # 물고기를 발견하지 못 했거나, 물고기를 발견한 거리보다 짧은 거리의 위치라면 다음 위치 조사
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not (nr, nc) in visited:
                    if ocean[nr][nc] <= size:
                        visited.add((nr, nc)) # 시간초과의 구세주
                        q.append((nr, nc, dist + 1))
    # 먹을 수 있는 물고기를 모두 찾은 뒤의 처리
    if bite_sized_fish:
        bite_sized_fish.sort(key=lambda x: (x[0], x[1]))
        r, c = bite_sized_fish[0]
        ocean[r][c] = 0
        fish_eaten += 1
        time += min_dist
        shark_r, shark_c = r, c

        if fish_eaten == size:
            size += 1
            fish_eaten = 0
    # 먹을 수 있는 물고기를 못 찾았다면 엄마 상어 부르기
    else:
        break

print(time)