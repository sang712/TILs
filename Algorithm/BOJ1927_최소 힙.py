'''
<11279 - 최대 힙>과 <11286 - 절댓값 힙>과는 다르게 
최소 힙을 구현한 heapq 라이브러리를 import하여 사용하였음
시간은 164ms 직접 구현한 것보다 더 빠르게 동작하였음
'''
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
