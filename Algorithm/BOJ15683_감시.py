'''
쉬운 카메라 부분만 구현하고 막혀서 찾아봤더니
카메라의 길이로 dfs를 이용해서 구하면 됐음
4000ms 정도 걸렸는데, 좌표상에 표시하는 것이 아니라 
좌표를 set에 넣어 이용하면 더 빠른 시간에 해결 가능함
'''
import copy

N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctvs.append((office[i][j], i, j))
cctvs.sort(reverse=True)

cam_dir = {1: [[0], [1], [2], [3]],
           2: [[0, 2], [1, 3]],
           3: [[0, 1], [1, 2], [2, 3], [3, 0]],
           4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
           5: [[0, 1, 2, 3]]}
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def camera_works(cur_office, r, c, cam_dir):
    for d in cam_dir:
        dr, dc = delta[d]
        nr, nc = r + dr, c + dc
        while 0 <= nr < N and 0 <= nc < M and not cur_office[nr][nc] == 6:
            if cur_office[nr][nc] == 0:
                cur_office[nr][nc] = 8
            nr, nc = nr + dr, nc + dc
ans = 65
def dfs(depth, office):
    global ans
    if depth == len(cctvs):
        blind_spot = 0
        for row in office:
            blind_spot += row.count(0)
        ans = min(blind_spot, ans)
        return
    
    cur_office = copy.deepcopy(office)
    cam, r, c = cctvs[depth]
    for dir in cam_dir[cam]:
        camera_works(cur_office, r, c, dir)
        dfs(depth+1, cur_office)
        cur_office = copy.deepcopy(office)
                
dfs(0, office)
print(ans)