"""
어느 한 점에서 어느 한 직선에 내리는 수선의 발을 구해서 문제를 풀려고 했는데
문제에서는 기차가 뒤로 가지 않기 때문에 문제가 발생할 수 있음

그래서 기차를 dx, dy만큼씩 움직이며 거리를 계산하여 결과를 얻도록 하였고
dx와 dy가 정수로 나누어 떨어지는 경우, 중간 위치를 생략하게되는 경우가 생김
그래서 dx, dy를 각각 최대공약수로 나누어 주었고 이때 음수 최대 공약수가 나오지 않도록
abs를 취해주었음
"""
xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
dxdy_gcd = gcd(abs(dx), abs(dy))
dx, dy = dx // dxdy_gcd, dy // dxdy_gcd

while (xs - xe) ** 2 + (ys - ye) ** 2 > (xs - xe - dx) ** 2 + (ys - ye - dy) ** 2:
    xe += dx
    ye += dy

print(xe, ye)

# a = dy
# b = - dx
# c = - dy * xe + dx * ye
# # print(f'{a}x + {b}y + {c} = 0')

# '''
# 어느 한 점(xs, yx)에서 직선(ax + by + c = 0)에 내린 수선의 발의 좌표는
# x = (b(bxs - ays) - ac) / (a^2 + b^2), y = (a(-bxs + ays) - bc) / (a^2 + b^2)
# '''
# x = (b * (b * xs - a * ys) - a * c) // (a ** 2 + b ** 2)
# y = (a * (- b * xs + a * ys) - b * c) // (a ** 2 + b ** 2)
# print(x, y)