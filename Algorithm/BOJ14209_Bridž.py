N = int(input())

# define krde
points = {'A': 4, 'K': 3, 'Q': 2, 'J': 1, 'X': 0}

total_points = 0

# Iterate over each hand dealt
for _ in range(N):
    hand = input().strip()  
    #sum
    for card in hand:
        total_points += points[card]

print(total_points)
