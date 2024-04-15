"""
자리를 바꾸는 경우와 바꾸지 않는 경우를 dp로 카운팅하는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
vip = set([int(input()) for _ in range(M)])
dp = [(1, 0)]
for i in range(1, N):
    not_changed, changed = dp[-1]
    if i not in vip and i+1 not in vip:
        dp.append((not_changed + changed, not_changed))
    else:
        dp.append((not_changed+changed, 0))
print(sum(dp[-1]))
