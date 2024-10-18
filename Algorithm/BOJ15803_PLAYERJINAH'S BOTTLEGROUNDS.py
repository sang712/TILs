"""
주어진 3개의 점이 직선인지를 판별하는 공식을 적용하였음
세점으로 2*3 매트릭스를 만들어 외적을 하는 방법임
이 공식의 결과값이 0이면 직선, 
양수이면 반시계, 음수이면 시계방향으로 진행함을 알 수 있고
2로 나누면 그 점들로 이루어진 삼각형의 넓이를 알 수 있음
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

d = x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2

if d:
    print('WINNER WINNER CHICKEN DINNER!')
else:
    print('WHERE IS MY CHICKEN?')
