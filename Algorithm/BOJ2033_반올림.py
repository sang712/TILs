"""
문제 요구사항대로 구현하였음
"""
N = int(input())
for i in range(1, len(str(N))):
    mod = N % (10 ** i)
    N -= mod
    if mod // (10 ** (i - 1)) >= 5:
        N += 10 ** i
print(N)