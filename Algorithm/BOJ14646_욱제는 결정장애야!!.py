"""
숫자가 딱 한 번 나왔을 때만 카운트하여 그 개수의 최댓값을 출력하는 문제
set 자료 구조를 이용해서 한 번만 나온 숫자를 저장하였고
이 때 숫자들의 개수를 카운트하는 변수를 따로 두어 연산하도록 하였음
그 후에 카운트 숫자가 커지는 경우에만 최댓값을 구하도록하여
최댓값을 출력하였음
"""
N = int(input())
roulette = set()
max_stickers = 0
stickers = 0
for n in input().split():
    if n in roulette:
        roulette.remove(n)
        stickers -= 1
    else:
        roulette.add(n)
        stickers += 1
        if stickers > max_stickers:
            max_stickers = stickers
print(max_stickers)