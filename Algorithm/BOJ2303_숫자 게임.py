"""
문제에서 요구한 사항을 시간복잡도 고려 없이 그대로 구현하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
winner = 0
score_winner = 0
for person in range(N):
    cards = list(map(int, input().split()))
    score = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                score = max(score, (cards[i] + cards[j] + cards[k]) % 10)
    if score_winner <= score:
        winner = person + 1
        score_winner = score
print(winner)
