"""
낚시터의 크기와 상어의 개수를 입력으로 받음

상어의 위치, 속력, 이동 방향, 크기가 주어짐

낚시왕은 1초에 오른쪽으로 한 칸씩 이동하고 가장 오른쪽 칸을 넘으면 이동을 멈춤
이동 후에는 바로 땅에서 가장 가까운 상어를 잡고
상어는 이동함

상어는 주어진 속도로 이동, 칸/초 의 속도이며
격자판의 경계를 넘으면 방향을 반대로 바꿔서 속력을 유지한 채 움직임

상어가 이동한 뒤에 한 칸에 상어 두마리 이상이 있을 경우 크기가 큰 상어가 다른 상어를 다 잡아먹음

낚시왕이 잡은 상어의 크기의 합을 출력
"""
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
fishing_spot = [[0] * C for _ in range(R)]
sharks_info = {}
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks_info[z] = (r-1, c-1, s, d)
    fishing_spot[r-1][c-1] = z

delta = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

total_weight = 0
for c in range(C): # 낚시꾼 이동
    # 상어 잡기
    for r in range(R):
        shark_num = fishing_spot[r][c]
        if shark_num:
            total_weight += shark_num
            fishing_spot[r][c] = 0
            del sharks_info[shark_num]
            break
    
    # 상어 이동결과 예측
    moving_shark = {}
    for z, info in sharks_info.items():
        r, c, s, d = info
        nr, nc = r + s * delta[d][0], c + s * delta[d][1]
        cnt = 0
        while nr < 0 or nr > R - 1:
            if nr < 0:
                nr *= -1
                d = 2
            elif nr > R - 1:
                nr -= 2*(nr - R + 1)
                d = 1
        while nc < 0 or nc > C - 1:
            if d == 3 and nc >= C - 1:
                nc -= 2*(nc - C + 1)
                d = 4
            elif d == 4 and nc <= 0:
                nc *= -1
                d = 3
        moving_shark.setdefault(nr*101 + nc, [])
        moving_shark[nr*101 + nc].append((z, d))
    
    # 상어 끼리 잡아먹기
    for pos, weights in moving_shark.items():
        if len(weights) > 1:
            weights.sort()
            for z, _ in weights[:-1]:
                r, c, _, _ = sharks_info[z]
                fishing_spot[r][c] = 0
                del sharks_info[z]
        z, d = weights[-1]
        r, c, s, _ = sharks_info[z]
        fishing_spot[r][c] = 0
        r, c = pos // 101, pos % 101
        sharks_info[z] = (r, c, s, d)
        
    # 새 위치 상어 배치 
    for z, info in sharks_info.items():
        r, c, s, d = info
        fishing_spot[r][c] = z
    
print(total_weight)