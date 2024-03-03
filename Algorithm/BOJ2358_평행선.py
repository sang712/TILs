"""
x좌표, y좌표별로 등장 횟수를 카운팅 하고
카운팅 횟수가 2회 이상인 좌표를 카운팅해 출력하였음
"""
import sys
input = sys.stdin.readline
n = int(input())
horizontal = {}
vertical = {}
for _ in range(n):
    x, y = map(int, input().split())
    horizontal.setdefault(y, 0)
    horizontal[y] += 1
    vertical.setdefault(x, 0)
    vertical[x] += 1

print(sum([1 for x in vertical if vertical[x] >= 2]) +
    sum([1 for y in horizontal if horizontal[y] >= 2]))