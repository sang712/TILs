"""
플레이어별로 카드를 입력으로 받아올 때 정렬을 하여 받아 왔고
맨 마지막 값들을 pop하여 최댓값과 같으면 이긴 사람 목록에 넣고
최댓값보다 크면 이긴 사람 목록을 초기화하는 방식으로 풀었음

마지막 점수 공동1등 또한 위와 같은 방식으로 뽑아 출력하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

players_card = []
scores = []
for _ in range(N):
	players_card.append(sorted(list(map(int, input().split()))))
	scores.append(0)

for _ in range(M):
    max_card = 0
    winner = []
    for i in range(N):
        card = players_card[i].pop()
        if max_card == card:
            winner.append(i)
        elif max_card < card:
            max_card = card
            winner = [i]
            
    for player in winner:
        scores[player] += 1

max_score = 0
the_winner = []
for player, score in enumerate(scores):
    if score == max_score:
        the_winner.append(player + 1)
    elif score > max_score:
        the_winner = [player + 1]
        max_score = score
print(*sorted(the_winner))