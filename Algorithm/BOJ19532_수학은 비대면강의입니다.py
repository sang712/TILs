"""
x나 y의 계수가 0일 때 ZeroDivisionError가 나올 수 있기 때문에 해당 부분을 고려해야함
"""
a, b, c, d, e, f = map(int, input().split())
y = (c*d - f*a) // (b*d - e*a)
x = (c - b*y) // a if a else (f - e*y) // d
print(x, y)