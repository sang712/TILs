# 정렬이 되어있다는 말이 없으므로 break 문으로 중간에 탈출하지 않고 처음부터 끝까지 확인해야함

N, M = map(int, input().split())
cards = list(map(int, input().split()))

blackjack = 0
biggest = 0
for i in range(N):
    blackjack += cards[i]
    for j in range(i+1, N):
        blackjack += cards[j]
        for k in range(j+1, N):
            blackjack += cards[k]
            if blackjack <= M:
                if blackjack >= biggest:
                    biggest = blackjack
            blackjack -= cards[k]
        blackjack -= cards[j]
    blackjack -= cards[i]
print(biggest)
