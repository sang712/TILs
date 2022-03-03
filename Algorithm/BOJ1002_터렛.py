for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 1 / 2)
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
    '''
    ~~실수1. d를 구하는 과정에서 루트를 씌우게 되면서 생기는 오차가 있음
    그래서 d를 구해서 ==으로 비교를 하게되면 무조건 false가 나옴
    따라서 d를 구해서 비교하지 말고 d의 제곱을 구해서 비교를 하는 방법을 사용해야함
    -> 이거 상관 없음 그냥 됨~~
    실수2. 위의 경우 5번이 경우 4번에 선행되어야 함
    안 그러면 반지름의 차이와 원의 중점 사이의 거리가 같아지는 순간 1을 반환함
    '''
    if d > r1 + r2:
        print(0)
    elif d == r1 + r2:
        print(1)
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    elif d == 0 and r1 == r2:
        print(-1)
    elif d == abs(r1 - r2):
        print(1)
    elif d < abs(r1 - r2):
        print(0)