"""
각 군대의 병사에 주인 정보를 포함하여 합친 뒤 정렬하여 맨 마지막 값을 얻어 출력하였음
"""
import sys


input = sys.stdin.readline
ans = []
for t in range(int(input())):
    input()
    N, M = map(int, input().split())
    s = list(map(lambda x: (int(x), 'S'), input().split()))
    b = list(map(lambda x: (int(x), 'B'), input().split()))
    
    battle = sorted(s + b)
    ans.append(battle[-1][1])
print(*ans, sep='\n')