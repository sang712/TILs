exchange = 1000 - int(input())

num_coins = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    while exchange >= coin:
        exchange -= coin
        num_coins += 1
        
print(num_coins)