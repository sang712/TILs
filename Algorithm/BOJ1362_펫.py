scenario = 0
while True:
    o, w = map(int, input().split())
    if o == w == 0:
        break
    scenario += 1
    is_alive = True
    while True:
        command, num = input().split()
        if command == '#':
            break
        elif command == 'E':
            w -= int(num)
        elif command == 'F':
            w += int(num)
            
        if w <= 0:
            is_alive = False
    if not is_alive:
        print(f'{scenario} RIP')
    elif o / 2 < w < o * 2:
        print(f'{scenario} :-)')
    else:
        print(f'{scenario} :-(')
    