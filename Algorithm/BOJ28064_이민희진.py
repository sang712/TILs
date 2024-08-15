"""
입력을 받아서 각 문자열의 앞과 뒤로 끝나거나 시작하는 것을 확인하여 카운팅하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
people = [input().strip() for _ in range(N)]

ans = 0
for i in range(N-1):
    s = people[i]
    for j in range(i+1, N):
        t = people[j]
        min_len = min(len(s), len(t))
        for k in range(1, min_len+1):
            if s.startswith(t[-k:]) or s.endswith(t[:k]):
                ans += 1
                break
            elif t.startswith(s[-k:]) or t.endswith(s[:k]):
                ans += 1
                break
print(ans)