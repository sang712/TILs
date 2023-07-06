import sys
input = sys.stdin.readline

N = int(input())

hand_comb = set()
for _ in range(N):
    finger1, finger2 = map(int, input().split())
    hand_comb.add((finger1, finger2))

if len(hand_comb) == 3 and ((1, 3) in hand_comb or (3, 1) in hand_comb) and ((1, 4) in hand_comb or (4, 1) in hand_comb) and ((4, 3) in hand_comb or (3, 4) in hand_comb):
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')