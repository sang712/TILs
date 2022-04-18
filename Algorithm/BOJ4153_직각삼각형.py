while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    isRightTriangle = False
    if a > b and a > c and a **2 == b**2 + c**2:
        isRightTriangle = True
    elif b > a and b > c and b**2 == a**2 + c**2:
        isRightTriangle = True
    elif c > a and c > b and c**2 == a**2 + b**2:
        isRightTriangle = True

    if isRightTriangle:
        print("right")
    else:
        print("wrong")