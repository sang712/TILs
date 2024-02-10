"""
우선 주어진 나무의 길이별로 + 1부터 가장 짧은 나무의 길이 만큼으로 잘라서 확인하는 방법으로 풀이했는데
가장 짧은 나무 길이보다 긴 길이로 잘랐을 때 이득이 되는 경우도 있어서
그냥 1부터 가장 긴 나무의 길이만큼씩 잘랐을 때로 수정하였음
잘랐을 때 나오는 결과물의 이익이 자르는 비용 때문에 0 이하가 된다면 자를 필요가 없기 때문에
이 부분을 처리해주어야 했음 안 해서 틀림
"""
import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
logs = sorted([int(input()) for _ in range(N)])

max_profit = 0
for length in range(1, logs[-1] + 1):
    profit = 0
    for log in logs:
        cut, remain = divmod(log, length)
        if remain:
            log -= remain
        else:
            cut -= 1
        unit_profit = log*W - cut*C
        if unit_profit > 0:
            profit += unit_profit
    max_profit = max(max_profit, profit)
print(max_profit)