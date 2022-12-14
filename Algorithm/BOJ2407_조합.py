'''
파이썬은 자료형에 대해 고민할 필요가 없어서 그냥 combination을 구하는 방법을 구현하였고
연산수를 줄이기 위해 nCm = nC(n-m)라는 combiantion의 정리를 적용하였음
'''
n, m = map(int, input().split())

m = min(n-m, m)
num = 1
for i in range(n - m + 1, n + 1):
    num *= i
for j in range(1, m+1):
    num //= j
print(num)