"""
첫 버스보다 먼저 온 경우와 그렇지 않은 경우로 나눠서 비교하였음
만약 첫 버스보다 먼저 온 경우 남은 시간을 바로 저장하였고
그렇지 않다면 몇 번째 버스를 타야하는지 반복문을 통해 결정하고 
해당 버스를 타기위해 기다리는 시간을 계산하여 저장하였음
"""
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
ans = 1_000_000
for i in range(N):
    S, I, C = map(int, input().split())
    gap_ts = T - S
    bus_time = 0
    if gap_ts >= 0:
        for c in range(C):
            if bus_time >= gap_ts:
                ans = min(ans, bus_time-gap_ts)
                break
            bus_time += I
    else:
        ans = min(ans, -gap_ts)
print(ans if ans < 1_000_000 else -1)