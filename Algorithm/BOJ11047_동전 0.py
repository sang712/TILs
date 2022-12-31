'''
조건에는 없었지만 원하는 금액이 동전의 조합으로 만들 수 있는 수라고 가정하고 문제를 풀었음
동전의 액면이 큰 수대로 돌면서 K의 값에서 뺄 수 있는 만큼 빼고
그 수를 동전의 개수에 더해서 마지막에 출력하도록 구현하였음
'''
N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input()))
    
coins.sort(reverse=True)

num_coin = 0
i = 0
while K and i < N:
    coin = coins[i]
    if K >= coin:
        num_coin += K // coin
        K %= coin
    i += 1
print(coins)
print(num_coin)