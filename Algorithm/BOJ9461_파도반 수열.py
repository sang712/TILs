"""
문제에서 준 예시에서 규칙을 너무 잘 드러내 주어서
발견한 규칙을 토대로 다이내믹 프로그래밍으로 구현하였음
1부터 5까지는 규칙이 없다가 
6부터 직전 숫자와 5번 이전의 숫자의 합이 해당 숫자가 되는 규칙이 생김
"""
import sys

dp = [0, 1, 1, 1, 2, 2]
for tc in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    length = len(dp)
    if length > n:
        print(dp[n])
    else:
        for i in range(length, n + 1):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[n])