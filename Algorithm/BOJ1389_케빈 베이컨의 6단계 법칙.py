'''
문제를 읽고 연결된 사람을 타고 타고 넘어갔을 때의 단계를 계산해 주어야 하기 때문에 BFS로 구현하였음
우선 입력이 1부터 시작되기 때문에 N+1 크기의 2차원 리스트를 만들고
두 사람의 관계가 입력이 되었을 때 각각의 관계에 해당하는 리스트에 append로 추가하였음
그 후에 각 사람별로 케빈 베이컨의 수를 구하기 위해 1부터 N+1까지 for문을 돌려서
for문의 i에 해당하는 사람부터 시작하는 BFS를 돌림
BFS를 돌려서 케빈 베이컨 수를 구했으면 그 수가 가장 작은지 비교하고
가장 작다면 케빈 베이컨을 갱신하여 출력함

N의 수가 100까지여서 
N*N의 관계 2차원 리스트를 만드는 것보다 
N*A의 2차원 리스트를 만들어 사용하는 것이 빠르다고 판단하였음
40ms 소요됨
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

relationships = [[] for _ in range(N + 1)]

for _ in range(M):
    person1, person2 = map(int, input().split())
    relationships[person1].append(person2)
    relationships[person2].append(person1)

min_sum_of_degree = 100000
kevin_bacon = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    
    visited[i] = 1
    stack = [(related, 1) for related in relationships[i]]
    
    sumation_of_degree = 0
    while stack:
        related, degree = stack.pop(0)
        
        if not visited[related]:
            visited[related] = 1
            sumation_of_degree += degree
            for next in relationships[related]:
                stack.append((next, degree + 1))

    if min_sum_of_degree > sumation_of_degree:
        min_sum_of_degree = sumation_of_degree
        kevin_bacon = i
print(kevin_bacon)
        
    