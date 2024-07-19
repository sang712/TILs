"""
최단 거리를 구하면서 그 최단 거리가 특정 수인 위치를 찾는 문제인데
다익스트라가 생각났지만 어차피 노드간의 거리가 모두 1로 같아서
그냥 BFS로 탐색하면서 답에 해당하는 도시 번호를 모아 출력하였음
출력에 *를 사용하면서 if-else 구문을 사용하면 
else 조건으로 나오는 값의 자료형도 iterable이어야 한다는 점을 새로 배웠음 
"""
import sys
import collections
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

visited = set()
ans = set()
q = collections.deque([(X, 0)])
while q:
    s, d = q.popleft()
    if s in visited:
        continue
    
    visited.add(s)
    
    if d == K:
        ans.add(s)
        continue
        
    
    for e in graph[s]:
        if e in visited:
            continue
        q.append((e, d+1))
print(*sorted(list(ans)) if ans else [-1], sep='\n')