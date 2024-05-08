"""
문제에서 요구하는 대로 구현하였음
플러시나 스트레이트는 풀하우스 ~ 페어와 같은 숫자 조합과는 양립 불가하기 때문에 우선 판정하였음
"""
cards = []
for _ in range(5):
    color, num = input().split()
    cards.append((color, int(num)))
cards.sort(key=lambda x: x[1])
counter = {cards[i][1]: list(zip(*cards))[1].count(cards[i][1]) for i in range(5)}

is_plush = cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0]
is_straight = cards[4][1] == cards[3][1]+1 == cards[2][1]+2 == cards[1][1]+3 == cards[0][1]+4

score = 0
if is_plush:
    if is_straight:
        score = 900 + cards[4][1]
    else:
        score = 600 + cards[4][1]
elif is_straight:
    score = 500 + cards[4][1]
else:
    if len(counter) <= 2:
        score = 700
        for num in counter:
            if counter[num] == 4:
                score += 100 + num
            elif counter[num] == 3:
                score += 10 * num
            elif counter[num] == 2:
                score += num
    elif len(counter) <= 3:
        for num in counter:
            if counter[num] == 3:
                score += 100 + num
            elif counter[num] == 2:
                score = max(score//10 + num * 10, num + score)
        score += 300
    elif len(counter) <= 4:
        for num in counter:
            if counter[num] == 2:
                score = 200 + num
    else:
        score = 100 + cards[4][1]
print(score)