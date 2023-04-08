"""
BFS로 쉽게 구현할 수 있는 문제였는데 pypy3로만 통과하는 문제가 있었음
한번 합쳐지지 않으면 주변에 변화가 없는 한 계속 안 합쳐지기 때문에
이를 탐색하는 부분을 제외하면 좀 더 빠르게 연산을 할 수 있을 것임
그래서 처음에는 연합된 부분이 평균으로 되어 차이가 나지 않을테니 제외하였는데
이럴 경우 한 연합과 다른 연합이 붙어있을 경우를 체크하지 못해 틀린답을 도출하게 되었음
그래서 반대로 연합에 포함되지 않은 나라를 제외하였고 python으로도 문제를 통과할 수 있었음
"""
import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def isUnion(r1, c1, r2, c2):
    return L <= abs(countries[r1][c1] - countries[r2][c2]) <= R

days = 0
stayed_still = [[0] * N for _ in range(N)]
while True:
    visitied = [[0] * N for _ in range(N)]
    q = deque()
    migration = 0
    for i in range(N):
        for j in range(N):
            if visitied[i][j]:
                continue
            if stayed_still[i][j]:
                continue
            q.append((i, j))
            visitied[i][j] = 1
            stayed_still[i][j] = 1
            popularity = 0
            union = []
            while q:
                r, c = q.popleft()
                union.append((r, c))
                popularity += countries[r][c]
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visitied[nr][nc] and isUnion(r, c, nr, nc):
                        q.append((nr, nc))
                        visitied[nr][nc] = 1
                        stayed_still[nr][nc] = 1
            if len(union) > 1:
                migration = popularity // len(union)
                while union:
                    r, c = union.pop()
                    countries[r][c] = migration
                    stayed_still[r][c] = 0
    if migration == 0:
        break
    days += 1
print(days)
            