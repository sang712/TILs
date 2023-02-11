"""
친족 관계를 2차원 리스트로 만들었고
만든 친족 관계를 BFS로 탐색하면서 몇 번을 거치면 만나게 되는지 계산하여 출력하도록 구현 하였음
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
person1, person2 = map(int, input().split())

m = int(input())
relationship = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    relationship[x].append(y)
    relationship[y].append(x)
    
q = deque()
q.append((person1, 0))
visited = [0] * (n + 1)
visited[person1] = 1
ans = -1
while q:
    person, relation = q.popleft()
    if person == person2:
        ans = relation
        break
    for related in relationship[person]:
        if not visited[related]:
            q.append((related, relation + 1))
            visited[related] = 1
print(ans)