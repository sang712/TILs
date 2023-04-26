"""
주어진 버거와 사이드메뉴, 음료의 가격 중 가장 비싼 것들로 세트메뉴를 만들었을 때
모든 메뉴의 가격의 합을 구하는 문제
주어지는 값을 정렬하여 가장 개수가 적은 것에 맞춰 더해주고
또 나머지는 나머지끼리 따로 더해주었음
그 후에 둘을 그냥 합한 값과 할인이 적용된 값을 출력하도록 하였음
"""
B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))
burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

num_sets = min(B, C, D)
sets = 0
for i in range(num_sets):
    sets += burgers[i] + sides[i] + drinks[i]
rests = sum(burgers[num_sets:] + sides[num_sets:] + drinks[num_sets:])

print(sets + rests)
print(sets * 9 // 10 + rests)