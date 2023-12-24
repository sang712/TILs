"""
source destination은 연막임
그냥 반복해서 두 구간이 겹치는지 확인하는 문제였음
두 구간 모두가 시작점, 시작점으로부터의 시간으로 주어진다는 점을 제대로 파악하지 못해 틀렸음
"""
import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    calls = [list(map(int, input().split())) for _ in range(N)]
    
    ans = []
    for _ in range(M):
        s, d = map(int, input().split())
        cnt = 0
        for _, _, start, duration in calls:
            if start + duration <= s or s + d <= start:
                continue
            cnt += 1
        ans.append(cnt)
    
    print(*ans, sep='\n')