"""
오름차순으로 정렬되어 있으므로
가장 앞선 수는 할인된 가격이 분명하므로
for문으로 돌면서 0이 아닌지만 판단하고
0이 아니라면 원래가격의 인덱스를 찾아
그 수를 0으로 만드는 방법으로 짝을 지어주었음
"""
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    P = int(input())
    price_tags = list(map(int, input().split()))
    ans = []
    for price in price_tags:
        if price:
            price_tags[price_tags.index((price//3) * 4)] = 0
            ans.append(str(price))
    
    print(f'Case #{tc + 1}: {" ".join(ans)}')
