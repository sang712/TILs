"""
우선 필요한 것은 가장 싼 패키지의 값과 가장 싼 낱개의 값이라 두 값만 뽑도록 하였음
패키지 값이 더 싸면 우선 6의 배수 분량은 모두 패키지로 사고
나머지는 낱개가 싼지, 패키지로 한번에 사는 게 싼지 비교하여 구매하도록 하였음
애초에 패키지보다 낱개가 싸다면 그냥 모두 낱개로 사도록 하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
packages = []
unit = []
for _ in range(M):
    price_package, price_unit = map(int, input().split())
    
    packages.append(price_package)
    unit.append(price_unit)
    
min_price_package = min(packages)
min_price_unit = min(unit)

ans = 0
if min_price_package / 6 < min_price_unit:
    ans += (N // 6) * min_price_package
    N %= 6
    if N * min_price_unit < min_price_package:
        ans += N * min_price_unit
    else:
        ans += min_price_package
else:
    ans += N * min_price_unit
print(ans)