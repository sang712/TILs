for _ in range(3):
    sticks = sum(map(int, input().split()))
    if sticks == 1:
        print('C')
    elif sticks == 2:
        print('B')
    elif sticks == 3:
        print('A')
    elif sticks == 4:
        print('E')
    else:
        print('D')