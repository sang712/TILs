"""
x, y좌표를 딕셔너리[셋] 구조로 저장해 쌍이 존재하는지 빠르게 찾을 수 있도록 하였음
x1과 x2가 정해졌으면 x1과 x2에 y1, y2가 있는지 확인해야할 뿐만아니라
x1, x2도 y1, y2에 존재하는지 확인해야 함

이분탐색도 문제유형으로 제시되었는데 이분탐색은 어디에 적용시켜야하는지 모르겠음
"""
import sys
input = sys.stdin.readline
N = int(input())
width, height = map(int, input().split())
xs = {}
ys = {}
for _ in range(N):
    x, y = map(int, input().split())
    xs.setdefault(x, set())
    xs[x].add(y)
    ys.setdefault(y, set())
    ys[y].add(x)

cnt = 0
for x1 in xs:
    x2 = x1 + width
    if x2 in xs:
        for y1 in xs[x1]:
            y2 = y1 + height
            if y2 in xs[x1] and y1 in xs[x2] and y2 in xs[x2]:
                cnt += 1
print(cnt)