A, B, C = map(int, input().split())
D = int(input())

B1, C1 = divmod(D, 60)
A1, B1 = divmod(B1, 60)

B2, C = divmod(C + C1, 60)
A2, B = divmod(B + B1 + B2, 60)
A = (A + A1 + A2) % 24

print(A, B, C)