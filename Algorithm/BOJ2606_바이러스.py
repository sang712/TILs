'''
양쪽으로 이동이 가능하게 연결이된 컴퓨터를 2차원 리스트로 표현하고
stack을 이용한 dfs를 구현하여 해결하였음
'''
import sys
input = sys.stdin.readline

num_computer = int(input())
computers = [[] for _ in range(num_computer + 1)]

num_pair = int(input())
for pair in range(num_pair):
    com1, com2 = map(int, input().split())
    computers[com1].append(com2)
    computers[com2].append(com1)
    
visited = [0] * (num_computer + 1)
stack = [1]

cnt = 0
while stack:
    com = stack.pop()
    if visited[com]:
        continue
    else:
        visited[com] = 1
        cnt += 1
        stack += computers[com]

print(cnt-1)