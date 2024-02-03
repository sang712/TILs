"""
파이썬에서 제공하는 set 자료 구조를 사용하여 쉽게 풀이하였음
"""
n_A, n_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = A - B
n_A_B = len(A_B)
print(n_A_B)
if n_A_B:
    print(*sorted(list(A_B)))