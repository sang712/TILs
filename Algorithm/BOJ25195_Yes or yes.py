'''
DFS가 구현하기 편한 문제라 DFS로 풀었음
DFS를 돌다가 팬을 만나면 바로 return하도록 하였고
목적지까지 잘 도착하면 flag를 True로 만들어서 마지막에 flag에 따라 결과를 출력하도록 하였음
구현 모양이 이쁘지는 않음
python의 recursion limit 때문에 2번 틀렸음
기본이 1000이고 100001로 해도 recursion Error가 나길래 20만으로 설정해주고 통과하였음

골드 4문제는 아니고
실버 1문제같은 25194번 문제가 더 어려운 듯...
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    nodes[start].append(end)
    
S = int(input())
fans = set(map(int, input().split()))

flag = False
def dfs(start):
    if start in fans:
        return
    if not nodes[start]:
        global flag
        flag = True
        return
    for next in nodes[start]:
        dfs(next)

dfs(1)

if flag:
    print('yes')
else:
    print('Yes')