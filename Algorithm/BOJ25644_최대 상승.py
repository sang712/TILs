"""
최솟값을 계속 저장하면서
현재 값과 최솟값의 차이가 최대가 되는 경우만을 저장해 출력하였음
"""
N = int(input())
stock = list(map(int, input().split()))

min_price = stock[0]
ans = 0
for price in stock:
    if price > min_price:
        ans = price - min_price
    min_price = min(price, min_price)
print(ans)