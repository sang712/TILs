"""
dp방식으로 이전 값과 현재 값의 곱과 현재 값을 비교하여 큰 값을 저장하도록 하였고
dp로 값을 모두 연산했으면 그 중에서 가장 큰 값을 구해 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
dp = [float(input())]
for i in range(N-1):
    realnum = float(input())
    dp.append(max(realnum, dp[i]*realnum))
print(f'{max(dp):0.3f}')