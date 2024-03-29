"""
순서대로 쌓여있는 카드에서 바지는 순서대로 구성해 출력하면 되는 줄 알았는데 그게아니고
거꾸로 덱을 구성해나가는 방식으로 구현하는 방식으로 풀어야 했음
"""
from collections import deque
N = int(input())
q = deque()
q.append(N)

for i in range(N-1, 0, -1):
    q.appendleft(i)
    for j in range(i):
        q.appendleft(q.pop())

print(*q)