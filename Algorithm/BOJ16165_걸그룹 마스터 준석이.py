"""
탐색시간의 단축과 편의를 위해 양방향으로 각각 dictionary를 만들었음
"""
girlgroup = {}
member = {}
N, M = map(int, input().split())
for _ in range(N):
    group_name = input().strip()
    group = []
    for _ in range(int(input())):
        member_name = input().strip()
        member[member_name] = group_name
        group.append(member_name)
    girlgroup[group_name] = sorted(group)
for _ in range(M):
    quiz = input().strip()
    if int(input()) == 0:
        print(*girlgroup[quiz], sep='\n')
    else:
        print(member[quiz])