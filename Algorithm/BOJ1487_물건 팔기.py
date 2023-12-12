"""
가장 비싸게 팔았을 때부터 확인할 수 있도록 입력값을 비싸게 구매하겠다는 사람들 순으로 정렬하였고
그 후에는 판매했을 때 이익을 브루트포스로 확인하여 다 더해서 비교하였음
배송비가 더 커 손해가 나는 경우는 안 팔 수도 있으니 0으로 되도록 하였음
가장 낮은 값을 갖도록 하기위에서 크거나 같다 연산자를 사용했는데
이득이 전혀 나지 않는 상황은 예외로 답을 갱신하지 않도록 하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

customers = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (-x[0]))

max_profits = 0
ans = 0
for price, _ in customers:
    profits = 0
    for customer in customers:
        if customer[0] >= price:
            profits += max(price - customer[1], 0)
        else:
            break
    
    if profits > 0 and max_profits <= profits:
        max_profits = profits
        ans = price
print(ans)