"""
출력 조건을 틀려서 문제를 틀렸음
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

list_from = []
list_to = []
for _ in range(N):
    row = input().strip()
    temp = []
    for s in row:
        if s.isdigit():
            temp.append(int(s))
    list_from.append(temp)
    
for _ in range(N):
    row = input().strip()
    temp = []
    for s in row:
        if s.isdigit():
            temp.append(int(s))
    list_to.append(temp)
    
def reverse(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            list_from[i][j] = (list_from[i][j] + 1) % 2

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if list_from[i][j] != list_to[i][j]:
            reverse(i, j)
            ans += 1
if list_from == list_to:
    print(ans)
else:
    print(-1)