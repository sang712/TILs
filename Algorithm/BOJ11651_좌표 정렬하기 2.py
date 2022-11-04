'''
주어진 조건대로 lambda를 사용하여 정렬하였음
'''
import sys
input = sys.stdin.readline

N = int(input())
poss = []
for _ in range(N):
  poss.append(tuple(map(int, input().split())))

poss.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
  print(*poss[i])
