"""
백준에서 처음으로 영어로 된 문제를 풀어보았음
이해는 대부분 되는데 제한 조건과 같은 수학적 용어가 긴가민가해서 자존심 상하지만 번역기를 돌렸음
문제는 쉬운 편으로
N개의 기계를 N-1개의 컨베이어로 엮었는데 이 때 모든 기계와 연결된 하나의 기계가 있나 확인하는 문제였음
그래프 탐색으로 문제를 구현하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [set() for _ in range(N + 1)]

for _ in range(N - 1):
    start, end = map(int, input().split())
    graph[end].add(start)

for i in range(1, N + 1):
    visited = set()
    visited.add(i)
    q = deque()
    q.append(i)
    while q:
        current = q.popleft()
        for next in graph[current]:
            if not next in visited:
                q.append(next)
                visited.add(next)
    if len(visited) == N:
        print(i)
        break
else:
    print(-1)
