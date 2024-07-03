"""
문제에서 요구하는 식을 계산하여 나타낸 식을 함수로 만들어 풀이하였음
"""
x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

def laser(x):
    return a * x ** 3 // 3 + (b - d) * x ** 2 // 2 + (c - e) * x

print(laser(x2) - laser(x1))