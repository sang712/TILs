import heapq
import sys
input = sys.stdin.readline

N = int(input())

h = []

for _ in range(N):
    x = int(input())
    
    if x:
        heapq.heappush(h, x)
    else:
        print(heapq.heappop(h)) if len(h) else print(0)
