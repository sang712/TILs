eye1, eye2, eye3 = map(int, input().split())
dice = [0 for _ in range(7)]
dice[eye1] += 1
dice[eye2] += 1
dice[eye3] += 1

if max(dice) == 3:
    print(10000 + eye1 * 1000)
elif max(dice) == 2:
    print(1000 + dice.index(2)*100)
else:
    print(max(eye1, eye2, eye3) * 100)