"""
입력을 받아서 정렬을 한 뒤에 역순으로 순차적으로 더하면서 B와 비교하였음
"""
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
H = sorted([int(input()) for _ in range(N)], reverse=True)

S = 0
for i in range(N):
    S += H[i]
    if S >= B:
        break
print(i+1)
