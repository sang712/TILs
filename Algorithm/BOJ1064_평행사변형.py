"""
일직선일 경우 평행사변형이 안 되므로 일직선인 경우를 판별해야 함
짧은 직선거리 2개의 합이 나머지 1개와 같으면 직선이라고 판별했는데 틀렸다는 결과를 보여주었음
부동소수점 문제인 것 같아 직선 판별하는 부분을 두 직선의 기울기 비교로 수정하였더니 통과하였음

CCW 적용해도 됨
"""
xa, ya, xb, yb, xc, yc = map(int, input().split())

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

sides = [dist(xa, ya, xb, yb), dist(xb, yb, xc, yc), dist(xc, yc, xa, ya)]

sides.sort()

if (xa - xb) * (yb - yc) == (xb - xc) * (ya - yb):
    print(-1)
else:
    print((sides[2]-sides[0]) * 2)