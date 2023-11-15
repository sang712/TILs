T = int(input())
_ = input()
num = 0
cnt = 0
for _ in range(T):
    try: 
        candy = input()
        while not candy == '':
            num += int(candy)
            cnt += 1
            candy = input()
        
        if num % cnt == 0:
            print('YES')
        else:
            print('NO')
        num, cnt = 0, 0
    except EOFError:
        break

        