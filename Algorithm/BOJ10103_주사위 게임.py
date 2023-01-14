n = int(input())
cy, sd = 100, 100
for _ in range(n):
    dice_cy, dice_sd = map(int, input().split())
    if dice_cy == dice_sd:
        continue
    elif dice_cy > dice_sd:
        sd -= dice_cy
    else:
        cy -= dice_sd
print(cy, sd, sep='\n')