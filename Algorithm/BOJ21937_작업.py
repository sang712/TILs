import sys
input = sys.stdin.readline

N, M = map(int, input().split())

works = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    works[B].append(A)

X = int(input())
stack = [X]
stack.append(X)
count = 0
while stack:
    node = stack.pop()
    # visited를 여기서 체크하면 스택에 직접 넘어가기 전에 스택에 쌓인 경우 2번 체크 되기 때문에 안됨
    for prev_node in works[node]:
        if not visited[prev_node]:
            stack.append(prev_node)
            visited[prev_node] = 1
            count += 1

print(count)

'''
반례 1
4 4
1 2
1 3
2 4
3 4
4
'''
'''
반례 2
5 6
1 3
1 4
2 3
2 4
3 5
4 5
5
'''
