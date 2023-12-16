"""
각종 정보를 딕셔너리에 저장하고
items로 뽑은 뒤 정렬을 하였음

까다로웠던 것은 마지막에 제출한 것이 빠른 순으로 정렬하는 것이었는데
마지막에 제출한 순서를 저장하는 변수를 따로 생성해 처리하였음
"""
import sys
input = sys.stdin.readline

for T in range(int(input())):
    n, k, t, m = map(int, input().split())
    teams = {}
    summitted = [0] * (n + 1)
    for summit in range(m):
        i, j, s = map(int, input().split())
        teams.setdefault(i, [0] * (k + 1))
        teams[i][0] += 1
        teams[i][j] = max(teams[i][j], s)
        summitted[i] = summit
    
    result = sorted(list(teams.items()), key=lambda x: (-sum(x[1][1:]), x[1][0], summitted[x[0]]))
    rank = 1
    for team, _ in result:
        if team == t:
            print(rank)
            break
        rank += 1
