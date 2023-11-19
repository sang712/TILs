"""
주어진 N이 홀수라는 것이 힌트
"""
import sys
input = sys.stdin.readline

N = int(input())
sum_of_candies = [int(input()) for _ in range(N)]

sumation = 0
plus_minus = 1
for candies in sum_of_candies:
    sumation += plus_minus * candies
    plus_minus *= -1

first_kid = sumation // 2

ans = [first_kid]
for i in range(N - 1):
    ans.append(sum_of_candies[i] - ans[-1])
    
print(*ans, sep='\n')