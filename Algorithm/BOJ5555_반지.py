"""
찾으려는 문자열이 반지의 문자열의 길이인 10을 초과하지 않으므로
그냥 반지의 문자열을 이어 붙여서 찾으려는 문자열이 있는지 확인하였음
"""

import sys

S = input()
N = int(input())
rings = [sys.stdin.readline().strip() * 2 for _ in range(N)]

cnt = 0
for ring in rings:
    if S in ring:
        cnt += 1
        
print(cnt)