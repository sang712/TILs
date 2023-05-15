"""
돼지가 다음날에 요구하는 사료의 총량의 규칙을 찾아서 구현하였음
돼지가 요구하는 사료의 총량은 날이 지날때마다 4씩 증가함
"""
for t in range(int(input())):
    N = int(input())
    pig_food = sum(map(int, input().split()))
    day = 1
    while N >= pig_food:
        pig_food *= 4
        day += 1
    print(day)
    