"""
문제에서 요구하는 대로 구현하였음
"""
a, b = map(int, input().split())
R = int(input())
field = [[0] * R for _ in range(R)]
field[a][b] = 1

t = 0
while True:
    t += 1
    if a + b + 2 < R:
        a += 1
        b += 1
    else:
        a //= 2
        b //= 2
    field[a][b] += 1
    if field[a][b] > 1:
        break
print(t)