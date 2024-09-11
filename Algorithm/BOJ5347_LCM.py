"""
최대공약수를 구해서
a와 b를 곱한 수에 최대공약수로 나눠 최소공배수를 구하였음
"""
n = int(input())

def gcd(l, k):
    if l%k: return gcd(k, l%k)
    return k

for _ in range(n):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))