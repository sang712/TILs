A, B = map(int, input().split())
C = int(input())
A += (B + C) // 60
B = (B + C) % 60
A %= 24

print(A, B)