"""
가장 빠르게 도착하는 몬스터만 고려하면 되기 때문에 나눗셈으로 몫이 가장 작은 몬스터를 찾았고
몬스터가 도착하면 지민이가 붙잡히는 것이므로 거리에 -1을 해주어 도착하지 않는 최대의 시간을 계산하도록 하였음
그렇게 가장 빨리 도착하는 몬스터가 걸리는 시간을 찾아냈으면
몬스터와 같은 위치라면 0을 출력하였고
몬스터가 주어진 시간 내에 도착하면 몬스터가 도달하기 까지 걸리는 시간과 
남은 시간 중 2초에 당 1번씩 금화를 가져갈 수 있으므로 이를 더해 출력하였고
그 외에 경우는 주어진 시간내에 몬스터가 도달하지 못 하는 경우로 그냥 막 금화를 가져가도 상관없으므로
그냥 시간과 금화를 곱해 출력하였음
"""
import sys
input = sys.stdin.readline
t, x, m = map(int, input().split())

min_time = 1_000_000
for _ in range(m):
    d, s = map(int, input().split())
    time = (d-1) // s if s > 0 else 0
    if min_time > time:
        min_time = time

ans = 0
if min_time == 0:
    pass
elif t > min_time:
    ans = min_time * x
    t -= min_time
    ans += (t // 2) * x
else:
    ans = t * x

print(ans)