"""
가로를 세는 반복문과 세로를 세는 반복문을 따로 만들어 풀이하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [input() for _ in range(N)]

plank = 0
for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            plank += 1
            if j > 0 and floor[i][j - 1] == '-':
                plank -= 1

for j in range(M):
    for i in range(N):
        if floor[i][j] == '|':
            plank += 1
            if i > 0 and floor[i - 1][j] == '|':
                plank -= 1
                
print(plank)
