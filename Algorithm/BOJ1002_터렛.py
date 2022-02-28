for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = pow(pow(x1-x2, 2) + pow(y1-y2, 2), 1/2)
    '''
    1. 원이 서로 멀어 만나지 않는 경우
        d > r1 + r2, OUTPUT = 0
    2. 원이 서로 외접하는 경우
        d = r1 + r2, OUTPUT = 1
    3. 원이 두 점에서 만나는 경우
        |r1 - r2| < d < r1 + r2, OUTPUT = 2 
    4. 원이 내접하는 경우
        d = |r1 - r2|, OUTPUT = 1
    5. 원이 겹치는 경우
        d = 0, r1 = r2, OUTPUT = -1
    6. 원이 원 안에 존재하는 경우
        d < |r1 - r2|, OUTPUT = 0
    '''
    if d > r1 + r2:
        print(0)
    elif d == r1 + r2:
        print(1)
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    elif d == abs(r1 - r2):
        print(1)
    elif d == 0 and r1 == r2:
        print(-1)
    elif d < abs(r1 - r2):
        print(0)