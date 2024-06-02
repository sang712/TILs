"""
행당 구름 정보를 -1로 가지고 있으면서
c라는 문자열을 만나면 0으로 초기화 하고 매번 방문한 지역을 해당 수로 초기화하였음
"""
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
joi = [list(input().strip()) for _ in range(H)]

for r in range(H):
    cloud = -1
    for c in range(W):
        if joi[r][c] == 'c':
            cloud = 0
        joi[r][c] = cloud
        cloud += 1 if cloud >= 0 else 0
for row in joi:
    print(*row)