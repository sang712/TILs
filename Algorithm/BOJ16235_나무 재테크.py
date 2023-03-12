"""
NxN의 땅
r, c는 1부터 시작
처음 양분은 모든 칸에 5만큼
M개의 나무를 심었고
여러 개의 나무가 심어져 있을 수 있음
나이만큼 양분을 먹고 나이가 1 증가
양분을 못 먹은 나무는 죽음
죽은 나무는 양분으로 되며 죽은 나무의 나이 //2가 양분으로 추가됨

나이가 5의 배수인 나무는 번식을 하며 인접한 8칸에 나이가 1인 나무가 추가됨

각 칸에 A[r][c]만큼의 양분이 추가됨

살아있는 나무의 개수 출력

pypy3로만 통과하였음
나무를 나이를 키값으로 갖는 딕셔너리 형태로 저장하면 python으로도 통과 됨
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

nourishment = [[5] * N for _ in range(N)]

for _ in range(K):
    # 봄
    dead_tree = []
    propagation = []
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])-1, -1, -1):
                tree = trees[i][j][k]
                if nourishment[i][j] >= tree:
                    nourishment[i][j] -= tree
                    trees[i][j][k] = tree + 1
                    if (tree + 1) % 5 == 0:
                        propagation.append((i, j))
                else:
                    dead_tree.append((i, j, trees[i][j].popleft()))
                    
    # 여름
    while dead_tree:
        r, c, age = dead_tree.pop()
        nourishment[r][c] += age // 2
        
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # 가을
    while propagation:
        r, c = propagation.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                trees[nr][nc].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            nourishment[i][j] += A[i][j]

num_trees = 0
for i in range(N):
    for j in range(N):
        num_trees += len(trees[i][j])
        
print(num_trees)