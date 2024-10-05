"""
insert함수를 이용해 주어지는 입력을 등수에 맞게 리스트에 삽입하여 문제를 풀이하였음
"""
N, M = map(int, input().split())
first_lap = []
for i in range(1, N+1):
    rank = int(input())
    first_lap.insert(rank-1, i)

second_lap = []
for j in range(M-1, -1, -1):
    rank = int(input())
    second_lap.insert(rank-1, first_lap[j])
print(*second_lap[:3], sep='\n')
