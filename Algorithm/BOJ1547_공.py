import sys
input = sys.stdin.readline

M = int(input())
ball = 1
for _ in range(M):
    cup_from, cup_to = map(int, input().split())
    if cup_from == ball:
        ball = cup_to
    elif cup_to == ball:
        ball = cup_from
        
print(ball)