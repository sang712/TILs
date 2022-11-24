'''
딱 보고 dp라고 생각해서 dp로 풀었고
제한 조건으로 n이 11까지여서 아예 dp리스트를 만들어서 호출하도록 하였음
'''
import sys
input = sys.stdin.readline

T = int(input())

dp = [0, 1, 2, 4]

for i in range(4, 12):
  dp.append(sum(dp[i-3:]))

for _ in range(T):
  n = int(input())
  print(dp[n])
