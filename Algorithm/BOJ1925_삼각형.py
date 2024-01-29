"""
삼각형을 이룰 때 만족해야 하는 각 변간의 관계를 식으로 써서 
분기를 나눠 그에 맞게 결과를 출력하도록 하였음

1열에 있다는 것은 식으로 나타내면 작은 두 변의 길이의 합이 긴 변의 길이와 같을 때 이므로
그렇게 표현하였음
"""
points = [list(map(int, input().split())) for _ in range(3)]
sides = []

for i in range(3):
    ax, ay = points[i]
    bx, by = points[i-1]
    sides.append((ax-bx)**2 + (ay-by)**2)

sides.sort()

if sides[0] ** 0.5 + sides[1] ** 0.5 <= sides[2] ** 0.5:
    print('X')
elif sides[0] == sides[1] or sides[1] == sides[2]:
    if sides[0] == sides[2]:
        print('JungTriangle')
    elif sides[0] + sides[1] > sides[2]:
        print('Yeahkak2Triangle')
    elif sides[0] + sides[1] == sides[2]:
        print('Jikkak2Triangle')
    else:
        print('Dunkak2Triangle')
else:
    if sides[0] + sides[1] > sides[2]:
        print('YeahkakTriangle')
    elif sides[0] + sides[1] == sides[2]:
        print('JikkakTriangle')
    else:
        print('DunkakTriangle')