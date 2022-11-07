import sys
input = sys.stdin.readline

N = int(input())
max_prize = 0
for _ in range(N):
    dice = list(map(int, input().split()))
    
    prize = 0
    for i in range(1, 7):
        if dice.count(i) == 3:
            prize = 10000 + i * 1000
            break
        if dice.count(i) == 2:
            prize = 1000 + i * 100
            break
    else:
        prize = max(dice) * 100
    max_prize = max(prize, max_prize)
print(max_prize)