import sys
input = sys.stdin.readline

N = int(input())
stage = [[0] * 500 for _ in range(500)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            stage[x][y] = 1

cnt = 0
for x in range(500):
    for y in range(500):
        if stage[x][y]:
            cnt += 1
print(cnt)