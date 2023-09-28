"""
입력을 받아 정렬을 한 뒤에
계란을 살 필요가 없는 사람을 제외하고 for문을 돌면서 예상 수익을 계산하여 최댓값을 계산하였음

조건을 만족하지 않는 경우 바로 답이 나오는 것이 아니기 때문에 탈출 하면 안 되고
끝까지 확인을 하도록 하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

people = [int(input()) for _ in range(M)]
people.sort()


max_price = 0
ans = 0
for i in range(max(0, M - N), M):
    price = people[i]
    expected_profit = price * (M - i)
    if expected_profit > max_price:
        max_price = expected_profit
        ans = price
    
print(ans, max_price)