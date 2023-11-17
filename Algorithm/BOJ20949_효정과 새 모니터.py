"""
인덱스 값과 가로 세로 값을 갖는 튜플 형태로 리스트에 저장해서 정렬하였음
정렬 식은 PPI를 구하는 공식에 음수를 취해서 적용하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

monitors = []
for i in range(1, N + 1):
    w, h = map(int, input().split())
    monitors.append((i, w, h))
    
monitors.sort(key=lambda x: (-(x[1] ** 2 + x[2] ** 2), x[0]))
ans = []
for idx, *_ in monitors:
    ans.append(idx)
print(*ans, sep='\n')