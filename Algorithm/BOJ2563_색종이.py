"""
색종이의 크기가 100 * 100 이기 때문에 해당 크기의 2차원 배열을 이용하면 편하겠다 생각하여
하나의 원소를 1*1크기의 색종이라고 생각하면서 구현하였음
입력에 따라 해당 부분에 1을 채워넣고 마지막에 1의 개수를 세어 출력하였음
"""
import sys
input = sys.stdin.readline
N = int(input())

white_canvas = [[0] * 100 for _ in range(100)]

for _ in range(N):
    r, c = map(int, input().split())
    for i in range(r, min(r + 10, 100)):
        for j in range(c, min(c + 10, 100)):
            white_canvas[i][j] = 1

cnt = 0
for row in white_canvas:
    cnt += row.count(1)
    
print(cnt)